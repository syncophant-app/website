---
format: 1080x1080
duration: 33.6s
message: "Out of space on your Mac? Don't buy a new Mac or another subscription. Plug in storage you own, and it feels like a new drive."
arc: PAS — hook → pain → agitation (new Mac) → agitation (subscription) → product intro → solution → secret deal → CTA
audience: Mac users running out of disk space who hate subscriptions
mode: collaborative
music: none
music_file: assets/music.wav (synthesized by audio-src/synth.py, 150 BPM, drop at 14.4s, final hit 30.4s)
music_host: "generated, high-octane driving electronic, ~150 BPM, hard kick, sidechained bass, riser into a drop at the product reveal (~14s), clean button ending at 30s"
---

# Syncophant — "A Mac hack you'll want to save"

No narration. Type is the voice: every line lands on a beat of the music. Two registers from `frame.md`: ink black for the problem, Syncophant Blue for the answer. Onest Variable only, weight swings (100 → 900) used as motion.

## Frame 1 — The hack

- scene: Words slam in per beat; bookmark drops on save.
- duration: 3.2s
- transition_in: cut
- status: animated
- src: compositions/frames/01-hack.html

## Frame 2 — Disk almost full

- scene: Bar fills to 99.8%, alert bonk, dog photos vs thesis.
- duration: 4.8s
- transition_in: cut
- status: animated
- src: compositions/frames/02-disk-full.html

## Frame 3 — Buy a new Mac?

- scene: RAM price line rockets out; RAMPOCALYPSE weight 100 to 900.
- duration: 3.2s
- transition_in: cut
- status: animated
- src: compositions/frames/03-new-mac.html

## Frame 4 — Another subscription?

- scene: Cards deal in, counter to #14, forever.
- duration: 3.2s
- transition_in: cut
- status: animated
- src: compositions/frames/04-subscription.html

## Frame 5 — Enter Syncophant

- scene: On the drop: the elephant pops in solid, the left gap cuts open upward, the right gap downward, letters rise.
- duration: 3.2s
- transition_in: cut
- status: animated
- src: compositions/frames/05-logo.html

## Frame 6 — Just another drive

- scene: Finder: Storage Box mounts under Macintosh HD with an eject button, click it, files with real statuses, the thesis uploads and verifies.
- duration: 4.8s
- transition_in: cut
- status: animated
- src: compositions/frames/06-finder.html

## Frame 7 — Except it's yours

- scene: The dropbox of 2026, except it's yours. Lock clicks, no one else sees it.
- duration: 3.2s
- transition_in: cut
- status: animated
- src: compositions/frames/07-private.html

## Frame 8 — The secret deal

- scene: Paper register. 1 TB, price flips on the snare roll, cha-ching on €3.81.
- duration: 3.2s
- transition_in: cut
- status: animated
- src: compositions/frames/08-deal.html

## Frame 9 — Free. Seriously.

- scene: Stamps on eighths, lockup builds itself on the final hit, syncophant.app types out.
- duration: 4.8s
- transition_in: cut
- status: animated
- src: compositions/frames/09-cta.html

---

# 2026-10-25 — v3 storyboard (proposal)

- format: 1080x1080
- duration: ~31.5s
- message: "Syncophant puts storage you own in Finder, like another drive."
- arc: Problem → answer → it's a drive in Finder → space → verified → private → price → end card
- mode: collaborative
- music: calm, inspirational, piano with soft pads, ~80–90 BPM (HeyGen library). Cuts land on phrase starts, not every beat.
- look: light field (paper and mist, soft white glows), ink type, Onest 400–650, sentence case. One Finder window carries frames 3–5 as one continuous world.
- motion: slow and precise. Fade and rise 24px over 0.6–0.8s, ease-out. No shakes, no slams, no blur punches.

### Frame 1 — Running out of space (0–3s)
- scene: A single Macintosh HD storage bar fills to 96%. Headline: "Running out of space on your Mac?"
- sfx: none

### Frame 2 — Storage you own (3–7s)
- scene: The mark builds itself (solid elephant, then the ear gaps open in their arrow directions), slow and quiet. Headline: "Add storage you own." Line under it: "Syncophant puts it in Finder."
- sfx: one soft cinematic whoosh as the mark forms

### Frame 3 — Next to Macintosh HD (7–12s)
- scene: A Finder window settles in. In Locations, "Storage Box" appears under Macintosh HD with an eject button. Caption: "It shows up in Finder, like another drive." Small line: "SFTP, WebDAV, S3-compatible storage or SMB."
- sfx: soft click when the drive is selected

### Frame 4 — Space on your Mac (12–16.5s)
- scene: Same window. The drive's files list in, each with its real status ("On your box", "Kept on this Mac"). Caption: "Your files stay on your storage." Small line: "Only the files you open take up space on your Mac."
- sfx: none

### Frame 5 — Verified (16.5–20.5s)
- scene: Same window, one row in focus: "Kitchen renovation.mov" goes Uploading → Verifying on your box → On your box · verified. Caption: "Every upload is verified."
- sfx: one quiet chime on "verified"

### Frame 6 — Private (20.5–24s)
- scene: The window recedes. Type only: "No account. No Syncophant server." Small line: "Your Mac connects straight to your storage. Passwords stay in your Keychain."
- sfx: none

### Frame 7 — Need storage? (24–27.5s)
- scene: "Need storage?" then a clean price block: "1 TB Hetzner Storage Box" / "€3.81 a month" / "Set up in one step in Syncophant."
- sfx: none

### Frame 8 — End card (27.5–31.5s)
- scene: The lockup builds itself as in frame 2. Under it: "Free and open source." and "syncophant.app". Holds while the music resolves.
- sfx: none

#### v3 music update (2026-10-25)
- music: HeyGen library 93f61e54 (warm piano, G major, ~99.7 BPM, builds), the user's pick over 7d074d66 (D minor, too sad) and two others. Cut from 7.555s, 32s, fade-out at the end: assets/music-v3.mp3.
- cuts on its bar grid (bar = 2.405s): 0, 4.795, 9.605, 19.195, 22.795, 26.395 → end 32.0. Finder caption swaps at +3.608 and +6.013; "verified" at +7.817.
