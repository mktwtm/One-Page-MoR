# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image

ASSETS = r'C:\Users\mtboh\OneDrive\My Documents\Antigravity\WTM\One Page MoR\wtm\assets'

# (relative path inside assets/, preserve_alpha?)
FILES: list[tuple[str, bool]] = [
    # original landing assets — RGB (jpg)
    ('photo_pattern_01.jpg', False),
    ('photo_pattern_02.jpg', False),
    ('photo_pattern_03.jpg', False),
    ('photo_pattern_05.jpg', False),
    ('photo_pattern_07.jpg', False),
    ('keyvisual_wtm.png',    False),

    # corporate site additions — PNGs with transparency must keep alpha
    ('whoweare.png',                       True),
    ('team-2023.jpg',                      False),
    ('mor-hero-glass.png',                 True),
    ('hero-arrow.png',                     True),
    ('world-map.png',                      True),
    ('gil-pletsch.jpg',                    False),
    ('valmor-kerber.jpg',                  False),
    ('orlando-mazzotta.jpg',               False),
    ('thiago-schutz.jpg',                  False),
    ('leadership/lisandro-vieira.png',     True),
    ('leadership/rafael-santiago.png',     True),
    ('leadership/dione-pioner.png',        True),
    ('leadership/henrique-dias.png',       True),
]


def convert(rel: str, keep_alpha: bool) -> None:
    src = os.path.join(ASSETS, rel)
    dst = os.path.join(ASSETS, os.path.splitext(rel)[0] + '.webp')
    if not os.path.exists(src):
        print(f'NOT FOUND: {src}')
        return
    img = Image.open(src)
    if keep_alpha and img.mode in ('RGBA', 'LA', 'P'):
        img = img.convert('RGBA')
    else:
        img = img.convert('RGB')
    img.save(dst, 'WEBP', quality=85, method=6)
    orig = os.path.getsize(src)
    new = os.path.getsize(dst)
    pct = 100 - new * 100 // max(orig, 1)
    print(f'{rel}: {orig // 1024}KB -> {new // 1024}KB ({pct}% smaller)')


if __name__ == '__main__':
    for rel, alpha in FILES:
        convert(rel, alpha)
