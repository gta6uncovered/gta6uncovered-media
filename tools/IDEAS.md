# GTA6 Uncovered: ideas backlog (appended by the daily learning task, keep under 150 lines)

## Second channel (proposal due Monday 30 Nov batch)

### Candidate A: Malayalam AI-character story series (Facebook Reels first)
- Examples: @naan_babybro "Greedy brother Part 1" (AI toddlers, Malayalam/Tamil): 452.9K likes, 12.5K comments in 1 day (Mohamed, 24 Nov).
  "Dino Mukk" (Storytellers Union, dir. Gokul Pillai): AI Malayalam short, 2.1M organic Instagram views, 2,500+ AI images,
  7-8 days production (https://animationxpress.com/?p=1625247). Kerala Police AI-crow reels built a 2M Instagram community (Onmanorama, Aug 2026).
- Production (fully automatic): script in Malayalam (Claude) -> character stills (consistent character sheet) -> image-to-video
  -> Malayalam TTS -> ffmpeg captions. Image-to-video prices (Aug-Sep 2026): Pruna P-Video $0.02/s 720p (draft), LTX-2.3 Fast
  $0.06/s 1080p with audio, Wan 3.0 $0.083/s 720p, Kling 3.0 Std $0.084/s, Hailuo 2.3 $0.28 per 6 s
  (https://invideo.io/blog/ai-video-model-pricing, https://aireiter.com/blog/cheapest-image-to-video-api).
  A 30 s episode (6 x 5 s) = ~$1.80 on LTX-2.3 Fast, ~$0.60 draft tier; x1.5 for retries. 1 episode/day = ~$55-80/month.
  No free API tier found; Kling web plan gives 66 free credits/day (manual, not automatic).
- Money from UAE: Facebook Content Monetization (invite-only, performance-based; program grew from <3M to 12M participants,
  https://nextbillion.net/news/creators-are-cashing-in-on-a-facebook-renaissance/). Meta paid ~$3B to creators in 2025, ~60% from Reels.
- Risks: AI labels required; Meta reduces reach for unoriginal/reposted content; Malayalam TTS quality must be checked;
  character consistency across episodes; vendor earnings claims (theprint BrandIt) are sponsored and unverified.
- TODO before 30 Nov: test 2 Malayalam TTS voices; find 3 more Malayalam AI series pages with view counts.

### Candidate B: pure "GTA 6: The Real Cost" channel (English, long-form + Shorts)
- Proof of demand: "Could you afford Vice City as a law-abiding citizen?" (https://www.gameshub.com/news/features/gta-6-vice-city-lifestyle-cost-2872949/),
  "Buying everything Rockstar is selling for GTA 6 costs $1,700" (https://www.gtaboom.com/buying-everything-rockstar-is-selling-for-gta-6-will-cost-you-1700),
  Mark Tilbury "GTA 6 saves you $5,000" went viral (beebom, Insider Gaming).
- Pro: long-form earns watch hours toward the doubled YPP bar; personal-finance angle has far higher RPM than gaming.
- Con: could just be our main channel's long-form slot instead of a new channel (one channel compounds faster). Leaning: B goes INTO the main channel.

## 2026-11-25 ideas
1. Viewer-impact first. Source: our own 010 (1,079 views in 17.5 h, 4x records). Why: it answers "does this affect ME?".
   Automate: topic filter in the batch script; reject any topic with no wallet/console/decision angle. Impact: ~2-4x views/h.
2. Weekly long-form Real Cost (6-8 min) stitched from the week's shorts + 3 new segments. Source: YPP 2027 changes
   (https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/). Why: Shorts views alone
   can't reach 20M/90d; watch hours are the only realistic YPP route. Automate: engine.py "long" mode concatenating scripts at 16:9.
   Impact: starts banking hours; long-form RPM ~10x Shorts.
3. "30 FPS even on PS5 Pro" debate short. Source: https://kotaku.com/some-players-are-crashing-out-about-gta-6-only-being-30-fps-starfield-got-assaulted-for-being-locked-to-30-fps-2000755892
   and TechRadar (Rockstar confirmed 30 fps at launch). Why: a real argument people already have, so the question gets comments.
   Automate: normal pipeline, question "30 locked or 60 blurry?". Impact: first comments.
4. "Visit Vice City" Shorts Effect from YouTube's launch push (https://blog.youtube/news-and-events/youtube-rockstar-games-gta-vi-launch/).
   Why: YouTube is promoting GTAVI content (3.5B views on launch day); effects/features can get feed boosts. Automate: not possible
   via API (in-app only), so low priority unless Mohamed posts one by phone. Impact: unknown, test once.
5. Pinned-comment keyword CTA "Comment COST for Part 2". Source: Ash and Claude reel (2.5K reactions, ~1K comments, Mohamed 24 Nov).
   Automate: voiceover line + on-screen text; Part 2 posts within 24 h. Impact: comments from 0 to measurable.
