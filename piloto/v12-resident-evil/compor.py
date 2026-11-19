"""Desenha por código o que a IA erra: o relógio e a bateria do celular no canto (o contador do vídeo) e os cartões
com número. Lê imagens/ e grava imagens_final/ (1920x1080). Roda em qualquer Python com Pillow.

  python piloto/v12-resident-evil/compor.py [ids...]
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

# capítulo -> (hora no relógio, bateria em %; None = celular morto). O capítulo 0 não tem contador.
CONTADOR = {"1": ("9:40 PM", 64), "2": ("10:30 PM", 51), "3": ("11:15 PM", 44), "4": ("12:00 AM", 38),
            "5": ("1:00 AM", 31), "6": ("2:00 AM", 22), "7": ("2:30 AM", 18), "8": ("4:00 AM", 9),
            "9": ("6:40 AM", None), "10": ("7:10 AM", None)}
MORTO_A_PARTIR = 115  # cena em que o celular morre no frio

# cena -> (número grande, legenda). Fonte de cada número no roteiro da proposta.
CARTOES = {
    44: ("3 WAYS OUT", "highway · tunnel · mountains"),
    53: ("60+ vs 7", "deaths linked to the evacuation vs the storm itself"),
    80: ("DOWNWIND", "most victims lived or worked in one narrow strip · Science, 1994"),
    124: ("4 EXITS CLOSED", "phones · highway · tunnel · the line"),
    7: ("DOZENS DEAD", "Sverdlovsk, USSR · April 1979"),
    25: ("3 MINUTES", "median wait before starting down · WTC 1, 2001 (NIST)"),
    30: ("PANIC IS RARE", "decades of disaster research"),
    49: ("2,000,000+", "may have fled Hurricane Rita · Texas, 2005"),
    50: ("4 H → 20 H", "Houston to Dallas during the evacuation"),
    51: ("7", "deaths caused directly by the storm"),
    52: ("20+", "died in one evacuation bus fire"),
    67: ("100%", "fatal once symptoms appear · WHO"),
    68: ("2–3 MONTHS", "typical time from bite to symptoms"),
    90: ("80,000", "people sealed in · West Point, Monrovia, 2014"),
    91: ("21 DAYS", "planned length of the quarantine"),
    95: ("~10 DAYS", "until the quarantine was lifted"),
    126: ("2 AM → 10 AM", "Wuhan · January 23, 2020"),
    127: ("11,000,000", "people · 8 hours' notice"),
    133: ("100,000+", "dead, according to the games"),
    135: ("13 YEARS", "until Moscow admitted what happened"),
}


def contador(img: Image.Image, hora: str, bateria: int | None) -> None:
    d = ImageDraw.Draw(img, "RGBA")
    x0, y0, x1, y1 = W - 330, 36, W - 36, 116
    d.rounded_rectangle((x0, y0, x1, y1), 18, fill=(0, 0, 0, 150))
    d.text((x0 + 22, y0 + 12), hora, font=ImageFont.truetype(IMPACT, 50), fill=(255, 255, 255))
    # pilha: contorno, polo e preenchimento proporcional
    bx, by = x1 - 98, y0 + 24
    d.rounded_rectangle((bx, by, bx + 66, by + 32), 6, outline=(255, 255, 255), width=4)
    d.rectangle((bx + 66, by + 10, bx + 72, by + 22), fill=(255, 255, 255))
    if bateria is None:
        d.line((bx + 8, by + 26, bx + 58, by + 6), fill=(230, 60, 60), width=5)
    else:
        cor = (230, 60, 60) if bateria <= 20 else (255, 255, 255)
        d.rectangle((bx + 7, by + 7, bx + 7 + int(52 * bateria / 100), by + 25), fill=cor)


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
                hora, bat = CONTADOR[c["capitulo"]]
                contador(img, hora, None if n >= MORTO_A_PARTIR else bat)
            if n in CARTOES:
                cartao(img, *CARTOES[n])
            img.save(FINAL / f"{nome}.png")
    print("ok", len(list(FINAL.glob("*.png"))), "imagens")


if __name__ == "__main__":
    main()
