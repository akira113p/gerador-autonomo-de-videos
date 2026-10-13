"""Monta a descrição do YouTube (inglês) com capítulos, fontes, créditos e hashtags. Rode depois do montar.py.

  python piloto/v4-futuro-1900/gerar_descricao.py                 # ACE-Step: tempos.json -> descricao.md
  SUFIXO=_jazz python piloto/v4-futuro-1900/gerar_descricao.py    # versão jazz: tempos_jazz.json -> descricao_jazz.md

Regras do YouTube: só as ~150 primeiras letras aparecem na busca (por isso o gancho com as palavras-chave vem
primeiro); capítulos começam em 0:00, são 3 ou mais e duram 10 s ou mais; limite de 5000 caracteres.
"""

import json
import os
from pathlib import Path

AQUI = Path(__file__).resolve().parent

CAPITULOS = {
    "0": "Intro: the December 1900 magazine",
    "1": "The world of 1900",
    "2": "Watkins' predictions: what he got right",
    "3": "Watkins' predictions: what he got wrong",
    "4": "Weirdly close",
    "5": "The French cards: En l'an 2000",
    "6": "Fiction: the credit card and streaming",
    "7": "The visionaries: Wells, Tesla and Edison",
    "8": "Why they were wrong",
    "9": "What about us?",
}

TOPO = """How people in 1900 imagined the year 2000: we read the famous 1900 article "What May Happen in the Next Hundred Years" and keep score. Right, wrong, or weirdly close?

In December 1900, John Elfreth Watkins Jr. published his predictions in the Ladies' Home Journal. Some are eerily accurate (wireless phones, photos sent across the world, air conditioning, ready-cooked meals), others are gloriously wrong (strawberries as big as apples, no letters C, X and Q). Along the way: the French "En l'an 2000" cards with flying firemen and a whale-drawn bus, Edward Bellamy's 1888 "credit card", E. M. Forster's 1909 story of a world of screens, and the visions of H. G. Wells, Tesla and Edison."""

FONTES = """SOURCES
- John Elfreth Watkins Jr., "What May Happen in the Next Hundred Years", Ladies' Home Journal, December 1900
- CDC/NCHS, United States Life Tables (life expectancy); U.S. Census (2000 population, housing and telephones in 1900)
- Federal Highway Administration, State Motor Vehicle Registrations 1900-1995
- Smithsonian National Air and Space Museum (Wright brothers, 1903)
- Official report of the 1900 Paris Exposition (BnF Gallica)
- Nobel Prize biography of Guglielmo Marconi
- Willis Carrier and the 1902 air conditioning system (ASME landmark; Carrier Corporation)
- The Henry Ford museum (Model T, 1908)
- New York Times, 1906 (Simplified Spelling Board and President Roosevelt)
- NCD-RisC, eLife 2016 (height in the 20th century)
- Isaac Asimov, Futuredays: A Nineteenth-Century Vision of the Year 2000 (1986); BnF Gallica (Villemard series)
- Edward Bellamy, Looking Backward (1888), Project Gutenberg
- E. M. Forster, "The Machine Stops" (1909)
- Rudyard Kipling, "With the Night Mail" (1905)
- H. G. Wells, "The Land Ironclads" (1903) and The World Set Free (1914); Imperial War Museum
- Weart and Szilard, Leo Szilard: His Version of the Facts (1978)
- Nikola Tesla interview, Collier's, 30 January 1926
- Thomas Edison interview, Miami Metropolis, October 1911

Illustrations: AI-generated in a custom style and checked for anachronisms. Narration: synthetic voice."""

MUSICA = {
    "": "Music: AI-generated (ACE-Step 1.5).",
    "_jazz": 'Music: "No Copyright - Royalty Free 12 hours JAZZ Music" by 741Hz, '
             "https://www.youtube.com/watch?v=HqPsROn8e8k",
}

# as 3 primeiras aparecem acima do título; mais de 15 anulam todas
HASHTAGS = "#History #Future #1900"


def mmss(s: float) -> str:
    s = int(s)
    return f"{s // 60}:{s % 60:02d}"


def main() -> None:
    sufixo = os.environ.get("SUFIXO", "")
    tempos = json.loads((AQUI / f"tempos{sufixo}.json").read_text(encoding="utf-8"))
    cenas = json.loads((AQUI / "roteiro.json").read_text(encoding="utf-8"))["cenas"]
    linhas = []
    for c in cenas:
        if c["inicio_capitulo"]:
            t = 0 if c["id"] == "001" else tempos["cenas"][c["id"]]
            linhas.append(f"{mmss(t)} {CAPITULOS[c['capitulo']]}")
    texto = f"{TOPO}\n\nCHAPTERS\n" + "\n".join(linhas) + f"\n\n{FONTES}\n{MUSICA[sufixo]}\n\n{HASHTAGS}\n"
    assert len(texto) <= 5000, f"descrição com {len(texto)} caracteres (limite do YouTube: 5000)"
    (AQUI / f"descricao{sufixo}.md").write_text(texto, encoding="utf-8")
    print(texto)


if __name__ == "__main__":
    main()
