"""Build a 9:16 Reel (H.264 + AAC, 30fps, faststart) from a scene list, plus a cover and a storyboard JPEG.

    python3 tools/reel.py posts/<slug>/reel.json

reel.json (paths relative to the json's folder):
{
  "out": "media/reel.mp4",
  "fade": 0.2,                       # seconds of fade-in/out per scene (0 = hard cuts)
  "audio": null,                     # optional path to an mp3/m4a you are licensed to use; else a silent track
  "scenes": [
    {"html": "src/scene-01.html", "seconds": 2.5},   # rendered at 1080x1920 via render.py
    {"image": "raw/shot.png", "seconds": 3},          # letterboxed onto cream
    {"video": "raw/screen.webm", "seconds": 6, "start": 0}  # e.g. a Playwright screen recording
  ]
}
Writes media/reel.mp4, media/reel-cover.jpg (first scene) and media/reel-storyboard.jpg (one frame per scene).
"""
import json, pathlib, subprocess, sys, tempfile
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import render as R

W, H, FPS = 1080, 1920, 30


def run(args):
    r = subprocess.run(args, capture_output=True, text=True)
    if r.returncode:
        sys.exit("ffmpeg failed:\n" + r.stderr[-3000:])


def main():
    spec_path = pathlib.Path(sys.argv[1]).resolve()
    base = spec_path.parent
    spec = json.loads(spec_path.read_text())
    ff, chrome = R.find_ffmpeg(), None
    fade = float(spec.get("fade", 0.2))
    out = (base / spec.get("out", "media/reel.mp4")).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    work = pathlib.Path(tempfile.mkdtemp(prefix="reel-"))
    fit = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=0xFFF7F0,"
           f"fps={FPS},format=yuv420p,setsar=1")
    segs, frames = [], []
    for i, s in enumerate(spec["scenes"], 1):
        t = float(s["seconds"])
        fx = fit + (f",fade=t=in:st=0:d={fade},fade=t=out:st={max(t - fade, 0):.3f}:d={fade}" if fade else "")
        seg = work / f"seg{i:02d}.mp4"
        if "html" in s:
            chrome = chrome or R.find_chrome()
            img = R.render((base / s["html"]).resolve(), work, W, H, chrome)
            run([ff, "-y", "-loop", "1", "-t", f"{t}", "-i", str(img), "-vf", fx, "-r", str(FPS), "-an", str(seg)])
        elif "image" in s:
            run([ff, "-y", "-loop", "1", "-t", f"{t}", "-i", str(base / s["image"]), "-vf", fx, "-r", str(FPS), "-an", str(seg)])
        else:
            run([ff, "-y", "-ss", str(s.get("start", 0)), "-t", f"{t}", "-i", str(base / s["video"]), "-vf", fx,
                 "-r", str(FPS), "-an", str(seg)])
        fr = work / f"frame{i:02d}.jpg"
        run([ff, "-y", "-ss", f"{min(t / 2, t - 0.05):.2f}", "-i", str(seg), "-frames:v", "1", "-q:v", "3", str(fr)])
        segs.append(seg); frames.append(fr)
    lst = work / "list.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in segs))
    total = sum(float(s["seconds"]) for s in spec["scenes"])
    audio = spec.get("audio")
    a_in = ["-i", str(base / audio)] if audio else ["-f", "lavfi", "-t", f"{total}", "-i", "anullsrc=r=44100:cl=stereo"]
    run([ff, "-y", "-f", "concat", "-safe", "0", "-i", str(lst), *a_in, "-map", "0:v", "-map", "1:a", "-shortest",
         "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-preset", "medium", "-crf", "20",
         "-g", str(FPS * 2), "-c:a", "aac", "-b:a", "128k", "-ar", "44100", "-movflags", "+faststart", str(out)])
    cover = out.with_name(out.stem + "-cover.jpg")
    run([ff, "-y", "-i", str(frames[0]), "-q:v", "2", str(cover)])
    n = len(frames)
    sb = out.with_name(out.stem + "-storyboard.jpg")
    inputs = sum((["-i", str(f)] for f in frames), [])
    run([ff, "-y", *inputs, "-filter_complex",
         "".join(f"[{k}:v]scale=270:480[s{k}];" for k in range(n)) + "".join(f"[s{k}]" for k in range(n)) + f"hstack=inputs={n}" if n > 1
         else "[0:v]scale=270:480", "-q:v", "3", str(sb)])
    print(f"{out}  {out.stat().st_size // 1024} KB  {total:.1f}s  ({n} scenes)\n{cover}\n{sb}")


if __name__ == "__main__":
    main()
