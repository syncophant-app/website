"""Synthesize the Syncophant promo soundtrack and sound effects from scratch.

No samples, no external services: every sound is built from oscillators and
seeded noise with numpy/scipy, so the output is reproducible.

    python synth.py            # writes ../assets/music.wav and ../assets/sfx/*.wav

Arrangement (150 BPM, 1 beat = 0.4 s, 1 bar = 1.6 s), matched to the cut list:
  bars 0-7    problem section (A minor), driving, a little dark
  bar  8      build: snare roll + noise riser, drums drop out on the last beat
  bars 9-17   drop at 14.4 s (C major lift), bigger bass, supersaw offbeat chords
  bar  18     stamps bar, then the final hit at 30.4 s and a ring-out to 33.6 s
"""

import os

import numpy as np
from scipy.signal import butter, fftconvolve, sosfilt
from scipy.io import wavfile

SR = 44100
BPM = 150
BEAT = 60 / BPM
BAR = 4 * BEAT
TOTAL = 33.6
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")

rng = np.random.RandomState(7)


# ---------- building blocks ----------

def t_axis(dur):
    return np.arange(int(dur * SR)) / SR


def noise(dur):
    return rng.uniform(-1, 1, int(dur * SR))


def env(dur, attack=0.002, decay=0.2, curve=1.0):
    t = t_axis(dur)
    a = np.clip(t / max(attack, 1e-4), 0, 1)
    return a * np.exp(-t / decay) ** curve


def filt(x, kind, freq, order=2):
    sos = butter(order, freq, btype=kind, fs=SR, output="sos")
    return sosfilt(sos, x)


def saw(freq, dur, detune=0.0):
    t = t_axis(dur)
    ph = (freq * (1 + detune)) * t
    return 2 * (ph - np.floor(ph + 0.5))


def sine_sweep(f0, f1, dur, k=30.0):
    t = t_axis(dur)
    f = f1 + (f0 - f1) * np.exp(-t * k)
    return np.sin(2 * np.pi * np.cumsum(f) / SR)


def reverb(x, length=1.6, decay=0.45, mix=0.3):
    ir_t = t_axis(length)
    ir = rng.uniform(-1, 1, len(ir_t)) * np.exp(-ir_t / decay)
    ir = filt(ir, "lowpass", 6000)
    wet = fftconvolve(x, ir)[: len(x)]
    wet /= np.max(np.abs(wet)) + 1e-9
    return x * (1 - mix) + wet * mix * np.max(np.abs(x))


def place(track, clip, at, gain=1.0):
    i = int(round(at * SR))
    if i >= len(track):
        return
    n = min(len(clip), len(track) - i)
    track[i : i + n] += clip[:n] * gain


def mtof(m):
    return 440.0 * 2 ** ((m - 69) / 12)


# ---------- drums ----------

def kick(big=False):
    d = 0.7 if big else 0.42
    body = sine_sweep(170 if big else 150, 44, d, k=28) * env(d, 0.001, 0.32 if big else 0.18)
    click = filt(noise(0.012), "highpass", 2500) * env(0.012, 0.0005, 0.004)
    body[: len(click)] += 0.35 * click
    return np.tanh(2.2 * body)


def clap():
    d = 0.32
    n = filt(noise(d), "bandpass", [900, 3500])
    e = np.zeros(int(d * SR))
    for off in (0.0, 0.011, 0.022):
        i = int(off * SR)
        seg = env(d - off, 0.0005, 0.012 if off < 0.02 else 0.09)
        e[i : i + len(seg)] = np.maximum(e[i : i + len(seg)], seg)
    return n * e


def snare():
    d = 0.2
    tone = np.sin(2 * np.pi * 190 * t_axis(d)) * env(d, 0.001, 0.05)
    n = filt(noise(d), "highpass", 1200) * env(d, 0.001, 0.07)
    return 0.6 * tone + n


def hat(open_=False):
    d = 0.25 if open_ else 0.05
    return filt(noise(d), "highpass", 7000) * env(d, 0.0005, 0.08 if open_ else 0.012)


def crash(d=2.2):
    n = filt(noise(d), "highpass", 4000)
    return n * env(d, 0.001, 0.7)


# ---------- tonal parts ----------

def pluck_chord(notes, dur=0.16, bright=3200, voices=3):
    out = np.zeros(int(dur * SR))
    for m in notes:
        for v in range(voices):
            out += saw(mtof(m), dur, detune=(v - 1) * 0.006)
    out = filt(out, "lowpass", bright)
    return out * env(dur, 0.002, dur * 0.35) / (len(notes) * voices)


def supersaw_chord(notes, dur=0.18):
    out = np.zeros(int(dur * SR))
    for m in notes:
        for v in range(7):
            out += saw(mtof(m), dur, detune=(v - 3) * 0.0045)
    out = filt(out, "lowpass", 5200)
    return out * env(dur, 0.004, dur * 0.5) / (len(notes) * 7)


def bass_note(m, dur, cutoff=900):
    x = saw(mtof(m), dur) + 0.5 * np.sign(np.sin(2 * np.pi * mtof(m) / 2 * t_axis(dur)))
    x = filt(x, "lowpass", cutoff)
    return np.tanh(1.6 * x) * env(dur, 0.003, dur * 0.8)


def sub_note(m, dur):
    return np.sin(2 * np.pi * mtof(m) * t_axis(dur)) * env(dur, 0.004, dur * 0.9)


def lead_note(m, dur):
    x = saw(mtof(m), dur, 0.003) + saw(mtof(m), dur, -0.003)
    x = filt(x, "lowpass", 4200)
    return x * env(dur, 0.002, dur * 0.4) * 0.5


# ---------- the song ----------

def song():
    n = int(TOTAL * SR)
    drums = np.zeros(n)
    music = np.zeros(n)
    bass = np.zeros(n)
    fx = np.zeros(n)

    # Chords per bar (MIDI). Problem: Am F C G Am F C E. Drop: C G Am F C G Am F G.
    A_MIN = [57, 60, 64]
    F_MAJ = [53, 57, 60]
    C_MAJ = [55, 60, 64]
    G_MAJ = [55, 59, 62]
    E_MAJ = [56, 59, 64]
    problem = [A_MIN, F_MAJ, C_MAJ, G_MAJ, A_MIN, F_MAJ, C_MAJ, G_MAJ, E_MAJ]
    roots_p = [45, 41, 48, 43, 45, 41, 48, 43, 40]
    drop = [C_MAJ, G_MAJ, A_MIN, F_MAJ, C_MAJ, G_MAJ, A_MIN, F_MAJ, G_MAJ]
    roots_d = [48, 43, 45, 41, 48, 43, 45, 41, 43]

    kicks = []
    # Problem section: bars 0-7 full groove, bar 8 is the build.
    for bar in range(9):
        b0 = bar * BAR
        build = bar == 8
        for beat in range(4):
            t = b0 + beat * BEAT
            if not (build and beat == 3):
                place(drums, kick(), t, 0.95)
                kicks.append(t)
            if beat in (1, 3) and not build:
                place(drums, clap(), t, 0.55)
            for s in range(4):
                if not build:
                    place(drums, hat(), t + s * BEAT / 4, 0.16 if s == 2 else 0.08)
        chord = problem[bar]
        # Syncopated 16th plucks.
        if not build:
            for s in (0, 3, 6, 10, 12, 14):
                place(music, pluck_chord([m + 12 for m in chord]), b0 + s * BEAT / 4, 0.55)
        # Offbeat bass.
        for e in range(8):
            if e % 2 == 1 and not (build and e > 5):
                place(bass, bass_note(roots_p[bar], BEAT / 2 * 0.9, 700), b0 + e * BEAT / 2, 0.7)

    # Build (bar 8, 12.8-14.4 s): snare roll accelerating + noise riser.
    b8 = 8 * BAR
    roll = [(i * BEAT / 2) for i in range(4)] + [2 * BEAT + i * BEAT / 4 for i in range(4)] + [3 * BEAT + i * BEAT / 8 for i in range(8)]
    for k, t in enumerate(roll):
        place(drums, snare(), b8 + t, 0.25 + 0.45 * k / len(roll))
    rd = BAR
    riser = noise(rd)
    tt = t_axis(rd)
    # Rising band-pass sweep built from overlapping blocks.
    rs = np.zeros_like(riser)
    blocks = 16
    for i in range(blocks):
        lo = 400 * 2 ** (i * 4 / blocks)
        seg = slice(int(i * len(riser) / blocks), int((i + 1) * len(riser) / blocks))
        rs[seg] = filt(riser, "bandpass", [lo, min(lo * 2.5, 18000)])[seg]
    place(fx, rs * (tt / rd) ** 2, b8, 0.5)

    # Drop: bars 9-17 (14.4-28.8 s).
    for i in range(9):
        bar = 9 + i
        b0 = bar * BAR
        for beat in range(4):
            t = b0 + beat * BEAT
            place(drums, kick(big=(i == 0 and beat == 0)), t, 1.0)
            kicks.append(t)
            if beat in (1, 3):
                place(drums, clap(), t, 0.7)
            place(drums, hat(open_=True), t + BEAT / 2, 0.14)
            for s in range(4):
                place(drums, hat(), t + s * BEAT / 4, 0.1 if s % 2 else 0.05)
        if i == 0:
            place(drums, crash(), b0, 0.5)
        chord = drop[i]
        for e in range(8):
            if e % 2 == 1:
                place(music, supersaw_chord([m + 12 for m in chord] + [chord[0] + 24]), b0 + e * BEAT / 2, 0.55)
        # 16th bass + sub.
        for s in range(16):
            if s % 4 != 0:
                place(bass, bass_note(roots_d[i], BEAT / 4 * 0.85, 1300), b0 + s * BEAT / 4, 0.55)
        place(bass, sub_note(roots_d[i] - 12, BAR), b0, 0.5)
        # Arp lead: chord tones up two octaves, 16ths.
        arp = [chord[0] + 24, chord[1] + 24, chord[2] + 24, chord[1] + 24]
        for s in range(16):
            place(music, lead_note(arp[s % 4], BEAT / 4 * 0.9), b0 + s * BEAT / 4, 0.22)
        # Bar 16 has a snare roll into bar 17 (the price flip in the deal frame, 26.8-27.2 s).
        if bar == 16:
            for k in range(8):
                place(drums, snare(), b0 + 3 * BEAT + k * BEAT / 8, 0.3 + 0.05 * k)

    # Bar 18 (28.8-30.4): stamps bar, 8th-note kicks on the last beat.
    b18 = 18 * BAR
    for beat in range(4):
        t = b18 + beat * BEAT
        place(drums, kick(), t, 1.0)
        kicks.append(t)
        place(drums, clap(), t, 0.5 if beat % 2 else 0.0)
        for s in range(4):
            place(drums, hat(), t + s * BEAT / 4, 0.12)
    for e in range(8):
        if e % 2 == 1:
            place(music, supersaw_chord([m + 12 for m in G_MAJ] + [79]), b18 + e * BEAT / 2, 0.75)
    for k in range(4):
        place(drums, snare(), b18 + 3 * BEAT + k * BEAT / 4, 0.4 + 0.1 * k)

    # Final hit at 30.4 s: big kick, crash, held C major chord, sub boom, long ring-out.
    hit = 19 * BAR
    place(drums, kick(big=True), hit, 1.1)
    kicks.append(hit)
    place(drums, crash(3.2), hit, 0.7)
    ring = TOTAL - hit
    chord_ring = np.zeros(int(ring * SR))
    for m in [48, 55, 60, 64, 67, 72]:
        for v in range(5):
            chord_ring += saw(mtof(m), ring, (v - 2) * 0.004)
    chord_ring = filt(chord_ring, "lowpass", 3800) * env(ring, 0.003, 0.9) / 30
    place(music, chord_ring, hit, 1.0)
    place(bass, sub_note(36, ring) * env(ring, 0.003, 0.8), hit, 0.9)

    # Sidechain pump on music and bass.
    duck = np.ones(n)
    tk = t_axis(0.3)
    shape = 1 - 0.75 * np.exp(-tk / 0.07)
    for k in kicks:
        i = int(k * SR)
        m = min(len(shape), n - i)
        duck[i : i + m] = np.minimum(duck[i : i + m], shape[:m])
    music = reverb(music, 1.4, 0.35, 0.25) * duck
    bass = bass * duck
    drums = drums + 0.25 * reverb(filt(drums, "highpass", 800), 1.2, 0.3, 1.0)

    mix = 0.9 * drums + 0.8 * music + 0.75 * bass + 0.6 * fx
    mix = filt(mix, "highpass", 28)
    # Glue + limit.
    mix = mix / (np.percentile(np.abs(mix), 99.5) + 1e-9) * 0.8
    mix = np.tanh(1.1 * mix) / np.tanh(1.1)
    # Fade the last 0.3 s to silence.
    fade = int(0.3 * SR)
    mix[-fade:] *= np.linspace(1, 0, fade)
    return mix


# ---------- sound effects ----------

def sfx_whoosh(up=True, d=0.35):
    x = noise(d)
    out = np.zeros_like(x)
    blocks = 12
    for i in range(blocks):
        f = 600 * 2 ** ((i if up else blocks - i) * 4 / blocks)
        seg = slice(int(i * len(x) / blocks), int((i + 1) * len(x) / blocks))
        out[seg] = filt(x, "bandpass", [f, min(f * 2, 18000)])[seg]
    tt = t_axis(d)
    shape = np.sin(np.pi * tt / d) ** 2
    return out * shape


def sfx_impact():
    d = 0.9
    boom = sine_sweep(110, 38, d, 12) * env(d, 0.001, 0.35)
    crack = filt(noise(0.08), "bandpass", [1500, 6000]) * env(0.08, 0.0005, 0.02)
    out = np.zeros(int(d * SR))
    out += np.tanh(2.5 * boom)
    out[: len(crack)] += 0.6 * crack
    return reverb(out, 1.0, 0.3, 0.2)


def sfx_pop():
    d = 0.14
    return sine_sweep(1400, 420, d, 40) * env(d, 0.001, 0.04)


def sfx_click():
    d = 0.03
    x = filt(noise(d), "bandpass", [2000, 6000]) * env(d, 0.0003, 0.005)
    return x + 0.5 * np.sin(2 * np.pi * 1800 * t_axis(d))[: len(x)] * env(d, 0.0003, 0.004)[: len(x)]


def sfx_bonk():
    # A cartoon "nope" alert: two descending square-ish tones.
    out = np.zeros(int(0.5 * SR))
    for k, (f, at) in enumerate(((520, 0.0), (390, 0.14))):
        d = 0.3
        tone = np.tanh(3 * np.sin(2 * np.pi * f * t_axis(d))) * env(d, 0.002, 0.09)
        place(out, filt(tone, "lowpass", 2400), at, 0.6)
    return out


def sfx_drip():
    d = 0.18
    return sine_sweep(600, 1900, d, -14) * env(d, 0.002, 0.05) * 0.8


def sfx_zip(up=True):
    d = 0.32
    t = t_axis(d)
    f0, f1 = (300, 2200) if up else (2200, 300)
    f = f0 * (f1 / f0) ** (t / d)
    x = np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR))
    x = filt(x, "lowpass", 5000) * np.sin(np.pi * t / d) * 0.35
    return x


def sfx_swish():
    return sfx_whoosh(True, 0.22) * 0.9


def sfx_chime():
    # Two-note mount chime (a fifth), soft bell partials.
    out = np.zeros(int(0.9 * SR))
    for f, at in ((880, 0.0), (1318.5, 0.09)):
        d = 0.8
        tt = t_axis(d)
        bell = (np.sin(2 * np.pi * f * tt) + 0.4 * np.sin(2 * np.pi * f * 2.76 * tt) * np.exp(-tt / 0.08)) * env(d, 0.002, 0.25)
        place(out, bell, at, 0.45)
    return reverb(out, 1.2, 0.35, 0.3)


def sfx_ding():
    d = 0.7
    tt = t_axis(d)
    f = 1567.98
    bell = (np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(2 * np.pi * f * 2.0 * tt)) * env(d, 0.002, 0.22)
    return reverb(bell * 0.5, 1.0, 0.3, 0.25)


def sfx_lock():
    out = np.zeros(int(0.2 * SR))
    place(out, sfx_click(), 0.0, 1.0)
    place(out, filt(noise(0.05), "bandpass", [600, 2500]) * env(0.05, 0.0005, 0.01), 0.045, 0.9)
    return out


def sfx_flap():
    # A split-flap clatter: rapid clicks.
    out = np.zeros(int(0.12 * SR))
    for k in range(4):
        place(out, sfx_click(), k * 0.025, 0.7)
    return out


def sfx_stamp():
    d = 0.25
    thud = sine_sweep(220, 70, d, 30) * env(d, 0.001, 0.06)
    slap = filt(noise(0.04), "bandpass", [800, 4000]) * env(0.04, 0.0005, 0.01)
    out = np.tanh(2 * thud)
    out[: len(slap)] += 0.5 * slap
    return out


def sfx_type():
    d = 0.04
    return filt(noise(d), "bandpass", [2500, 7000]) * env(d, 0.0003, 0.006) * 0.8


def sfx_cash():
    # Cha-ching: a short bell cluster after a clack.
    out = np.zeros(int(0.8 * SR))
    place(out, sfx_click(), 0.0, 1.0)
    for f in (2093.0, 2637.0, 3136.0):
        d = 0.6
        tt = t_axis(d)
        place(out, np.sin(2 * np.pi * f * tt) * env(d, 0.001, 0.15), 0.08, 0.25)
    return reverb(out, 0.8, 0.2, 0.2)


def sfx_rumble():
    d = 0.5
    x = filt(noise(d), "lowpass", 180) * env(d, 0.01, 0.2)
    return np.tanh(3 * x)


def write(path, x, peak=0.89):
    x = np.asarray(x, dtype=np.float64)
    x = x / (np.max(np.abs(x)) + 1e-9) * peak
    stereo = np.stack([x, x], axis=1)
    wavfile.write(path, SR, (stereo * 32767).astype(np.int16))


if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "sfx"), exist_ok=True)
    write(os.path.join(OUT, "music.wav"), song())
    effects = {
        "whoosh": sfx_whoosh(True),
        "impact": sfx_impact(),
        "pop": sfx_pop(),
        "click": sfx_click(),
        "bonk": sfx_bonk(),
        "drip": sfx_drip(),
        "zip-up": sfx_zip(True),
        "zip-down": sfx_zip(False),
        "swish": sfx_swish(),
        "chime": sfx_chime(),
        "ding": sfx_ding(),
        "lock": sfx_lock(),
        "flap": sfx_flap(),
        "stamp": sfx_stamp(),
        "type": sfx_type(),
        "cash": sfx_cash(),
        "rumble": sfx_rumble(),
    }
    for name, x in effects.items():
        write(os.path.join(OUT, "sfx", name + ".wav"), x, 0.7)
    print("wrote music.wav and", len(effects), "sfx")
