"""Gera as imagens do v13 com FLUX.2 klein (ComfyUI ligado). Pula arquivos existentes.
  python gerar_local.py estilo          -> testes t001_1.. para as referencias de estilo
  python gerar_local.py tudo [ini fim]  -> imagens/NNN.png (+ NNNb.png se a frase tem mais de 17 palavras)
  python gerar_local.py um N [seed_extra]  -> refaz uma cena (sobrescreve)
"""
import json, sys, time
from pathlib import Path
A = Path(__file__).resolve().parent
sys.path.insert(0, str(A.parents[1] / "ferramentas"))
from klein_ref import gerar

REFS = A / "imagens_gpt"
TPL = ("Use image 1 for the character and image 2 for the art style and color palette. New scene: {p} "
       "Keep the character exactly as in image 1: minimalist stick figure, white circle head, plain grey hoodie, dark navy jeans, white sneakers. "
       "Style: detailed moody illustrated environment, flat 2D illustration, muted overcast New York palette.")
TPL_E = ("Use image 1 for the character and image 2 only for the line style and level of detail; the palette is overcast New York: brick brown, concrete grey, navy, olive, pale streetlight yellow; no snow. "
         "New scene: {p} Keep the character exactly as in image 1: minimalist stick figure, white circle head, plain grey hoodie, dark navy jeans, white sneakers. "
         "Style: detailed moody illustrated environment, flat 2D illustration, muted overcast New York palette.")
TPL_N = ("Use image 1 for the art style and color palette. New scene: {p} {c} "
         "Style: detailed moody illustrated environment, flat 2D illustration, muted overcast New York palette.")
VAR = ["", " Different camera angle, a wider view.", " Different camera angle, a closer view from the side."]
LOG = A / "imagens_local_log.txt"


def log(s):
    with LOG.open("a", encoding="utf-8") as f:
        f.write(s + "\n")


def faz(c, nome, seed, extra="", estilo=False):
    saida = (REFS / nome) if estilo else (A / "imagens" / nome)
    ref2 = REFS / f"{c['ref2']}.png"
    if "grey hoodie" in c["prompt"] or estilo:
        t = (TPL_E if estilo else TPL).format(p=c["prompt"]) + extra
        refs = [REFS / "p0.png", ref2]
    else:
        ref2 = REFS / ("010.png" if "stick figure" in c["prompt"] else "030.png")
        t = TPL_N.format(p=c["prompt"], c=("Stick figures have white circle heads." if "stick figure" in c["prompt"] else "No people anywhere in the picture.")) + extra
        refs = [ref2]
    s = gerar(t, refs, saida, seed=seed)
    log(f"{nome}\tseed {seed}\t{s:.0f}s\tgerada")


def main():
    cenas = {c["cena"]: c for c in json.load(open(A / "prompts_local.json", encoding="utf-8"))}
    modo = sys.argv[1]
    if modo == "estilo":
        for n in (1, 10, 11):
            for s in (1, 2):
                faz(cenas[n], f"t{n:03d}_{s}.png", n * 10 + s, estilo=True)
    elif modo == "tudo":
        ini = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        fim = int(sys.argv[3]) if len(sys.argv) > 3 else 126
        for n in range(ini, fim + 1):
            c = cenas[n]
            if not (A / "imagens" / f"{n:03d}.png").exists():
                faz(c, f"{n:03d}.png", n * 7)
            if len(c["texto"].split()) > 17 and not (A / "imagens" / f"{n:03d}b.png").exists():
                faz(c, f"{n:03d}b.png", n * 7 + 3, VAR[1 + n % 2])
    elif modo == "um":
        n = int(sys.argv[2]); k = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        c = cenas[n]
        faz(c, f"{n:03d}.png", n * 7 + 1000 * k)
        if len(c["texto"].split()) > 17:
            faz(c, f"{n:03d}b.png", n * 7 + 3 + 1000 * k, VAR[1 + n % 2])


main()
