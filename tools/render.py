"""Render HTML slides to Instagram-ready JPEGs with headless Chromium.

    python3 tools/render.py posts/<slug>/src/slide-*.html --out posts/<slug>/media            # feed 1080x1350
    python3 tools/render.py posts/<slug>/src/story.html --size 1080x1920 --out posts/<slug>/media

In your HTML: put {{BRAND}} inside <head> (inlines tools/brand.css with fonts), and use {{ROOT}} for repo files,
e.g. <img src="{{ROOT}}/brand/heartbeat-wordmark-black.svg">. Relative paths resolve from the HTML file's folder.
Output: <name>.jpg (quality 90, sRGB) next to a .png. IG wants JPEG, <=8 MB, aspect 4:5 to 1.91:1.
"""
import argparse, glob, os, pathlib, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent


def find_chrome():
    cands = [os.environ.get("CHROME", "")]
    cands += sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome"), reverse=True)
    cands += sorted(glob.glob("/opt/pw-browsers/chromium*/chrome"), reverse=True)
    cands += ["/opt/pw-browsers/chromium", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]
    cands += [shutil.which(n) or "" for n in ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable")]
    for c in cands:
        if c and os.path.isfile(c) and os.access(c, os.X_OK):
            return c
    sys.exit("No Chromium found. Set CHROME=/path/to/chrome (try: ls /opt/pw-browsers).")


def find_ffmpeg():
    if shutil.which("ffmpeg"):
        return shutil.which("ffmpeg")
    try:
        import imageio_ffmpeg
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", "imageio-ffmpeg"], check=True)
        import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def prepare(html_path: pathlib.Path, w: int, h: int) -> pathlib.Path:
    css = (ROOT / "tools/brand.css").read_text()
    src = html_path.read_text()
    root_uri = ROOT.as_uri()
    brand = f"<style>:root{{--w:{w}px;--h:{h}px}}\n{css}</style>"
    out = src.replace("{{BRAND}}", brand).replace("{{ROOT}}", root_uri)
    tmp = html_path.with_name(f".render-{html_path.name}")
    tmp.write_text(out)
    return tmp


def to_jpeg(png: pathlib.Path, jpg: pathlib.Path):
    try:
        from PIL import Image
        Image.open(png).convert("RGB").save(jpg, "JPEG", quality=90, optimize=True, progressive=False)
    except ImportError:
        subprocess.run([find_ffmpeg(), "-y", "-loglevel", "error", "-i", str(png), "-q:v", "2", str(jpg)], check=True)


def render(html: pathlib.Path, out: pathlib.Path, w: int, h: int, chrome: str) -> pathlib.Path:
    out.mkdir(parents=True, exist_ok=True)
    tmp = prepare(html, w, h)
    png = out / (html.stem + ".png")
    args = [chrome, "--headless=new", "--no-sandbox", "--hide-scrollbars", "--disable-gpu", "--force-device-scale-factor=1",
            f"--window-size={w},{h+200}", "--virtual-time-budget=8000", "--allow-file-access-from-files",
            f"--screenshot={png}", tmp.as_uri()]
    r = subprocess.run(args, capture_output=True, text=True)
    tmp.unlink(missing_ok=True)
    if not png.exists():
        sys.exit(f"render failed for {html}:\n{r.stderr[-2000:]}")
    cropped = png.with_name(png.stem + ".crop.png")
    subprocess.run([find_ffmpeg(), "-y", "-loglevel", "error", "-i", str(png), "-vf", f"crop={w}:{h}:0:0", str(cropped)], check=True)
    cropped.replace(png)
    jpg = out / (html.stem + ".jpg")
    to_jpeg(png, jpg)
    print(f"{jpg}  {jpg.stat().st_size // 1024} KB  {w}x{h}")
    return jpg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html", nargs="+")
    ap.add_argument("--out", required=True)
    ap.add_argument("--size", default="1080x1350")
    a = ap.parse_args()
    w, h = map(int, a.size.lower().split("x"))
    chrome = find_chrome()
    for f in a.html:
        render(pathlib.Path(f).resolve(), pathlib.Path(a.out).resolve(), w, h, chrome)


if __name__ == "__main__":
    main()
