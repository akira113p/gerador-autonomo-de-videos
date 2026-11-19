"""Lê roteiro.md (fonte da verdade do texto) e grava roteiro.json para os outros scripts.

  python piloto/v14-backrooms/construir_roteiro.py

Cada linha numerada vira uma cena: id de 3 dígitos, texto sem os marcadores [...], capítulo e trilha.
Cena com imagem extra (imagens/NNNb.png) troca de imagem no meio da fala.
"""

import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent

# trilha por intervalo de cenas (o resto não existe: todo o vídeo está coberto)
TRILHAS = [((1, 69), "liminar"), ((70, 78), "tensa"), ((79, 86), "liminar"), ((87, 100), "jazz"), ((101, 157), "tensa"), ((158, 167), "liminar")]


def trilha(n: int) -> str:
    return next(nome for (a, b), nome in TRILHAS if a <= n <= b)


def main() -> None:
    md = (AQUI / "roteiro.md").read_text(encoding="utf-8")
    titulo = md.splitlines()[0].lstrip("# ").strip()
    prompts = {}
    pj = AQUI / "prompts_local.json"
    if pj.exists():
        dados = json.loads(pj.read_text(encoding="utf-8"))
        prompts = {int(p["cena"]): p for p in (dados if isinstance(dados, list) else dados.get("cenas", []))}
    cenas, cap, nome_cap, novo_cap = [], None, "", False
    for linha in md.splitlines():
        if m := re.match(r"^## (\w+)\. ([^·]*)", linha):
            cap, nome_cap, novo_cap = m.group(1), m.group(2).split("(")[0].strip(), True
            continue
        if m := re.match(r"^(\d+)\. (.*)", linha):
            n = int(m.group(1))
            texto = re.sub(r"\s*\[[^\]]*\]", "", m.group(2)).strip()
            cenas.append({
                "id": f"{n:03d}",
                "texto": texto,
                "capitulo": cap,
                "nome_capitulo": nome_cap,
                "trilha": trilha(n),
                "inicio_capitulo": novo_cap,
                "cartao": bool(prompts.get(n, {}).get("cartao", False)),
                "extra": (AQUI / "imagens" / f"{n:03d}b.png").exists(),
            })
            novo_cap = False
    assert [int(c["id"]) for c in cenas] == list(range(1, len(cenas) + 1)), "numeração com buraco"
    (AQUI / "roteiro.json").write_text(
        json.dumps({"titulo": titulo, "cenas": cenas}, indent=1, ensure_ascii=False), encoding="utf-8")
    print(len(cenas), "cenas", sum(len(c["texto"].split()) for c in cenas), "palavras")


if __name__ == "__main__":
    main()
