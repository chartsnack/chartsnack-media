#!/bin/bash
# usage: pub.sh NN slug   -> copies yt+tt to queue, commits, pushes, uploads tt to cloudinary
set -e
N=$1; S=$2; cd /home/claude/chartsnack-media
cp /home/claude/chartsnack/ep$N/out/chartsnack_ep${N}_$S.mp4 queue/ep$N.mp4
cp /home/claude/chartsnack/ep$N/out_tt/chartsnack_ep${N}_${S}_tt.mp4 queue/tt$N.mp4
git add episodes/ep$N.py queue/ep$N.mp4 queue/tt$N.mp4 >/dev/null
git commit -qm "ep$N + tt$N" && git push -q 2>&1 | tail -1
curl -s -X POST https://api.cloudinary.com/v1_1/lxthmsnt/video/upload -F file=@queue/tt$N.mp4 -F upload_preset=chartsnack_upload -F public_id=tt$N | python3 -c "import json,sys; print(json.load(sys.stdin).get('secure_url'))"
