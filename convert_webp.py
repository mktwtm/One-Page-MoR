# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image

assets = r'C:\Users\mtboh\OneDrive\My Documents\Antigravity\WTM\One Page MoR\wtm\assets'

files = ['photo_pattern_01.jpg','photo_pattern_02.jpg','photo_pattern_03.jpg',
         'photo_pattern_05.jpg','photo_pattern_07.jpg','keyvisual_wtm.png']

for fn in files:
    src = os.path.join(assets, fn)
    dst = os.path.join(assets, os.path.splitext(fn)[0] + '.webp')
    if os.path.exists(src):
        img = Image.open(src).convert('RGB')
        img.save(dst, 'WEBP', quality=85)
        orig = os.path.getsize(src)
        new  = os.path.getsize(dst)
        pct  = 100 - new * 100 // orig
        print(f'{fn}: {orig//1024}KB -> {new//1024}KB ({pct}% smaller)')
    else:
        print(f'NOT FOUND: {src}')
