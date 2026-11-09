#!/usr/bin/env python3
"""Real-ESRGAN on CPU with PyTorch (no Vulkan / GPU needed). Our own Arete upscaler.

Runs the official SRVGGNetCompact weights from the Real-ESRGAN v0.2.5.0 release:
  realesr-animevideov3.pth  (illustration video, default, 16 conv blocks)
  realesr-general-x4v3.pth  (general, 32 conv blocks; try it if the anime model flattens washes)
Pipeline: frames -> ESRGAN x4 -> lanczos to exactly WxH (cover + centre crop) -> blend PAPER_MIX of a
plain lanczos upscale back in (keeps watercolor paper grain and soft pigment edges) -> x264 CRF 16,
same fps, audio copied.

Usage: python esrgan_cpu.py IN.mp4 OUT.mp4 [--w 720 --h 1280 --model anime|general --mix 0.25]
Env:   ESRGAN_WEIGHTS  folder with the .pth files (default ./weights)
Speed (box, CPU): ~0.7 s per 270x480 frame, so an 8 s 24 fps part takes ~2-3 min (estimate).
"""
import argparse, os, subprocess, time
import numpy as np, torch, torch.nn as nn, torch.nn.functional as F

class SRVGG(nn.Module):
    def __init__(s, nf=64, nc=16, up=4):
        super().__init__(); s.up = up
        b = [nn.Conv2d(3, nf, 3, 1, 1), nn.PReLU(nf)]
        for _ in range(nc): b += [nn.Conv2d(nf, nf, 3, 1, 1), nn.PReLU(nf)]
        b += [nn.Conv2d(nf, 3 * up * up, 3, 1, 1)]
        s.body = nn.ModuleList(b); s.ps = nn.PixelShuffle(up)
    def forward(s, x):
        o = x
        for l in s.body: o = l(o)
        return s.ps(o) + F.interpolate(x, scale_factor=s.up, mode='nearest')

ap = argparse.ArgumentParser()
ap.add_argument('inp'); ap.add_argument('out')
ap.add_argument('--w', type=int, default=720); ap.add_argument('--h', type=int, default=1280)
ap.add_argument('--model', default='anime', choices=['anime', 'general'])
ap.add_argument('--mix', type=float, default=float(os.environ.get('PAPER_MIX', 0.25)))
a = ap.parse_args()

wd = os.environ.get('ESRGAN_WEIGHTS', 'weights')
net = SRVGG(nc=16 if a.model == 'anime' else 32)
sd = torch.load(os.path.join(wd, 'realesr-animevideov3.pth' if a.model == 'anime' else 'realesr-general-x4v3.pth'), map_location='cpu')
net.load_state_dict(sd.get('params', sd)); net.eval(); torch.set_num_threads(os.cpu_count() or 4)

w, h, fps = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height,r_frame_rate',
                            '-of', 'csv=p=0', a.inp], capture_output=True, text=True).stdout.strip().split(',')[:3]
w, h = int(w), int(h)
if h <= w: raise SystemExit(f'reject: {a.inp} is not vertical ({w}x{h})')

dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', a.inp, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
fit = f'scale={a.w}:{a.h}:force_original_aspect_ratio=increase:flags=lanczos,crop={a.w}:{a.h},setsar=1,format=yuv444p'
enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{w*4}x{h*4}', '-r', fps, '-i', '-',
                        '-i', a.inp, '-filter_complex',
                        f"[0:v]{fit}[e];[1:v]{fit}[s];[e][s]blend=all_expr='A*{1-a.mix:.3f}+B*{a.mix:.3f}',format=yuv420p[v]",
                        '-map', '[v]', '-map', '1:a?', '-c:a', 'copy', '-c:v', 'libx264', '-crf', '16', '-preset', 'medium',
                        '-r', fps, '-shortest', a.out], stdin=subprocess.PIPE)
t0 = time.time(); n = 0
with torch.inference_mode():
    while True:
        buf = dec.stdout.read(w * h * 3)
        if len(buf) < w * h * 3: break
        x = torch.from_numpy(np.frombuffer(buf, np.uint8).reshape(h, w, 3).copy()).permute(2, 0, 1)[None].float() / 255
        enc.stdin.write(net(x).clamp(0, 1)[0].permute(1, 2, 0).mul(255).round().byte().numpy().tobytes()); n += 1
enc.stdin.close(); enc.wait()
print(f'{n} frames in {time.time()-t0:.1f}s -> {a.out}')
