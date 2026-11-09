# Join per-paragraph Chatterbox takes into one narration file.
# Verified on Garbo: joined.wav == plain concatenation of p1..p4.wav (no crossfade,
# no stretching). Each Chatterbox take already has ~0.25 s lead-in and ~0.1-0.2 s tail,
# so the natural paragraph pause is ~0.4-0.5 s.
# usage: python join_paragraphs.py joined.wav p1.wav p2.wav p3.wav p4.wav
import sys, numpy as np, soundfile as sf
parts = [sf.read(p) for p in sys.argv[2:]]
sr = parts[0][1]; assert all(s == sr for _, s in parts)
sf.write(sys.argv[1], np.concatenate([a if a.ndim == 1 else a.mean(1) for a, _ in parts]), sr)
print("joined", len(parts), "parts")
