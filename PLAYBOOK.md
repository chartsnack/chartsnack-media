# Chart Snack – daily production playbook

Owner: Kurai (German speaker – talk to him in German). Channel language: English.
Goal: grow fast, pay for the Claude Max plan ($100/month) first via TikTok Creator Rewards, then grow side income.

## Channels
- YouTube: "Chart Snack", handle @chartsnacks, channel id UCxB9MReuCcVlW8DODL6L_0w (Studio: https://studio.youtube.com)
- TikTok: @chartsnack (Studio: https://www.tiktok.com/tiktokstudio/upload)
- Both are logged in inside the Claude desktop app's built-in browser on Kurai's PC "timo". Use the built-in browser tools.
- Kurai gave full permission to upload, schedule and publish, and to change anything on both channels.

## Format
- Animated data shorts, 1080x1920, 30 fps. YouTube: 60–70 s.
- TikTok (since 2026-11-09, test): separate 25–35 s cut per episode (template tools/tt/tt04.py, tt05.py: hook text visible at frame 0, 3–4 fast steps, payoff + "Follow for more"). Reason: avg watch time on TikTok was ~2 s with 0–2 views; the account first needs reach and retention, Creator Rewards (>1 min) comes later. Re-evaluate once TikTok views take off.
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
   Schedule: radio "Zeitplan" (confirm "Erlauben"), time picker `.tiktok-timepicker-option-list` (hours list, minutes list in 5-min steps), button "Planen". Or "Veröffentlichen" for now.
   Set the tab viewport to 1400x1000 while working, reset to desktop afterwards.
4. Times (Europe/Berlin): since 2026-11-11 TWO posts per day on both platforms: 12:00 and 19:00.
   Always continue from the last scheduled slot in LOG.md (no gaps, no double slots).
   Cloudinary upload also works from the YouTube Studio tab (console.cloudinary.com may log out).
   YouTube date picker only renders when the browser tab is in front (tabs_select first).

## Log
Append one line per published video to `LOG.md`: date, ep, topic, YouTube id, TikTok status.

## Notes learned
- TikTok profile is set up (name, bio, logo). Done.
- TikTok AI label: NOT set (Kurai's decision). Published TikToks cannot change the label afterwards (edit page has no toggle).
- TikTok scheduling via JS: date = click the yyyy-mm-dd input, then click `span.day.valid` with the day number; time = click the hh:mm input, then in `.tiktok-timepicker-option-list` (hours, then minutes) click the CHILD element of the option (`(opt.querySelector('*')||opt).click()`), verify input values before clicking "Planen".
- If "Weiter und veröffentlichen?" appears after "Planen", click "Abbrechen", wait ~30 s until "Keine Probleme gefunden", then "Planen" again.
- YouTube upload dialog opens directly via https://studio.youtube.com/channel/UCxB9MReuCcVlW8DODL6L_0w/videos/upload?d=ud
- Hook scene: make the first text visible at t=0 (appear start < 0) so the auto cover/first frame isn't dark.
- TikTok post ids appear in the content page HTML in row order (newest-scheduled first) – useful to identify rows.

## Learnings (2026-11-09)
- YouTube viewed-vs-swiped: ep01 seconds 55 % viewed, ep02 money 42 %, ep03 car-to-moon 9 % (dead). Big-number / money comparisons work; travel/space framing did not.
- TikTok: 60 s versions got 0–2 views; first 25 s cut (tt04 paper) got 441 views + 3 comments in 2 h. Keep TikTok at 25 s.
- Every new episode (from ep06): one file builds both versions: `python3 epNN.py yt` (60–65 s, out/) and `python3 epNN.py tt` (25 s, out_tt/). Template: episodes/ep06.py, uses lib.run().
- YouTube version gets the subscribe moment: 2.5 s scene `sub_scene()` before the last big reveal, VO "Subscribe for more.", and `outro_next("<teaser of next episode>")` at the end. Description ends with "A new chart snack every day – subscribe so you don't miss the next one."
- TikTok version: no subscribe scene, ends with "Follow for more".
- Hook text must be fully visible at frame 0 (no fade-in on the first scene).

## Learnings (2026-11-10, weekly run)
- YouTube has a DAILY UPLOAD LIMIT for unverified channels: after ~10 uploads in one day the dialog shows "Tägliches Upload-Limit erreicht" (done button disabled). Spread uploads: max ~9 per night, or Kurai verifies identity (Studio → Überprüfung starten, phone) to raise it. Failed/abandoned upload attempts count too.
- If the Claude desktop window is minimized/the Browser pane hidden, requestAnimationFrame never fires: YouTube's upload dialog stays width 0, TikTok's time picker updates very late. Fix: run this in the tab before opening dialogs:
  `window.requestAnimationFrame = cb => setTimeout(()=>cb(performance.now()),16); window.cancelAnimationFrame = id => clearTimeout(id);`
  On YouTube load /videos/short (no ?d=ud), patch, then open the dialog in-page (click ytcp-button "Erstellen" → item "Videos hochladen"). Keep the same page for all uploads (close success dialog with ytcp-button#close-button).
- Browser pane tabs need a size: if innerWidth is 0, call resize_window (e.g. 1280x900) on that tab.
- YouTube text: focus #textbox, getSelection().selectAllChildren(el), document.execCommand('insertText', false, text). Close hashtag suggestion popups: ytcp-social-suggestions-dropdown tp-yt-paper-dialog .close().
- YouTube date without calendar: open #datepicker-trigger, set the dd.mm.yyyy input + its tp-yt-paper-input .value, then dpkr=document.querySelector('ytcp-date-picker'); dpkr.onDateTextChange({target:paperInput, detail:{value}}); dpkr.onFormSubmit(new Event('submit')). Time: focus+select the time input in ytcp-datetime-picker via JS, then computer "type" "19:00" + Return. Verify both before #done-button.
- TikTok: typing emojis with the computer "type" action crashes the editor ("Es ist etwas schiefgelaufen"). Insert caption text+emoji with execCommand('insertText'), then type hashtags one by one with the computer tool.
- TikTok "Weiter und veröffentlichen?" dialog with "Jetzt veröffentlichen": never click that (would publish now). If the check hangs on "Überprüfung läuft" for >10 min, reload the upload page and re-inject the same Cloudinary file – the check then passes instantly.
- tools/scenes.py: reusable scene builders (hook, bars_scene, recap, statement) used by ep09+ to build episodes faster.
