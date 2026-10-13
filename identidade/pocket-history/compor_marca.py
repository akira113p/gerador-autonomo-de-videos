"""Compõe a foto de perfil (800x800) e o banner (2048x1152) do canal a partir de bases/ e do texto, em código.
Roda no C:/ai-local/venv-voz (precisa de numpy e scipy).

  C:/ai-local/venv-voz/Scripts/python.exe identidade/pocket-history/compor_marca.py

Saídas: perfil_N.png, banner_N.png e prévias (perfil em círculo de 98 px, banner com a área segura de 1235x338 em vermelho).
"""

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy.ndimage import label

AQUI = Path(__file__).resolve().parent
BASES = AQUI / "bases"
IMPACT, INK = "C:/Windows/Fonts/impact.ttf", "C:/Windows/Fonts/Inkfree.ttf"
AMARELO, PRETO, BRANCO = (255, 226, 0), (0, 0, 0), (255, 255, 255)
W, H = 2048, 1152
SEGURA = (406, 407, 1641, 745)  # área que aparece em qualquer tela


def cor_fundo(img: Image.Image) -> np.ndarray:
    a = np.asarray(img.convert("RGB")).astype(float)
    borda = np.concatenate([a[:8].reshape(-1, 3), a[-8:].reshape(-1, 3), a[:, :8].reshape(-1, 3), a[:, -8:].reshape(-1, 3)])
    return np.median(borda, axis=0)


def recortar(img: Image.Image) -> tuple[Image.Image, np.ndarray]:
    """Tira o fundo liso (a parte ligada à borda e parecida com a cor do fundo). Devolve RGBA recortado na caixa."""
    rgb = np.asarray(img.convert("RGB")).astype(float)
    bg = cor_fundo(img)
    dist = np.linalg.norm(rgb - bg, axis=2)
    rotulos, _ = label(dist < 45)
    borda = set(np.unique(np.concatenate([rotulos[0], rotulos[-1], rotulos[:, 0], rotulos[:, -1]]))) - {0}
    fundo = np.isin(rotulos, list(borda))
    alfa = np.where(fundo, np.clip((dist - 14) / 22, 0, 1), 1.0)
    out = Image.fromarray(np.dstack([rgb, alfa * 255]).astype(np.uint8), "RGBA")
    return out.crop(out.getchannel("A").point(lambda v: 255 if v > 30 else 0).getbbox()), bg


def contorno(d, xy, s, fonte, cor, esp) -> None:
    d.text(xy, s, font=fonte, fill=cor, anchor="mm", stroke_width=esp, stroke_fill=PRETO)


def perfil(n: int) -> None:
    img = Image.open(BASES / f"perfil_{n}.png").convert("RGB").resize((800, 800), Image.LANCZOS)
    img.save(AQUI / f"perfil_{n}.png")
    prev = Image.new("RGB", (800 + 40 + 160 + 20 + 98, 800), (245, 245, 245))
    for tam, x in [(800, 0), (160, 840), (98, 1020)]:
        m = Image.new("L", (tam, tam), 0)
        ImageDraw.Draw(m).ellipse((0, 0, tam - 1, tam - 1), fill=255)
        prev.paste(img.resize((tam, tam), Image.LANCZOS), (x, 0), m)
    prev.save(AQUI / f"perfil_{n}_previa_circulo.png")


def banner(n_perfil: int, n_marcos: int) -> None:
    pers, bg_l = recortar(Image.open(BASES / f"perfil_{n_perfil}.png"))
    marcos, bg_r = recortar(Image.open(BASES / f"marcos_{n_marcos}.png"))
    # fundo: degradê horizontal entre a cor de fundo de cada arte (assim o recorte não deixa halo)
    t = np.linspace(0, 1, W)[None, :, None]
    fundo = (bg_l[None, None, :] * (1 - t) + bg_r[None, None, :] * t) * np.ones((H, 1, 1))
    img = Image.fromarray(fundo.astype(np.uint8), "RGB").convert("RGBA")

    h = 740
    pers = pers.resize((round(pers.width * h / pers.height), h), Image.LANCZOS)
    img.alpha_composite(pers, (50, 1090 - h))
    w = 1100
    marcos = marcos.resize((w, round(marcos.height * w / marcos.width)), Image.LANCZOS)
    img.alpha_composite(marcos, (W - w - 50, 1090 - marcos.height))

    img = img.convert("RGB")
    d = ImageDraw.Draw(img)
    titulo = "POCKET HISTORY"
    tam = 240
    f = ImageFont.truetype(IMPACT, tam)
    while d.textlength(titulo, font=f) > 920:  # cabe entre o personagem e a borda direita da área segura
        tam -= 4
        f = ImageFont.truetype(IMPACT, tam)
    cx, cy = 1175, 576
    contorno(d, (cx + 8, cy + 10), titulo, f, PRETO, 14)
    contorno(d, (cx, cy), titulo, f, AMARELO, 14)
    destino = AQUI / f"banner_{n_perfil}.png"
    img.save(destino)

    prev = img.copy()
    pd = ImageDraw.Draw(prev, "RGBA")
    pd.rectangle(SEGURA, outline=(255, 0, 0, 255), width=6)
    prev.resize((1024, 576)).save(AQUI / f"banner_{n_perfil}_previa_area_segura.png")


def tela_final(n_perfil: int) -> None:
    """Fundo dos 15 s finais (1920x1080): marca à esquerda e espaços para os elementos finais do YouTube
    (círculo de inscrição e um vídeo). No Studio, encaixe os elementos sobre as áreas claras."""
    w, h = 1920, 1080
    pers, bg_l = recortar(Image.open(BASES / f"perfil_{n_perfil}.png"))
    _, bg_r = recortar(Image.open(BASES / "marcos_2.png"))
    t = np.linspace(0, 1, w)[None, :, None]
    fundo = (bg_l[None, None, :] * (1 - t) + bg_r[None, None, :] * t) * np.ones((h, 1, 1))
    img = Image.fromarray(fundo.astype(np.uint8), "RGB").convert("RGBA")
    ph = 560
    pers = pers.resize((round(pers.width * ph / pers.height), ph), Image.LANCZOS)
    img.alpha_composite(pers, (90, 1020 - ph))

    d = ImageDraw.Draw(img, "RGBA")
    f = ImageFont.truetype(IMPACT, 150)
    contorno(d, (960 + 7, 150 + 9), "POCKET HISTORY", f, PRETO, 12)
    contorno(d, (960, 150), "POCKET HISTORY", f, AMARELO, 12)
    # vídeo: 16:9 à direita; inscrição: círculo entre o personagem e o vídeo
    caixa = (1080, 330, 1800, 735)
    cx, cy, r = 830, 532, 120
    camada = Image.new("RGBA", img.size, (0, 0, 0, 0))  # desenhar direto em RGBA substitui o pixel em vez de misturar
    dc = ImageDraw.Draw(camada)
    dc.rounded_rectangle(caixa, 18, fill=(255, 255, 255, 90), outline=(0, 0, 0, 255), width=6)
    dc.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(255, 255, 255, 90), outline=(0, 0, 0, 255), width=6)
    img.alpha_composite(camada)
    d = ImageDraw.Draw(img)
    contorno(d, ((caixa[0] + caixa[2]) / 2, caixa[1] - 55), "WATCH NEXT", ImageFont.truetype(IMPACT, 70), BRANCO, 7)
    img.convert("RGB").save(AQUI / "tela_final.png")


def main() -> None:
    for n in (1, 3):
        perfil(n)
        banner(n, 2)
        print("ok", n)
    tela_final(3)
    print("ok tela_final")


if __name__ == "__main__":
    main()
