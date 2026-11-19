"""Gera as imagens do vídeo 14 com o FLUX.2 klein (ferramentas/klein_ref.py). Pula arquivos existentes.
  python gerar_local.py [ids...]       (sem ids: todas; sufixo b = imagem extra; 'ancoras' = 60 105 116)
  Variáveis: SEED_EXTRA=1000 refaz com outra seed (ex.: refazer)."""
import json, os, sys, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "ferramentas"))
from klein_ref import gerar

AQUI = Path(__file__).resolve().parent
G = AQUI / "imagens_gpt"
REF2 = {"A": "_L0", "B": "_L0", "C": "_L0", "M": "_L0", "L1": "060", "L2": "105", "L3": "116"}
PERSO = {"y": [G / "p0.png"], "j": [G / "p0b.png"], "jp": [G / "p0b.png"], "n": []}
MOLDE = ("Use image 1 for the character and image 2 for the art style and color palette. {extra}New scene: {p}. "
         "Keep the character exactly as in image 1. Draw only single figures, not a character sheet. Style: minimalist stick figures with single thin black line arms and legs in a detailed moody illustrated environment with soft shadows, depth, dim greenish fluorescent light and an oppressive mood, flat 2D illustration.")
MOLDE_N = ("Use image 1 for the art style and color palette only. New scene: {p}. "
           "Style: detailed moody illustrated environment with soft shadows, depth, dim greenish fluorescent light and an oppressive mood, flat 2D illustration. Characters, if any, are thin-line stick figures with plain white circle heads.")
LOG = AQUI / "imagens_local_log.txt"
EXTRA = int(os.environ.get("SEED_EXTRA", "0"))


def tarefa(c, b):
    n = c["cena"]
    nome = f"{n:03d}{'b' if b else ''}"
    saida = AQUI / "imagens" / f"{nome}.png"
    if saida.exists():
        return
    r = REF2.get(c["ref2"], "_L0")
    if r == "_L0":
        r = ["_L0", "_L0b", "_L0c", "_L0d"][(n + (1 if b else 0)) % 4]
    ref2 = G / f"{r}.png"
    chars = PERSO[c["perso"]]
    p = c["prompt"] + (". A different camera angle and composition" if b else "")
    if c["ref2"] == "N":
        refs = chars
        prompt = ("Use image 1 for the character only. " if chars else "") + "New scene in natural colors, entirely outdoors or in a cave, NO yellow room and NO office: " + p + ". Keep the character exactly as in image 1. Style: minimalist stick figure with thin black line arms and legs in a detailed moody illustrated environment with soft shadows and depth, flat 2D illustration."
    elif c["perso"] == "n":
        refs, prompt = [ref2], MOLDE_N.format(p=p)
    else:
        extra = {"y": "The character wears only a plain blue t-shirt, his arms and legs are thin black lines, bare head, no hoodie, no hat, no trousers. ",
                 "j": "The character wears the lime-yellow explorer jacket with the small black eagle patch, thin black line legs, bare head. ",
                 "jp": "The character wears the lime-yellow explorer jacket with the small black eagle patch, thin black line legs, bare head. Image 3 is the partner (a stick figure woman with a low ponytail in a lime-yellow jacket). "}[c["perso"]]
        refs = chars + [ref2] + ([G / "partner.png"] if c["perso"] == "jp" else [])
        prompt = MOLDE.format(p=p, extra=extra) + (" Level 0 means vast open office-like rooms with sickly mono-yellow wallpaper, partition walls and doorless openings, a low drop ceiling with fluorescent panels, damp stained beige carpet, never a hotel corridor with rows of doors." if c["ref2"] in ("A","B","C","M") else "")
    seed = n * 7 + (500 if b else 0) + EXTRA
    try:
        s = gerar(prompt, refs, saida, seed=seed)
        msg = f"{nome}\tseed {seed}\t{s:.0f}s\tgerada"
    except Exception as e:
        msg = f"{nome}\tERRO {str(e)[:120]}"
    print(msg, flush=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(msg + "\n")


def main():
    cenas = json.loads((AQUI / "prompts_local.json").read_text(encoding="utf-8"))
    pedidos = sys.argv[1:]
    if pedidos == ["ancoras"]:
        pedidos = ["60", "105", "116"]
    jobs = []
    for c in cenas:
        n = c["cena"]
        for b in (False, True):
            if b and len(c["texto"].split()) <= 17:
                continue
            tag = f"{n}{'b' if b else ''}"
            if pedidos and tag not in pedidos and str(n) not in pedidos:
                continue
            jobs.append((c, b))
    with ThreadPoolExecutor(2) as ex:
        list(ex.map(lambda j: tarefa(*j), jobs))


main()

