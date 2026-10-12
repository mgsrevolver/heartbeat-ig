#!/usr/bin/env bash
# Usage: tools/check_media.sh URL [URL...]
# Every URL must return HTTP 200 with an image/jpeg or video/mp4 content type, or this exits 1.
fail=0
for u in "$@"; do
  h=$(curl -sIL --max-time 30 "$u")
  code=$(printf '%s' "$h" | grep -i '^HTTP/' | tail -1 | awk '{print $2}')
  ct=$(printf '%s' "$h" | grep -i '^content-type:' | tail -1 | awk '{print $2}' | tr -d '\r;')
  if [[ "$code" == "200" && ( "$ct" == "image/jpeg" || "$ct" == "video/mp4" ) ]]; then echo "OK   $code $ct $u"; else echo "FAIL $code $ct $u"; fail=1; fi
done
exit $fail
