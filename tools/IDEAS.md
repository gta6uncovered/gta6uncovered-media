# GTA6 Uncovered: ideas backlog (appended by the daily learning task, keep under 200 lines)

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
- TODO before 30 Nov: find 3 more Malayalam AI series pages with view counts.
- 28 Nov: Malayalam TTS CONFIRMED: Sarvam Bulbul v3 Malayalam page, voices incl. Shubh, Shreya, Manan, Ishita, Manglish
  code-switching, Rs 20 per 10K chars, free trial, no card (https://www.sarvam.ai/apis/text-to-speech/malayalam).
  A 30 s episode (~400 chars) = ~Rs 0.80. TTS cost is negligible; image-to-video (~$55-80/month) is the real cost.
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

## Radar 2026-11-27
- Windsor.ai "Facebook Page Insights" connector (Claude directory, also "Windsor.ai for Social Media").
  Source: https://windsor.ai/connect/facebook-page-insights-mcp/ , https://windsor.ai/pricing/ (updated 22 Nov).
  Real: Forever Free plan = 1 data source, 1 account, 30-day lookback, MCP included; metrics include Reels plays and
  15/30/60 s + 95% watch counts. Since 15 Jun 2026 Meta no longer splits organic/paid reach (totals only). Cost: $0
  (Basic $19-23/mo only if we want TikTok/YT in it too: not needed, vidIQ covers those). Fit: HIGH, it is our only FB stats
  route. Action: Mohamed enables the connector in claude.ai and signs in with the FB account that owns the Page (his yes).
- GTA 6 clipping market snapshot (FindClout, 18 Nov): 12 live campaigns, $45,080 posted budgets, median $1.00/1k views
  (range $0.35-2.00), 3 streamer-clip campaigns, 6 music (need in-app sound = not automatic), budgets median $2,104.
  Caveats: per-post caps, view minimums, budget runs out; realised pay on one marketplace ~$0.66/1k.
  Source: https://findclout.com/gta-6-clipping/pay-rates/ , https://findclout.com/gta-6-clipping/campaigns/ .
  Fit: streamer campaigns only (no sound needed). Action: include in 30 Nov proposal (Candidate C); retry the Content
  Rewards discover page tomorrow (blocked today).
- Social posting connectors (Blotato, Metricool, Windsor Social): listed at https://www.blotato.com/blog/best-claude-connectors-social-media .
  Real but redundant: vidIQ already posts to YT/TikTok/FB. Fit: LOW. No action.
- OpusClip: no new feature found this week beyond the 4.0 release (https://www.opus.pro/blog/opusclip-4-0). Connector + Pro
  $29/mo still the plan for Candidate C.
- YouTube enforcement is channel-level: one pattern across the last ~30 uploads can cut monetisation for all; on-camera
  faces and niche education fared better; AI labels themselves are not penalised (TNW, 15 Jun 2026,
  https://thenextweb.com/news/youtube-ai-slop-crackdown-faceless-creators-collateral-damage). Fit: direct risk to us. Action:
  raise own-analysis share (Real Cost) to >= 1 in 3 uploads; vary the template (see idea 3 below).

## 2026-11-27 ideas
1. Big-number hook rule. Source: our 005 "sold 32.5 MILLION" = 99 views/h, 1,730 in 17 h (best ever) after we had "banned"
   records. Why: a huge concrete number is a 1-second hook. Automate: batch script rejects a title without a number >= 1M or a
   $ figure, unless it is a character twist. Impact: lift median day-1 from ~600 to 1,000+.
2. Real Cost "price tag" Shorts in the 005 shape: one giant $ number first ("$653 BILLION to build Vice City"). Source: 005 +
   Real Cost demand. Why: combines our best hook type with the only content that is safe on FB and protective on YouTube.
   Automate: existing Real Cost scripts, first card = the total. Impact: same views as 005 with policy safety.
3. Template variety to avoid the "mass-produced" pattern: rotate 3 visual formats (trailer B-roll / QS cost-card board /
   map + numbers) and 2 voices. Source: TNW channel-level enforcement. Automate: engine.py STYLE flag. Impact: risk reduction.
4. Clips cash test (Candidate C) as a 2-week paid pilot: OpusClip Pro $29 + 2 new accounts, streamer campaigns only.
   Break-even = ~44k paid views at $0.66/1k. Source: FindClout snapshot above. Needs Mohamed's yes + sign-ups on 30 Nov.
5. Daily FB numbers via Windsor (free) feeding this report, so FB-only decisions stop being guesses. Needs his one-time connect.

## 2026-11-28 — Nightly read-only scan (FB Page + TikTok, Browser 2)
Coverage: FB Reels feed 15 reels; FB video search x5 (GTA 6, GTA 6 tips, AI faceless channel, AI video automation, Claude AI automation);
TikTok For You 14 videos. TikTok search blocked AGAIN by slider CAPTCHA (stopped per rules; not solved). (FB counts read from page text: approx.)
### What's winning
- FB feed: Hawk Creates "I built a secret underground house hidden beneath a mangrove from scratch!" ~2.8M likes / 18K comments.
  Why: "I built X from scratch" + secret/hidden = curiosity + process payoff. GTA angle: "What a secret Vice City hideout would cost to build for real" (Real Cost).
- FB feed: AI-labelled content keeps getting big numbers (Vishal Kumar AI romance ~505K, KArt creator AI bunny ~135K, Komal AI ~60K). AI label still not suppressing reach on FB.
- FB "Smartest Workers" (Anaya) ~67K, "4K Explores" Dubai ~505K: satisfying/visual footage + short caption.
- FB GTA 6 tips search (all < 5 h old): 2RayD "Stop going broke in Leonida — Which tip helped you most?" (warning hook + comment question, same shape as our hook #4);
  "GTA 6 Tips, Clips and More" page "WHO NEEDS A WEAPON WHEN YOU HAVE BEER?!" 86 reactions in 4 h (funny mechanic discovery).
  Heidy "GTA 6 MOBILE IS HERE?! How to download & play on mobile" = SCAM BAIT (no mobile version). Do NOT copy; possible debunk Short: "GTA 6 on mobile? It's a scam — here's why".
- FB GTA 6 search otherwise = tiny (0-14 reactions) fresh clips, incl. AI stickman "GTA 6" animation (madu stikman world). Competition on FB still weak.
- FB AI niche: "Claude AI Se Video Editing? Without CapCut!" (Amin Sati, 2 days, AI-labelled) — Claude-for-video tutorials are starting to appear in Hindi/Urdu.
  "Automate AI videos with Google Flow on mobile using Antigravity (free)" (Epictube Sensei, 1 day). Digital Services Program "Claude, Claude Cowork, Claude Code" 18.4K / 2K shares (Jul) = Claude Cowork tutorials pull shares.
- TikTok FYP: FKLzz "GTA 6 + DLSS 5 + 120 FPS" ~5.4K likes, 905 saves, 2,122 shares (shares > likes/3 = outlier for a small account). GTA 6 has NO PC version yet (PC rumoured Q1 2027),
  so this is a mod/fake/edit — but "GTA 6 PC / max graphics" curiosity is huge. Safe angle: "When is GTA 6 coming to PC? What we know" (cite sources).
- TikTok FYP: zoukayzie "+$9708.5 hrs maybe that's what it cost..." 167.6K likes, 26.6K saves — money-number-first caption again wins (supports the big-number rule).
- TikTok FYP: GOLDMAN e-waste gold recovery 581.9K likes / 68.1K shares — "hidden value in junk" format.
### Hooks to test next batch
1. "GTA 6's first patch just changed the graphics — here's what players noticed" (news + before/after cards; cite Notebookcheck/Reddit)
2. "Stop going broke in Leonida: 3 money mistakes in GTA 6" (warning hook + "which tip helped?" question)
3. "GTA 6 on mobile? Don't download it — it's a scam" (debunk; protective + high search)
4. "GTA 6 on PC with DLSS 5? Here's the truth" (PC release status explainer)
5. "What a secret Vice City hideout would cost in real Miami" (Real Cost, FB-safe, from the 2.8M 'secret house' format)

## Radar 2026-11-28
- Kapwing "7 Best Claude Skills for YouTubers" (18 Nov, free ZIPs): /outliers (uses vidIQ), /youtube-script-researcher,
  /footage-check, /kai-rough-cut, /packaging (25-point title+thumbnail check), /upload-pack (SEO, chapters, SRT, pinned
  comment), /community-post; bonus /make-it-global (translate + dub). Source:
  https://www.kapwing.com/resources/best-claude-skills-for-youtubers/ . Real: yes, SKILL.md files; some need Kapwing or
  vidIQ credits. Cost: $0 to read. Fit: HIGH for /packaging + /upload-pack logic (we can copy the checklists into our own
  pipeline, no credits); /make-it-global = cheap route to Spanish/Portuguese GTA Shorts later. Action: next batch run
  downloads the ZIP into scratch, reads it (third-party code: read only, never run), ports the packaging checklist.
- "AI Producer by OpusClip" connector is in the Claude directory (separate from the OpusClip clips connector): AI editing
  tools build_captions, find_broll, enhance_voice, frame_speaker. Fit: MEDIUM; our engine already does captions/B-roll.
  Only matters for Candidate C. No action until C is approved.
- YouTube Shorts originality (1 Oct 2026, TeamYouTube "Prioritizing original content on Shorts"): re-uploads with nothing
  added get less reach and are excluded from the Shorts Creator Pool; template edits and voice-over describing on-screen
  action are not "original" (https://ppc.land/re-uploaded-shorts-lose-reach-as-youtube-favours-original-clips/). Fit:
  direct risk to our trailer-narration Shorts. Action: own-analysis share to >= 1 in 2 by 10 Dec (see ALERTS).
- Free stats route: YouTube Data API v3 = 10,000 quota units/day free, videos.list costs 1 unit
  (https://developers.google.com/youtube/v3/determine_quota_cost). One API key (Mohamed, Google Cloud console, 5 min)
  replaces all paid vidIQ stats calls. Windsor.ai free plan still the FB route (directory: "Windsor.ai for Social Media").
- Content Rewards discover page: blocked again (2nd day). OpusClip's own article (updated 22 Nov): payouts only after review
  (~72 h) and a minimum view threshold, bot score on every submission, payout trouble in non-Stripe countries
  (https://www.opus.pro/blog/content-rewards). UAE is a Stripe country, so payout should work; verify in Whop settings.
- No new Facebook monetization changes found this week; YPP 2027 doubling (1 Feb) unchanged.

## 2026-11-28 ideas
1. Pre-draft checklist in RUNBOOK (length <= 18 s, strongest video at Slot B, title has number/$/twist, own-analysis
   flag). Source: 012/013 shipped at 21 s and RC at Slot C despite written lessons. Automate: engine.py prints PASS/FAIL;
   batch refuses to draft a FAIL. Impact: stops repeating known mistakes.
2. "Add-value" Short format for news: every news Short gets one own-made comparison card (e.g. "30 FPS = 33 ms per frame vs
   17 ms at 60", or a cost-per-hour sum) so the video is analysis, not narration. Source: YT 1 Oct originality
   rule. Automate: CARDS template "OUR MATH". Impact: protects Shorts reach and the channel's YPP review.
3. Price/wallet series in the 011 shape: "GTA 6 costs you $X per hour played", "Ultimate Edition: $20 for what?",
   "Series S owners: the $X upgrade question". Source: 011 = 57/h, 012 = 30/h + best engagement. Impact: our best
   repeatable hook family; FB-safe when it is our own math.
4. Free stats pipeline: a 30-line script calling YouTube Data API videos.list for all our IDs, run by every learning task
   at 0 credits. Needs the API key. Impact: saves ~150 credits/month for discovery calls.
5. Spanish GTA Shorts (second-language test) with the same engine: Kokoro has Spanish voices; GTA audience in LatAm/Spain
   is large and competition lower. Source: Kapwing /make-it-global idea. Automate: translate LINES, ef_dora/em_alex voice.
   Impact: a second, cheap reach channel; propose after the 30 Nov decision.


## Calendar
- 1B Followers Summit AI Film Award: SKIPPED 2026 (Mohamed, 29 Nov). Next edition likely opens ~late Sep 2027: start story in Oct 2027. Rules 2027 ed.: 5-7 min, 70% Dreamina Seedance, 16:9 1080p, EN subs, 5 themes.
