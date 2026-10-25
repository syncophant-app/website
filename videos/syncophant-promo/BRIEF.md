---
workflow: product-launch-video
flow: automation
storyboard: yes
message: "Out of space on your Mac? Don't buy a new Mac or another subscription. Plug in storage you own, and it feels like a new drive."
destination: social-feed
aspect: 1080x1080
language: en
audience: Mac users running out of disk space who hate subscriptions
length: 34s
angle: comedic-problem-hack
narration: no
---

## Intent

A small, fast social promo for Syncophant (syncophant.app). Hook in the user's words: "Here's a hack for your Mac that you want to keep track". Pitch: running out of storage on your Mac? A new Mac is expensive, especially with the RAMpocalypse (RAM prices keep climbing). Cloud storage charges a hefty sum for a TB, and it's yet another subscription. Syncophant lets you bring your own storage: connect it and it looks like you just got a new hard drive. "The Dropbox of 2026", but your data is yours and no one else sees it.

Kicker: don't have storage? Hetzner Storage Boxes cost 3.81 EUR (4.27 USD, 403.66 INR) per month for 1 TB, and Syncophant sets up the Hetzner connection in one step.

Close: free, open source, no paywalls, no tracking, no account needed to start syncing. syncophant.app

Tone: comedic, relatable, high-octane. Typography heavy. The user's script is a rough idea; restructure freely. Design visual elements from scratch so they match the brand.

## Assets

- src/data/brand.ts (website repo) — the mark and lockup SVG paths. Copy verbatim, never redraw. The mark is an elephant head whose ear gaps form one clockwise sync loop (up arrow left, down arrow right). Animate the logo.
- public/fonts/Onest-Variable.woff2 (website repo) — "Onest Variable", the only typeface. Variable weight 100–900.

## Customizations

- Music and SFX: v2 synthesizes both locally with audio-src/synth.py (numpy/scipy, no samples, no external service). 150 BPM, drop at 14.4 s, final hit at 30.4 s. v1 used an ElevenLabs track.
- v2: show what Syncophant does — a Finder window where the storage mounts in Locations right under Macintosh HD, like another drive.
- v2: the logo animates its own geometry (solid elephant, then ear gaps cut open in arrow direction, then wordmark letters rise). No external flashes or light trails.
- Super fast motion graphics, kinetic typography.
- Logo animation: the sync-loop arrows in the ear gaps are the hero motion.

## Notes

- Brand colours: ink #0a0a0a, paper #ffffff, mist #eef1f6, ink-muted #5a6372, line #d5dbe4. Syncophant Blue #4DA3FF to #0A5FDB (app icon gradient).
- Claims must stay true: works with SFTP, WebDAV, S3-compatible and SMB; Hetzner gets a guided setup; free, GPL; no account, no telemetry; macOS 26 or later.
- No narration. No captions needed; the typography carries the copy.

## 2026-10-25 — v3 brief (replaces the v1/v2 creative direction)

The user scrapped the earlier storyboard. Same project, same format (1080×1080), same workflow.

- message: "Syncophant puts storage you own in Finder, like another drive."
- tone: modern, minimal, solution-oriented. No humour, no buzzwords. Show the value of the product plainly.
- length: ~30s
- product UI: rebuilt in HTML from the website's Finder component (user's choice). The site README notes these drawings should become real screenshots before launch.
- music: HyperFrames BGM from the HeyGen music library (no synth). Calm and inspirational.
- sfx: allowed, sparingly, only to accompany motion. Use the bundled HyperFrames SFX.
- look: the website's monochrome system (ink, paper, mist, ink-muted, line) on a soft light field. Blue only where the brand uses it. Onest Variable for all type, sentence case.
