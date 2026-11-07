# Chart Snack – daily production playbook

Owner: Kurai (German speaker – talk to him in German). Channel language: English.
Goal: grow fast, pay for the Claude Max plan ($100/month) first via TikTok Creator Rewards, then grow side income.

## Channels
- YouTube: "Chart Snack", handle @chartsnacks, channel id UCxB9MReuCcVlW8DODL6L_0w (Studio: https://studio.youtube.com)
- TikTok: @chartsnack (Studio: https://www.tiktok.com/tiktokstudio/upload)
- Both are logged in inside the Claude desktop app's built-in browser on Kurai's PC "timo". Use the built-in browser tools.
- Kurai gave full permission to upload, schedule and publish, and to change anything on both channels.

## Format
- Animated data shorts, 1080x1920, 30 fps, 60–70 s (TikTok pays only for videos > 1 min).
- Strong hook in the first 2 s ("X = Y. So how long/big is Z?"), counters, bars, timelines, reveal, recap, outro "Follow Chart Snack".
- English AI voiceover (Kokoro, voice am_michael, speed 1.1) + self-generated music/SFX (no licensed music).
- Facts must be correct (check numbers; prefer pure math or stable, well-known figures). No sources needed in the description.
- Clickbait hooks OK, but title/description must not promise things the video doesn't deliver.
- Money/health topics OK as data, never as advice.
- Descriptions must NOT reveal the answer. End with a "guess before the end" prompt + hashtags.
- Hashtags: TikTok 6–8 per video (mix: 2 broad like #fyp #foryou, 2–3 format like #facts #didyouknow #learnontiktok, 2–3 topic-specific like #space #money), YouTube 5–7 incl. #shorts. Only relevant tags – no unrelated trending tags.
- Thumbnail/cover: choose a frame from the middle with a big number on screen (not the dark first frame).
- Each video: new topic, new research. Vary categories (numbers, money, space, geography, animals, everyday life, history).

## Tools (this repo)
- `tools/lib.py` – render kit (drawing helpers, scene renderer, music, voiceover, `build()`).
- `tools/example_ep02.py` – a complete episode script to copy.
- Setup in a fresh session:
  ```
  pip install --break-system-packages -q kokoro-onnx soundfile
  mkdir -p /home/claude/tts && cd /home/claude/tts
  curl -sL -o kokoro-v1.0.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
  curl -sL -o voices-v1.0.bin https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
  ```
  lib.py expects itself at /home/claude/chartsnack/lib.py (copy it there) and fonts Poppins (preinstalled).
- Before rendering everything: render stills of the busiest moments and look at them. Voice lines must report "OK" (fit their scene).

## Upload pipeline (no file dialog)
1. Commit the final mp4 to this repo under `queue/epNN.mp4` and push (main).
2. YouTube Studio: open upload dialog (Erstellen → Videos hochladen), then in page JS:
   fetch `https://raw.githubusercontent.com/chartsnack/chartsnack-media/main/queue/epNN.mp4` → File → DataTransfer → set `input[type=file].files` → dispatch `change`.
   Then: title, description, "Nein, nicht speziell für Kinder", Mehr anzeigen → KI-Frage "Ja", Weiter ×3, Sichtbarkeit: schedule (Veröffentlichungszeitpunkt festlegen) or Öffentlich.
3. TikTok blocks GitHub (CSP). Use Cloudinary (cloud `lxthmsnt`, unsigned preset `chartsnack_upload`):
   in the Cloudinary console tab (https://console.cloudinary.com) run JS: fetch the raw GitHub file, POST FormData(file, upload_preset, public_id) to `https://api.cloudinary.com/v1_1/lxthmsnt/video/upload` → `secure_url`.
   On https://www.tiktok.com/tiktokstudio/upload: fetch the secure_url → File → inject into `input[type=file]`.
   Caption: focus the `[contenteditable=true]`, select all, Delete, type text, then type each hashtag followed by a space.
   "Mehr anzeigen" → "KI-generierter Inhalt" switch on (confirm "Aktivieren").
   Schedule: radio "Zeitplan" (confirm "Erlauben"), time picker `.tiktok-timepicker-option-list` (hours list, minutes list in 5-min steps), button "Planen". Or "Veröffentlichen" for now.
   Set the tab viewport to 1400x1000 while working, reset to desktop afterwards.
4. Times (Europe/Berlin): main slot 19:00. Optional extra slots 15:00 / 23:00.

## Log
Append one line per published video to `LOG.md`: date, ep, topic, YouTube id, TikTok status.

## Open TODOs (do these at the start of the next run, then delete them here)
- Set up the TikTok profile (TikTok Studio / profile edit): name "Chart Snack", bio "The world, one chart at a time 📊 New chart snack every day.", profile picture = https://res.cloudinary.com/lxthmsnt/image/upload/v1794034995/profile.png (inject via fetch → File → input[type=file], same trick as videos).
- AI label: Kurai prefers no TikTok AI label because the content is not realistic. TikTok's dialog says labels are required for content "fully AI-generated or significantly edited by AI" – our visuals are code-made, only the voice is synthetic. Decide per TikTok's current wording; if it only targets realistic content, leave the label off.
