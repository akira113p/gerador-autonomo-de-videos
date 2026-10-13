"""Cartões com contagem ou proporção exata, desenhados em código (a IA de imagem erra número e quantidade de divisões).
Mesmo estilo dos cartões gerados: fundo branco, contorno preto grosso levemente tremido, cor chapada, letra manuscrita.

  python piloto/v2-dia-em-roma/cartoes.py

Sobrescreve imagens/012, 014, 015, 119, 151 e 153.
"""

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

AQUI = Path(__file__).resolve().parent
W, H = 1344, 768
PRETO, BRANCO = (20, 20, 20), (255, 255, 255)
AMARELO, LARANJA, AZUL_CLARO = (255, 214, 64), (245, 160, 50), (150, 205, 240)
ROSA, AZUL, VERMELHO, VERDE = (246, 150, 190), (90, 150, 230), (224, 48, 48), (58, 168, 69)
NOITE = (40, 50, 90)
FONTE = "C:/Windows/Fonts/Inkfree.ttf"
rng = random.Random(3)


def fonte(tam: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONTE, tam)


def tremido(pts: list[tuple[float, float]], amp: float = 1.6, passo: float = 14) -> list[tuple[float, float]]:
    """Subdivide a linha e desloca cada ponto um pouco, para parecer traço de marcador."""
    out = []
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        n = max(1, int(math.dist((x0, y0), (x1, y1)) / passo))
        for i in range(n):
            f = i / n
            out.append((x0 + (x1 - x0) * f + rng.uniform(-amp, amp), y0 + (y1 - y0) * f + rng.uniform(-amp, amp)))
    out.append(pts[-1])
    return out


def linha(d: ImageDraw.ImageDraw, pts, largura: int = 7, cor=PRETO) -> None:
    pts = tremido(pts)
    d.line(pts, fill=cor, width=largura, joint="curve")
    for x, y in (pts[0], pts[-1]):
        d.ellipse((x - largura / 2, y - largura / 2, x + largura / 2, y + largura / 2), fill=cor)


def retangulo(d, x0, y0, x1, y1, cor=None, largura=7) -> None:
    if cor:
        d.rectangle((x0, y0, x1, y1), fill=cor)
    linha(d, [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)], largura)


def texto(d, xy, s, tam, cor=PRETO, ancora="mm") -> None:
    d.text(xy, s, font=fonte(tam), fill=cor, anchor=ancora, stroke_width=1, stroke_fill=cor)


def sol(d, cx, cy, r, cor=AMARELO, raios=True) -> None:
    if raios:
        for k in range(12):
            a = k * math.pi / 6
            linha(d, [(cx + math.cos(a) * (r + 14), cy + math.sin(a) * (r + 14)),
                      (cx + math.cos(a) * (r + 38), cy + math.sin(a) * (r + 38))], 6, LARANJA)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=cor)
    pts = [(cx + math.cos(a / 40 * 2 * math.pi) * r, cy + math.sin(a / 40 * 2 * math.pi) * r) for a in range(41)]
    linha(d, pts, 6)


def floco(d, cx, cy, r) -> None:
    for k in range(3):
        a = k * math.pi / 3
        linha(d, [(cx - math.cos(a) * r, cy - math.sin(a) * r), (cx + math.cos(a) * r, cy + math.sin(a) * r)], 5, AZUL)


def check(d, x, y, s=1.0) -> None:
    linha(d, [(x, y), (x + 22 * s, y + 24 * s), (x + 64 * s, y - 34 * s)], int(12 * s), VERDE)


def xis(d, x0, y0, x1, y1, largura=11) -> None:
    linha(d, [(x0, y0), (x1, y1)], largura, VERMELHO)
    linha(d, [(x1, y0), (x0, y1)], largura, VERMELHO)


def arco_do_dia(d, cx, cy, r_ext, r_int, cores) -> None:
    """Meio círculo do nascer (esquerda) ao pôr do sol (direita) em 12 fatias numeradas 1 a 12."""
    for k in range(12):
        a0, a1 = math.pi + k * math.pi / 12, math.pi + (k + 1) * math.pi / 12
        poly = [(cx + math.cos(a0 + (a1 - a0) * i / 8) * r_ext, cy + math.sin(a0 + (a1 - a0) * i / 8) * r_ext)
                for i in range(9)]
        poly += [(cx + math.cos(a1 - (a1 - a0) * i / 8) * r_int, cy + math.sin(a1 - (a1 - a0) * i / 8) * r_int)
                 for i in range(9)]
        d.polygon(poly, fill=cores[k])
        linha(d, [(cx + math.cos(a0) * r_int, cy + math.sin(a0) * r_int),
                  (cx + math.cos(a0) * r_ext, cy + math.sin(a0) * r_ext)], 5)
        am = (a0 + a1) / 2
        rm = (r_ext + r_int) / 2
        texto(d, (cx + math.cos(am) * rm, cy + math.sin(am) * rm), str(k + 1), 44)
    for r in (r_ext, r_int):
        linha(d, [(cx + math.cos(math.pi + i * math.pi / 60) * r, cy + math.sin(math.pi + i * math.pi / 60) * r)
                  for i in range(61)], 7)
    linha(d, [(cx + r_int, cy), (cx + r_ext, cy)], 5)


def novo():
    img = Image.new("RGB", (W, H), BRANCO)
    return img, ImageDraw.Draw(img)


def c012():
    img, d = novo()
    cx, cy = W / 2, 600
    arco_do_dia(d, cx, cy, 440, 300, [AMARELO] * 12)
    sol(d, cx - 520, cy - 10, 42)
    sol(d, cx + 520, cy - 10, 42, LARANJA)
    linha(d, [(90, cy + 40), (W - 90, cy + 40)], 7)
    texto(d, (cx - 520, cy + 95), "SUNRISE", 44)
    texto(d, (cx + 520, cy + 95), "SUNSET", 44)
    texto(d, (cx, cy - 120), "12 HOURS", 80)
    return img


def barra_horas(d, x0, y, comprimento, altura, cor) -> None:
    passo = comprimento / 12
    retangulo(d, x0, y, x0 + comprimento, y + altura, cor)
    for k in range(12):
        if k:
            linha(d, [(x0 + k * passo, y), (x0 + k * passo, y + altura)], 5)
        texto(d, (x0 + (k + 0.5) * passo, y + altura / 2), str(k + 1), int(min(42, passo * 0.55)))


def c014():
    img, d = novo()
    comp = 1100  # 15,2 h de luz em junho na latitude de Roma
    sol(d, W / 2, 190, 95)
    barra_horas(d, (W - comp) / 2, 370, comp, 110, AMARELO)
    texto(d, ((W - comp) / 2, 330), "JUNE", 64, ancora="lm")
    texto(d, (W / 2, 620), "1 HOUR = 75 MIN", 100)
    return img


def c015():
    img, d = novo()
    comp = 1100 * 9.15 / 15.2  # 9,15 h de luz em dezembro, na mesma escala do cartão de junho
    sol(d, W / 2, 210, 55, (255, 236, 170), raios=False)
    for x, y in [(380, 140), (520, 260), (840, 150), (960, 270), (700, 90)]:
        floco(d, x, y, 26)
    barra_horas(d, (W - comp) / 2, 370, comp, 110, AZUL_CLARO)
    texto(d, ((W - comp) / 2, 330), "DECEMBER", 64, ancora="lm")
    texto(d, (W / 2, 620), "1 HOUR = 45 MIN", 100)
    return img


def c119():
    img, d = novo()
    lado, esp = 110, 26

    def fileira(n, y, letras=None):
        x0 = (W - (n * lado + (n - 1) * esp)) / 2
        for k in range(n):
            x = x0 + k * (lado + esp)
            retangulo(d, x, y, x + lado, y + lado, (250, 244, 228))
            if letras:
                texto(d, (x + lado / 2, y + lado / 2), letras[k], 64)
        return x0, x0 + n * lado + (n - 1) * esp

    texto(d, (W / 2, 70), "7 DAYS", 64)
    a, b = fileira(7, 120)
    xis(d, a - 20, 100, b + 20, 250)
    texto(d, (W / 2, 390), "8 DAYS", 64)
    a, b = fileira(8, 440, "ABCDEFGH")
    retangulo(d, b - lado, 440, b, 440 + lado, (255, 200, 120))
    texto(d, (b - lado / 2, 440 + lado / 2), "H", 64)
    texto(d, (b - lado / 2, 600), "MARKET", 40)
    check(d, b + 30, 500)
    return img


def c151():
    img, d = novo()
    cx, cy = W / 2, 620
    arco_do_dia(d, cx, cy, 460, 300, [ROSA] * 7 + [AZUL] * 5)
    linha(d, [(90, cy + 40), (W - 90, cy + 40)], 7)
    texto(d, (cx - 330, cy + 90), "WOMEN: HOURS 1-7", 52)
    texto(d, (cx + 330, cy + 90), "MEN: HOUR 8 ON", 52)
    texto(d, (cx, cy - 130), "BATH TIME", 80)
    return img


def c153():
    img, d = novo()
    horas = 14  # 12 do dia + 2 da noite
    x0, x1, y = 80, W - 80, 330
    passo = (x1 - x0) / horas
    d.rectangle((x0 + 12 * passo, y - 230, x1, y + 210), fill=NOITE)
    d.ellipse((x1 - passo * 1.4, y - 210, x1 - passo * 0.6, y - 130), fill=(250, 240, 180))
    d.ellipse((x1 - passo * 1.2, y - 220, x1 - passo * 0.45, y - 145), fill=NOITE)
    linha(d, [(x0, y), (x1, y)], 7)
    for k in range(horas + 1):
        linha(d, [(x0 + k * passo, y - 18), (x0 + k * passo, y + 18)], 5)
    for k in range(horas):
        cor = BRANCO if k >= 12 else PRETO
        texto(d, (x0 + (k + 0.5) * passo, y - 50), str(k + 1 if k < 12 else k - 11), 44, cor)
    texto(d, ((x0 + x0 + 12 * passo) / 2, y - 125), "DAY", 52)
    texto(d, (x0 + 13 * passo, y + 180), "NIGHT", 40, BRANCO)
    retangulo(d, x0, y + 50, x0 + 7 * passo, y + 140, ROSA)
    texto(d, (x0 + 3.5 * passo, y + 95), "WOMEN", 56)
    retangulo(d, x0 + 7 * passo, y + 50, x0 + 14 * passo, y + 140, AZUL)
    texto(d, (x0 + 10.5 * passo, y + 95), "MEN", 56)
    texto(d, (W / 2, 660), "ROMAN BATH RULES, VIPASCA", 64)
    return img


def main() -> None:
    for nome, f in [("012", c012), ("014", c014), ("015", c015), ("119", c119), ("151", c151), ("153", c153)]:
        f().save(AQUI / "imagens" / f"{nome}.png")
        print("ok", nome)


if __name__ == "__main__":
    main()
