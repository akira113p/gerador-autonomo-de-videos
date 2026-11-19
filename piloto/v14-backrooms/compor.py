"""Desenha por código o que a IA erra: o relógio e a bateria do celular no canto (o contador do vídeo) e os cartões
com número. Lê imagens/ e grava imagens_final/ (1920x1080). Roda em qualquer Python com Pillow.

  python piloto/v14-backrooms/compor.py [ids...]
"""

import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

AQUI = Path(__file__).resolve().parent
ORIG, FINAL = AQUI / "imagens", AQUI / "imagens_final"
W, H = 1920, 1080
IMPACT = "C:/Windows/Fonts/impact.ttf"
NEGRITO = "C:/Windows/Fonts/arialbd.ttf"
AMARELO = (255, 214, 0)

# capítulo -> texto do contador no canto (capítulos fora daqui não têm contador)
CONTADOR = {"1": "YOUR COUNT: HOUR 1", "2": "YOUR COUNT: HOUR 9", "3": "YOUR COUNT: DAY 3?", "4": "YOUR COUNT: DAY 4?", "5": "YOUR COUNT: DAY 21?", "6": "YOUR COUNT: DAY 200?", "7": "YOUR COUNT: DAY ???", "8": "YOUR COUNT: DAY ???"}

# cena -> (número grande, legenda). Fonte de cada número no roteiro da proposta.
CARTOES = {
    9: ("2002", "Oshkosh, Wisconsin"),
    10: ("600,000,000 SQ MI", "the original post · 4chan, May 2019"),
    11: ("MAY 2024", "the photo is traced to its source"),
    23: ("100× A SECOND", "old fluorescent lights flicker"),
    24: ("HEADACHES ÷ 2", "with flicker-free lights · 1989 study"),
    42: ("< 20 M", "circles walked blindfolded · 2009 study"),
    50: ("1–2%", "body weight lost in water: mood and focus already drop"),
    55: ("AUGUST 20?", "what Siffre thought the date was"),
    56: ("MID-SEPTEMBER", "the real date"),
    66: ("600 KCAL", "one full bottle of Almond Water"),
    100: ("20%", "of the M.E.G. budget · defending Base Gamma"),
    110: ("8 FEET", "how far a Clump reaches"),
    140: ("40 YARDS", "to Base Gamma"),
}


def contador(img: Image.Image, texto: str) -> None:
    d = ImageDraw.Draw(img, "RGBA")
    f = ImageFont.truetype(IMPACT, 50)
    larg = d.textlength(texto, font=f)
    x1, y0 = W - 36, 36
    d.rounded_rectangle((x1 - larg - 44, y0, x1, y0 + 80), 18, fill=(0, 0, 0, 150))
    d.text((x1 - larg - 22, y0 + 12), texto, font=f, fill=(255, 255, 255))


def cartao(img: Image.Image, grande: str, legenda: str) -> None:
    d = ImageDraw.Draw(img, "RGBA")
    f1, f2 = ImageFont.truetype(IMPACT, 150), ImageFont.truetype(NEGRITO, 42)
    w1, w2 = d.textlength(grande, font=f1), d.textlength(legenda, font=f2)
    larg = max(w1, w2) + 120
    x0, y0 = (W - larg) / 2, H - 420
    d.rounded_rectangle((x0, y0, x0 + larg, y0 + 300), 28, fill=(0, 0, 0, 175))
    d.text(((W - w1) / 2, y0 + 30), grande, font=f1, fill=AMARELO, stroke_width=6, stroke_fill=(0, 0, 0))
    d.text(((W - w2) / 2, y0 + 220), legenda, font=f2, fill=(255, 255, 255))


def main() -> None:
    cenas = json.loads((AQUI / "roteiro.json").read_text(encoding="utf-8"))["cenas"]
    pedidos = set(sys.argv[1:])
    FINAL.mkdir(exist_ok=True)
    for c in cenas:
        if pedidos and c["id"] not in pedidos:
            continue
        n = int(c["id"])
        for nome in [c["id"]] + ([c["id"] + "b"] if c["extra"] else []):
            img = Image.open(ORIG / f"{nome}.png").convert("RGB").resize((W, H), Image.LANCZOS)
            if c["capitulo"] in CONTADOR:
                contador(img, CONTADOR[c["capitulo"]])
            if n in CARTOES:
                cartao(img, *CARTOES[n])
            img.save(FINAL / f"{nome}.png")
    print("ok", len(list(FINAL.glob("*.png"))), "imagens")


if __name__ == "__main__":
    main()
