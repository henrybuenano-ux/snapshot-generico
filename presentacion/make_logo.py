#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recrea el wordmark de omnia. Genera 2 variantes en assets/:
  - omnia-logo.png        (degradado azul→púrpura→rosa + 'in business' oscuro)
  - omnia-logo-white.png  (todo blanco, para fondos con degradado)
Placeholder fiel mientras no tengamos el PNG oficial."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(__file__)
os.makedirs(os.path.join(HERE, "assets"), exist_ok=True)
F_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F_REG  = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
PAD = 36
f_omnia = ImageFont.truetype(F_BOLD, 360)
f_sub   = ImageFont.truetype(F_REG, 132)
STOPS = [(0.0,(0x1D,0x9B,0xF0)),(0.5,(0x8B,0x5C,0xF6)),(1.0,(0xEC,0x48,0x99))]

tmp = ImageDraw.Draw(Image.new("RGBA",(10,10)))
ob = tmp.textbbox((0,0),"omnia",font=f_omnia)
sb = tmp.textbbox((0,0),"in business",font=f_sub)
ow,oh = ob[2]-ob[0], ob[3]-ob[1]
sw,sh = sb[2]-sb[0], sb[3]-sb[1]
gap = 26
W = PAD*2 + max(ow,sw)
H = PAD*2 + oh + gap + sh

def color_at(t):
    for i in range(len(STOPS)-1):
        t0,c0 = STOPS[i]; t1,c1 = STOPS[i+1]
        if t0 <= t <= t1:
            f=(t-t0)/(t1-t0)
            return tuple(int(c0[k]+(c1[k]-c0[k])*f) for k in range(3))
    return STOPS[-1][1]

def build(white):
    canvas = Image.new("RGBA",(W,H),(0,0,0,0))
    mask = Image.new("L",(W,H),0)
    ImageDraw.Draw(mask).text((PAD-ob[0], PAD-ob[1]),"omnia",font=f_omnia,fill=255)
    if white:
        fill = Image.new("RGBA",(W,H),(255,255,255,255))
        canvas.paste(fill,(0,0),mask)
        sub_color=(255,255,255,235)
    else:
        grad = Image.new("RGB",(W,H)); gpx = grad.load()
        for x in range(W):
            c = color_at(x/(W-1))
            for y in range(H): gpx[x,y]=c
        canvas.paste(grad,(0,0),mask)
        sub_color=(0x2B,0x2D,0x3A,255)
    ImageDraw.Draw(canvas).text((PAD-sb[0]+6, PAD+oh+gap-sb[1]),"in business",font=f_sub,fill=sub_color)
    return canvas

build(False).save(os.path.join(HERE,"assets","omnia-logo.png"))
build(True).save(os.path.join(HERE,"assets","omnia-logo-white.png"))
print("OK -> assets/omnia-logo.png + omnia-logo-white.png", (W,H))
