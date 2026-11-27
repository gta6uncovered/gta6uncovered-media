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
- 26 Nov: TTS cost: Sarvam Bulbul v4 Flash INR 2 per 1,000 chars (v3 INR 3), INR 100 free credits on signup
  (https://docs.sarvam.ai/api-reference-docs/getting-started/pricing). A 30 s Malayalam script (~400 chars) = ~INR 0.80. Malayalam
  support not stated on the pricing page: confirm on the Bulbul model page before proposing. Kokoro has no Malayalam.
- 26 Nov: PRO for A: Meta's originality rule (Mar 2026) rewards fully original content; an AI story series we write ourselves is
  100% original, unlike trailer-based GTA clips. Market signal: ManoramaMAX launched "Khushi", a 100-min Malayalam AI-animated
  kids' film, 14 Nov 2026 (https://www.onmanorama.com/entertainment/entertainment-news/2026/11/18/manoramamax-launches-khushi-jungle-adventure.html).
- 26 Nov: Creator Fast Track (Meta) pays $1,000/month guaranteed for 3 months to creators with 100k+ followers on TikTok/YT/IG
  (https://about.fb.com/news/2026/03/creator-fast-track-grow-your-audience-earn-money-on-facebook/). Not reachable now; it is a
  milestone to aim at: 100k TikTok followers unlocks FB money without waiting for an invite.

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

## 2026-11-26 ideas
1. "Who they were before GTA 6" series (Jason soldier, Lucia, Cal, Boobie, Brian, Real Dimez...). Source: our 008 = 1,305 views in
   17 h, 1.3% engagement, first comment. Why: single-person twist in 5 words. Automate: facts only from Rockstar's official
   character pages; one script template, Part N in title. YouTube + TikTok only (not FB: narration = "unoriginal" on Meta). Impact: 2x median views/h.
2. FB Page = Real Cost only. Source: https://about.fb.com/news/2026/03/rewarding-original-creators/ (narrating on-screen footage
   is demoted; added analysis is rewarded; primarily-unoriginal Pages can be demonetised). Automate: batch script adds FB destination
   only when topic tag == real-cost. Impact: protects the only platform likely to pay us in 2027.
3. TikTok 18 s cap. Source: our data (4/4 TikToks at 21 s+ = 0 views; 5/5 at 16-18 s got 151-621). Automate: engine.py warns
   when the TikTok render exceeds 18 s; trim the outro card for TikTok. Impact: stops wasting 1 in 3 TikTok posts, if confirmed by 012/017.
4. Title hashtag diet. Source: Metricool, 799,718 videos (https://metricool.com/youtube-trends/): Shorts with hashtags ~10% fewer
   views, ~9% more engagement. Automate: title without "#gta6 #shorts", 3 tags in description. Impact: small, cheap A/B.
5. Strongest video at Slot B (01:00 UTC = 8 PM ET). Source: 010 and 008, our two best, both at Slot B. Automate: batch planner
   sorts each day's 3 videos by predicted strength and puts #1 at 01:00 UTC. Impact: +20-50% on the lead video (hypothesis).

## From Mohamed's reels, 26 Nov 2026
### Second-channel candidate C: GTA 6 stream-clips page for paid clipping campaigns (strong)
- Reel (Faceless Launchpad): OpusClip now plugs into Claude, so you can paste a GTA 6 launch-stream link, get ranked vertical clips with captions and titles, and queue them. It claims a clips channel got 1.6M views on one clip in its first day (unverified).
- Why it fits: this unblocks the BIG Content Rewards pools we skipped on 23 Nov because we couldn't download Twitch: Reach GTA 6 $20K pool, Kai Cenat $10K pool, Lacy $12.5K, Lauren Hamden $1.50/1K, AsianJeff. Those pay ~$1-2 per 1K views with no follower minimum and no in-app sound, so it is fully automatic, and it pays UAE creators (unlike TikTok).
- Tool: the OpusClip connector exists in the Claude directory (not installed). Twitch import needs OpusClip Pro at $29/month (300 source minutes, about 5 h of stream); Starter at $15 covers YouTube links only.
- Must run on SEPARATE new clip accounts (TikTok + YouTube Shorts; Facebook Page optional). Never put stream clips on GTA6 Uncovered, or the reused-content risk kills its monetization. Account sign-ups are Mohamed's.
- Math: 1M clip views/month at about $1/1K = about $1,000. Campaign budgets cap and move fast, so check live budgets before each batch.
### Research method upgrade (Scott Smith reel, 804 reactions)
- Find ANOMALIES: channels under 100K subs with videos at 1M+ views in the last 60 days. That proves the topic and packaging, not channel size.
- Dissect their top 10 recent videos: core topic, title template, emotional trigger. Then generate our titles on the same proven template (never copy content).
- Apply in the daily hunt (vidiq_outliers on Sundays; vidiq_youtube_search + views/subs ratio on other days).

## 2026-11-26 — Feed warm-up scan (FB Page, AI/faceless searches)
- Searched as the Page: AI faceless channel, Claude AI automation, OpusClip AI clips, AI video generator faceless income, GTA 6 viral.
- Pattern: "income math" hooks ($500 x 7 = $3,500 / x30 = $15,000) on clipping reels (Rashmi Kumari, OpusClip + YT clips). Money-math overlay = strong hook; test "GTA 6 costs you $X/hour" style math.
- Mr Secret "Bulk AI video generator / consistent characters" (OmniFlash): 413 likes / 848 comments → comment-for-link bait drives comments 2x likes. Test a "comment GTA for the full list" CTA on FB (no external link promises).
- GTA 6 viral reels: price ($80) / "buying GTA 6" reactions and GTA-V "clipping moment" pages are posting daily. Price/affordability debate = our winning "viewer-impact" angle.
- Next nightly automated scan: trig_01X7UqiqTxFp5ENd6FDpcZA9 (21:41 UAE, read-only, his Chrome).

## 2026-11-26 — TikTok warm-up scan (logged in on Chrome "Browser 2")
- Searched: AI faceless channel, AI video automation, Claude AI, GTA 6.
- GTA 6 top videos right now (1 day old) are in-game gameplay tricks/strats: "infinite food strat" 377.8K likes, stunts 164.7K, "biggest bank robbery 130K" 64.7K, "Ultimate Edition worth the wait" 93K. Post-launch (19 Nov) demand has moved to "how to / strat / money" tips.
- Action: test text-card "GTA 6 money/strat" Shorts built from published guides (with a cited source, no reused gameplay footage). Gameplay footage would need our own capture (we have no console), so keep away from reused-content risk.
- AI niche: "Comment 'edit' to get…" CTA (Kevin Dang 18.6K) again confirms comment-bait CTAs.

## 2026-11-27 — Nightly read-only scan (FB Page + TikTok, Browser 2)
Coverage: FB Reels feed ~12 reels; FB video search x5 (GTA 6, GTA 6 tips, AI faceless channel, AI video automation, Claude AI automation);
TikTok For You ~14 videos. TikTok search was blocked by a slider CAPTCHA (stopped per rules; not solved).
### What's winning
- FB "how machines work" AI explainer: "How Do ATMs Know What to Do?" (Ideas on 5 mi..., AI-labelled) = 2.9M likes, 172K shares.
  Why: curiosity question + see-inside visual, zero face. Test: "How GTA 6 knows where you are / how the police AI decides" text-card explainer (cite Rockstar/press, no gameplay reuse).
- FB AI-generated story reels dominate the feed: Milo & Chikoo animal story 2.4M likes; AI baby 1.2M; AI Cinemas 49.5K. AI-labelled content is NOT being suppressed on FB if it is original.
- FB "GTA 6 Daily" (1 h old): "6 RARE GTA 6 cars you can steal for FREE — which one are you grabbing first?" Listicle + free + question CTA. Copy the template (number + rare + free + choose-one question).
- FB GTA 6 video search = mostly fresh GTA V clips mislabelled #GTA6 with 1-10 reactions. Low competition on real post-launch tips on FB.
- TikTok FYP: GTAWorld "Time for GTA 6" skyline 15.3K likes; TAMRIX "GTA 6 vs GTA 5 — the graphics upgrade is unreal" 24.6K saves/likes. Side-by-side "vs" comparison remains a reliable GTA hook.
- FB AI niche searches: old or low-engagement (2-14 reactions); "AI Faceless Channel Blueprint 2026" (Money Printer PRO). Nothing new on Claude.
### Hooks to test next batch
1. "6 rare GTA 6 cars you can get for FREE — which one first?" (listicle, comment question)
2. "How does GTA 6's police AI actually find you?" (how-it-works explainer)
3. "GTA 6 vs GTA 5: the one upgrade nobody noticed" (vs format)
4. "Stop doing this in GTA 6 — it's costing you money" (money tip, warning hook)
5. "Real Cost: what Lucia's Vice City apartment costs in real Miami" (FB-safe own analysis)
