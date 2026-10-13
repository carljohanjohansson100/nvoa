#!/usr/bin/env python3
"""Skapar om alla genererade illustrationer och filmscener i media/generated/.

Valfritt verktyg. Webbplatsen fungerar utan det: SVG- och HTML-filerna är färdiga och kan redigeras för hand.
Kräver bara Python 3 (standardbiblioteket). Kör: python3 tools/generate_media/build.py
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import images as I
import films as F

OUT = os.path.join(HERE, '..', '..', 'media', 'generated')


def w(rel, s):
    p = os.path.normpath(os.path.join(OUT, rel))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)


for n, f in [('steg-1-kalla', I.steg_kalla), ('steg-2-vattenverk', I.steg_vattenverk), ('steg-3-ledningsnat', I.steg_ledningsnat),
             ('steg-4-hemmet', I.steg_hemmet), ('steg-5-reningsverk', I.steg_reningsverk),
             ('bild-1-ledningsarbete', I.gal_ledningsarbete), ('bild-2-pumpstation', I.gal_pumpstation),
             ('bild-3-atervinningscentral', I.gal_atervinningscentral), ('bild-4-sorteringskarl', I.gal_sorteringstunnor),
             ('bild-5-vattenverk-inne', I.gal_vattenverk_inne), ('bild-6-provtagning', I.gal_provtagning),
             ('bild-7-sopbil', I.gal_sopbil), ('bild-8-miljohus', I.gal_miljohus), ('bild-9-sjopromenad', I.gal_sjopromenad),
             ('karta-driftinformation', I.karta)]:
    w(n + '.svg', f())
for k, f in I.ITEMS.items():
    w(f'items/{k}.svg', f())
for id, label, c in I.BINS:
    w(f'bins/{id}.svg', I.bin_svg(id, label, c))
w('films/hero-vattnets-kretslopp.html', F.hero_scene())
w('hero-poster.svg', F.hero_poster())
w('films/en-dag-pa-reningsverket.html', F.film1())
w('films/sa-blir-matavfall-biogas.html', F.film2())
w('films/vad-hander-nar-du-spolar.html', F.film3())
print('Klart: media/generated/ är uppdaterad.')
