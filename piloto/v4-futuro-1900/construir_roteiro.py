"""Lê roteiro.md (fonte da verdade do texto) e grava roteiro.json para os outros scripts.

  python piloto/v4-futuro-1900/construir_roteiro.py

Cada linha numerada vira uma cena: id de 3 dígitos, texto sem os marcadores [Fn], capítulo e bloco de música.
"""

import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from prompts import P, cartao  # noqa: E402

# capítulo do roteiro -> bloco de música (cada bloco tem uma trilha; muda ao longo do vídeo)
BLOCOS = {
    "0": "abertura", "1": "mundo1900",
    "2": "acertos", "3": "erros", "4": "perto",
    "5": "cartoes", "6": "ficcao", "7": "visionarios",
    "8": "porque", "9": "fecho",
}


def main() -> None:
    md = (AQUI / "roteiro.md").read_text(encoding="utf-8").split("## Fontes")[0]
    titulo = md.splitlines()[0].lstrip("# ").strip()
    cenas, cap = [], None
    for linha in md.splitlines():
        if m := re.match(r"^## (\w+)\. (.*)", linha):
            cap = m.group(1)
            nome_cap = m.group(2)
            novo_cap = True
            continue
        if m := re.match(r"^(\d+)\. (.*)", linha):
            n = int(m.group(1))
            texto = re.sub(r"\s*\[F\d+\]", "", m.group(2)).strip()
            cenas.append({
                "id": f"{n:03d}",
                "texto": texto,
                "capitulo": cap,
                "nome_capitulo": nome_cap,
                "bloco": BLOCOS[cap],
                "inicio_capitulo": novo_cap,
                "cartao": cartao(n),
            })
            novo_cap = False
    assert [int(c["id"]) for c in cenas] == list(range(1, len(cenas) + 1)), "numeração com buraco"
    assert len(cenas) == len(P), f"{len(cenas)} cenas no roteiro e {len(P)} prompts"
    (AQUI / "roteiro.json").write_text(
        json.dumps({"titulo": titulo, "cenas": cenas}, indent=1, ensure_ascii=False), encoding="utf-8"
    )
    print(len(cenas), "cenas", sum(len(c["texto"].split()) for c in cenas), "palavras")


if __name__ == "__main__":
    main()
