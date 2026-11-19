"""Desenha por código o que a IA erra: o relógio e a bateria do celular no canto (o contador do vídeo) e os cartões
com número. Lê imagens/ e grava imagens_final/ (1920x1080). Roda em qualquer Python com Pillow.

  python piloto/v13-bloods-nova-york/compor.py [ids...]
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
CONTADOR = {"1": "JUNE", "2": "JULY", "3": "SEPTEMBER", "4": "NOVEMBER", "5": "MARCH", "6": "APRIL", "8": "JUNE"}

# cena -> (número grande, legenda). Fonte de cada número no roteiro da proposta.
CARTOES = {
    5: ("1 YEAR", "most common length of a gang membership"),
    12: ("1993", "Rikers Island, New York"),
    22: ("~1 IN 3", "joined a gang · Rochester study, high-risk neighborhoods"),
    23: ("14", "peak age for joining a gang · United States"),
    38: ("16,141", "names in the NYPD gang database · 2022"),
    39: ("99%", "Black or Hispanic · NYC Department of Investigation"),
    51: ("1/3 → 2/3", "of the teenagers · of the offenses"),
    63: ("70% · 6%", "of gunshot survivors · of the city · Chicago"),
    76: ("70", "NYPD gang takedowns in 2025"),
    84: ("5 · 7 · 10 YEARS", "added for a gun: carried · brandished · fired"),
    87: ("6 → 10", "defendants · Nov 2018 → Jan 2019"),
    88: ("15 YEARS", "guilty plea"),
    89: ("24 YEARS", "after trial"),
    94: ("47+ YEARS", "what prosecutors said he faced"),
    96: ("2 YEARS", "his sentence after cooperating"),
    106: ("~400,000", "young people join a gang each year in the US · almost as many leave"),
    117: ("688", "shootings in New York in 2025 · fewest on record"),
    118: ("1,294", "shootings in 2022"),
    119: ("~2%", "of US youth are in a gang at any given time"),
    123: ("50 YEARS", "federal sentence · 2003"),
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
