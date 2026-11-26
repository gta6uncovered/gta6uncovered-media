# GTA6 Uncovered: weekly batch runbook

Goal: USD 1,000/month from a faceless, AI-automated GTA 6 short-video channel (YouTube, TikTok, Instagram), English only.

## One-time setup in a fresh container
```
pip install --break-system-packages kokoro-onnx soundfile pillow numpy
mkdir -p /tmp/kk && cd /tmp/kk
# Kokoro v1.0 (Apache-2.0) from the kokoro-onnx GitHub releases
curl -sLO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
curl -sLO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
```
Footage (official Rockstar trailers, never committed to this repo): put them at `$FOOT/t1.mp4` and `$FOOT/t2.mp4` (default `/home/claude/footage`).
If missing, import each YouTube link with vidIQ `vidiq_video_upload` (url = the YouTube link), poll `vidiq_job_poll`, then download the returned storage.googleapis.com URL with curl:
- t1 = Grand Theft Auto VI Trailer 1 (Rockstar Games channel)
- t2 = Grand Theft Auto VI Trailer 2 (Rockstar Games channel)
Make contact sheets (one tile every 4 s) to pick shots: `ffmpeg -i t1.mp4 -vf "fps=1/4,scale=320:-1,tile=6x8" t1_sheet.jpg`.
Crops are built into engine.py: t1 is full-frame 1080p; t2 is letterboxed.

## Making a video
1. Copy a script from `tools/scripts/` into a new folder `work/bNN/script.py`. Edit NAME, SOURCE, LINES, SHOTS, CARDS, IMPACTS, TICKS, DROP, PROG.
2. `python3 -I tools/engine.py work/bNN voice` (Kokoro am_fenrir, speed 1.16)
3. `python3 -I tools/engine.py work/bNN preview`, then look at contact.jpg. Fix any text overflow or overlap.
4. `python3 -I tools/engine.py work/bNN full` produces `NAME.mp4` (1080x1920, 30 fps, -14 LUFS).
5. Copy to `videos/NNN-slug.mp4`, then commit and push (`git -c push.negotiate=true push origin HEAD`).
6. `vidiq_video_upload` url = `https://raw.githubusercontent.com/gta6uncovered/gta6uncovered-media/main/videos/NNN-slug.mp4`

## Content rules
- Hook (curiosity gap) in the first 1-2 s. Snowball story ("then... but then"). A visual change every 1-1.5 s, with a sound for each one. End on an unanswered question.
- Every number or claim must come from a source found this week; put it in SOURCE (shown on screen) and in the caption.
- Rockstar: mute the trailer music (the engine does this). No story spoilers or ending reveals, no long cutscenes.
- 15-21 s per video.

## Posting
- Accounts (platformAccountId):
  - YouTube: UCAgYSIVaPN90qmxf5ePCN_w
  - TikTok: _000_iNPEUYjS76n3j4kfNQfEN_8eQ-MVhuB
  - Instagram: DISABLED 24 Nov 2026, never use.
  - Facebook Page: 1471377252729945 (max 1 Reel/day at 7 PM UAE until 9 Dec; then max 2/day if no warnings)
- One `vidiq_social_post_draft_create` per video, with all three destinations.
  - YouTube: title, privacyStatus public, categoryId 20, tags.
  - TikTok: privacyLevel PUBLIC_TO_EVERYONE, allowComment true, musicUsageConfirmed true, isAiGenerated true. (These are the owner's standing choices.)
- Slots (UAE, UTC+4, approved 25 Nov): 5:00 AM (01:00 UTC), 1:00 PM (09:00 UTC), 7:00 PM (15:00 UTC), 3 Shorts/day on YouTube + TikTok.
  Thursday run = Sat 05:00 to Tue 19:00 UAE (12 Shorts) + weekly LONG on YouTube Sunday 6:00 PM UAE (14:00 UTC); Sunday 1 PM Short is TikTok-only.
  Monday run = Wed 05:00 to Fri 19:00 UAE (9 Shorts).
- PUBLISH ONLY AFTER Mohamed replies "approve week" to that batch.
- The vidIQ free plan allows 3 YouTube uploads per day; the limit resets at 08:00 UTC. Publish TikTok and Instagram at once. Send YouTube destinations 3 per day using `send_later` reminders at 08:10 UTC, in slot order.
- If he approves late and a slot has already passed, move that video to the end of the week and tell him.

## Clipping campaigns (Content Rewards, joined 23 Nov 2026 as "GTA6 Uncovered")
STATUS 23 Nov: BOTH PARKED. Owner cannot add in-app sounds by phone, and decided not to join the logo campaigns for now. Do NOT make clips for them. Revisit at the 10 Dec checkpoint. Then, only suggest campaigns that run fully automatically (no in-app sound, no manual steps).
Payouts only count after submitting each post's link on contentrewards.com (Submit clip). Owner approves posts as usual.

### 1) Whethan & DEV - Bass Down Low (GTA VI) - $1 per 1K views, max $150/clip, ends 31 Dec
- Brief: https://creatorbrief.artistinfluence.com/brief/xihujCHy4ZebW3plgeK2 (gameplay clip repo in Drive, 105 clips sorted by lane)
- TikTok + Instagram only. 20-60 s (aim 20+), vertical, hook in first 2 s, big change at +0:03, cut on the bass.
- MUST use the official "Bass Down Low" sound added inside the app (TikTok start 0:00, Instagram 0:00). So export the edit SILENT and the owner (or Chrome on TikTok Studio) adds the sound. API posting cannot attach it.
- One lane per edit: Chases & Getaways / Leonida Nights / Chaos & Fails / Graphics Flex (GTA 6 vs real Miami or GTA 5).
- Max one short line of text. Caption must include @whethan #GTAVI #GTA #BassDownLow. English. Likes + comments on. Never say "out now". No gore.
- Don't reuse the same clip across accounts. 1%+ like rate needed.

### 2) GTA 6 x GTA Clipper Tool - $0.70 per 1K views, TikTok + YouTube Shorts
- Rules: https://docs.google.com/document/d/1vkMGyT6ToXcsBjj2RofrpdJVKIpxgymTG44LMTwxzWQ/edit
- Footage: https://drive.google.com/drive/folders/14fw6Ow0X_xK_L7ikwuJ8udmKNikRQXgR
- A video ABOUT GTA Clipper (a clipping tool) with our own hook and voice. Reposting their examples gets rejected.
- Description must contain gtaclipper.com. Hashtags: #gta6 #gta6clipping #clipping #makemoney #gtaclipper. Keep the post up for 60 days. At least 50% of views must come from US/UK/CA/AU.
- The owner must join their Discord first (discord.gg/gtaclipper). It is a paid promotion, so set TikTok brandContent=true and disclose "paid partnership" on YouTube.
- Keep these posts off the main YouTube channel's normal style. Max 1 per week, so the channel stays GTA-news-first.

## Hook and outlier rules (our own notes, learned from studying the open-source "YouTube Agent Skill" idea, 23 Nov 2026)
- Write 5 candidate hooks per video and pick the strongest. Score each on 5 things: specific (a real number or a name), about the viewer ("you"), stakes (lose / never / before), an open question (why / but / until), and no filler words ("insane", "crazy", "guys", "today"). The weakest of the five counts most.
- Hook formulas that fit GTA 6 news shorts: The Statistic (a verified number + the consequence), The Comparison (X vs Y), The Reveal (a hidden fact), The Warning (don't buy / don't do X yet), The Question (an unresolved debate), Before & After, The Impossible Claim (only when it is true and sourced).
- Confirm the title or thumbnail promise in the first sentence. One idea per video.
- Outlier research: rank other creators' videos by views divided by that channel's median views (2x or more = outlier), never by raw views. Copy the FORMAT, never the footage.
- Retention: name the single biggest drop point (hook leak in the first 3 s, a cliff, or a slow slide) and make ONE change per week.

## Instagram status (24 Nov 2026): PERMANENTLY DISABLED (appeal failed). Never post to Instagram account 30103538905917108 again. Remove it from every draft.
## (history below)
- The Instagram account was suspended ("doesn't follow Community Standards"). Mohamed submitted an appeal with a selfie on 24 Nov. All scheduled IG posts were cancelled.
- Until vidiq_social_account_list shows Instagram with canPublish=true, leave Instagram OFF all drafts. Never retry repeatedly.
- After reinstatement, ramp up slowly to look human: week 1 = 1 Reel/day at 7 PM UAE, varied captions, no hashtag stuffing (3-5 tags), no near-duplicate videos. Then increase to 2/day only if there are no warnings.
- If the appeal fails, the account is permanently disabled and cannot be appealed again. Then propose a fresh Instagram account to Mohamed (it must be his own sign-up, with a 1-2 week manual warm-up before any automated posting), or drop Instagram and use Facebook Reels or YouTube instead.

## Reference reels Mohamed shared (24 Nov 2026), and lessons to apply
1. Facebook, "Ash and Claude" (AI VTuber setup, 2.5K reactions, ~1K comments): the caption says "Comment LIVE and I'll send you the guide". A comment-keyword CTA turns viewers into commenters, and comments are a top ranking signal. APPLY: end some videos with "Comment COST and I'll pin the full breakdown" (pin the answer as a reply; never promise DMs we can't send).
2. Instagram, @naan_babybro "Greedy brother Part 1" (AI-made toddler characters, a Malayalam/Tamil story series): 452.9K likes and 12.5K comments in 1 day, and most comments say "Part 2". APPLY:
   - SERIES + CLIFFHANGER. Split strong topics into Part 1 / Part 2 (e.g. "Real Cost of Vice City, Part 1: the skyline"), end on an open question, and post Part 2 within 24 h. "Part X" in the title makes viewers follow.
   - Emotion and story beat information. Wrap facts in a mini-story (who, what was at stake, the twist).
3. SECOND-NICHE CANDIDATE for the 10 Dec checkpoint: an AI-character story series in MALAYALAM for Facebook Reels. Facebook Content Monetization is open to UAE creators and supports Malayalam; Mohamed is a native speaker from Kerala. Needs AI image-to-video generation. Cost-check free or cheap options before proposing. Our English GTA pipeline stays as is.

## Facebook Page (created 24 Nov 2026 from Mohamed's own profile, Page name "GTA6 Uncovered")
- Connected to vidIQ on 24 Nov 2026 as FACEBOOK_PAGES, platformAccountId 1471377252729945. Count the first 2-week ramp from 25 Nov. Public URL: facebook.com/gta6uncoveredyt (profile id 61596809074624). Profile picture, cover, bio, YouTube + TikTok links and a pinned welcome post were added on 26 Nov.
- It replaces Instagram. Facebook Content Monetization is open to UAE creators (invite-only), so Facebook is a PAYING platform for us, unlike TikTok.
- Ramp-up, learned from the Instagram ban: weeks 1-2 = max 1 Reel/day at 7 PM UAE, varied captions, 3-5 hashtags, originality-first (Real Cost videos first). Raise to 2/day only after 2 clean weeks.
- Never send near-identical videos in a row to the Page. Rotate formats.

## Long-form (weekly Real Cost episode), added 26 Nov 2026
- Engine: `tools/engine_long.py` (1920x1080, 30 fps). Script = `work/LNN/script.py` with BEATS = [(narration, visual)]; one sentence per beat.
  Visuals: `c(SHOT, SHOT)` trailer clips from the clean-window library at the top of `tools/scripts/L01.py`; `card(bg, els, src)` with
  elements title/sub/counter/formula/bars/table/chips/map/stats/rule/assume/note/range; `chap(n, title, bg)` chapter cards.
- Steps: `voice` (Kokoro, files named by text hash so beats can be inserted) -> `preview` (contact.jpg + chapter times) -> `full` (JOBS=2, renders beats in parallel then concatenates) -> `thumb` (1280x720).
- Trailer windows: always pick start times from a 1 fps sheet and check brightness; t1 15-18 s, t3 15-17 s, 22-25 s and 72+ s have title cards; t2 0-7 s is black/fade.
- Rules: hook confirms the title in the first 15 s; clips max ~5 s each; every cost card shows ESTIMATE and source; 8 min+ for mid-rolls; chapters + sources in the description; thumbnail = big object + $ figure + max 3 words, uploaded with vidiq_upload_image and set as thumbnailImageId.
- engine.py shots may now be (file, start, max_seconds): the cut is slow-mo stretched inside the clean window instead of running into a title card.

## Communication rule (26 Nov 2026)
Mohamed chats ONLY in the main control chat. Batch and learning runs must:
- save every draft (postId, revision, per-platform publicationIds, slot time) to tools/scripts/drafts_YYYY-MM-DD.json and commit it before ending;
- write anything he must know or answer to tools/ALERTS.md (dated, newest first).
The main chat's daily 12:15 PM UAE check-in relays the batch to him, collects "approve", publishes, and spreads YouTube uploads 3/day. Batch runs must NOT wait for or expect replies in their own session.
