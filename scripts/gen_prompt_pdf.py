#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, re
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

pdfmetrics.registerFont(TTFont('Arial', '/Library/Fonts/Arial Unicode.ttf'))
W, H = A4
M = 50
OUT = os.path.expanduser('~/.openclaw/workspace/magazines/android-magazine/reports/LISA_Master_Prompt_v6_FINAL.pdf')
SRC = os.path.expanduser('~/.openclaw/workspace/LISA_Editorial_Master_Prompt_v4.md')

src = open(SRC).read()

c = canvas.Canvas(OUT, pagesize=A4)
c.setTitle('LISA Editorial Intelligence Master Prompt v6 FINAL')

# Header
c.setFillColor(colors.HexColor('#1A1A2E'))
c.rect(0, H-70, W, 70, fill=1, stroke=0)
c.setFillColor(colors.HexColor('#E94560'))
c.setFont('Arial', 20)
c.drawString(M, H-38, 'LISA — Editorial Intelligence')
c.setFillColor(colors.white)
c.setFont('Arial', 11)
c.drawString(M, H-58, 'Master Prompt v6 FINAL  |  AndroidMagazine  |  17. 8. 2026  |  Schvalil Roman Zavrel')

y = H - 90

def chk(c, y, need=25):
    if y < M + need:
        c.showPage()
        return H - M
    return y

def clean(line):
    line = re.sub(r'\*\*(.+?)\*\*', lambda m: m.group(1), line)
    line = re.sub(r'`(.+?)`', lambda m: m.group(1), line)
    line = re.sub(r'\*(.+?)\*', lambda m: m.group(1), line)
    return line

def wrap(c, text, x, y, width, size=10, color='#222222'):
    c.setFont('Arial', size)
    c.setFillColor(colors.HexColor(color))
    words = text.split()
    if not words:
        return y
    line = ''
    for w in words:
        test = (line + ' ' + w).strip()
        if c.stringWidth(test, 'Arial', size) < width:
            line = test
        else:
            y = chk(c, y)
            c.setFont('Arial', size)
            c.setFillColor(colors.HexColor(color))
            c.drawString(x, y, line)
            y -= size + 3
            line = w
    if line:
        y = chk(c, y)
        c.drawString(x, y, line)
        y -= size + 3
    return y

for raw in src.split('\n'):
    line = raw.rstrip()
    y = chk(c, y)
    txt = clean(line)

    if line.startswith('# ') and not line.startswith('## '):
        y -= 4
        c.setFillColor(colors.HexColor('#1A1A2E'))
        c.rect(M-5, y-5, W-2*M+10, 22, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont('Arial', 13)
        c.drawString(M, y+2, txt[2:])
        y -= 26
    elif line.startswith('## '):
        y -= 8
        c.setFillColor(colors.HexColor('#E94560'))
        c.setFont('Arial', 12)
        c.drawString(M, y, txt[3:])
        y -= 4
        c.setStrokeColor(colors.HexColor('#E94560'))
        c.line(M, y, W-M, y)
        y -= 10
    elif line.startswith('### '):
        y -= 4
        c.setFillColor(colors.HexColor('#1A1A2E'))
        c.setFont('Arial', 11)
        c.drawString(M, y, txt[4:])
        y -= 14
    elif re.match(r'^[-*☑□]\s', line):
        body = re.sub(r'^[-*☑□]\s+', '', txt)
        c.setFillColor(colors.HexColor('#E94560'))
        c.setFont('Arial', 10)
        c.drawString(M+2, y, '•')
        y = wrap(c, body, M+14, y, W-2*M-20)
    elif line.startswith('---'):
        c.setStrokeColor(colors.HexColor('#DDDDDD'))
        c.line(M, y, W-M, y)
        y -= 8
    elif line.strip() == '':
        y -= 4
    elif line.startswith('|'):
        y = wrap(c, txt, M, y, W-2*M, size=9, color='#444444')
    else:
        y = wrap(c, txt, M, y, W-2*M)

c.setFont('Arial', 8)
c.setFillColor(colors.HexColor('#999999'))
c.drawCentredString(W/2, M-15, 'LISA AI sefredaktorka  |  Text Factory  |  AndroidMagazine.eu  |  v6 FINAL 17.8.2026')
c.save()
print('OK:', OUT)
