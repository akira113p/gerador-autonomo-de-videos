"""Monta a descrição do YouTube (inglês) com capítulos, fontes, créditos e hashtags. Rode depois do montar.py.

  python piloto/v3-last-of-us/gerar_descricao.py        # tempos.json -> descricao.md

Regras do YouTube: só as ~150 primeiras letras aparecem na busca (gancho com as palavras-chave primeiro); capítulos
começam em 0:00, são 3 ou mais e duram 10 s ou mais; limite de 5000 caracteres.
"""

import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent

CAPITULOS = {
    "0": "Intro: the last normal day",
    "1": "The fungus is real (sort of)",
    "2": "Day 1: when everything stops",
    "3": "Week 1: everything needs people",
    "4": "Month 1: the quarantine zone",
    "5": "Year 1: what the infected become",
    "6": "Year 1: a normal day",
    "7": "Outside the wall",
    "8": "The silent enemy: medicine runs out",
    "9": "Nature takes it back",
    "10": "Twenty years later",
    "11": "So, would you survive?",
}

TOPO = """What would your life really be like after a zombie apocalypse like The Last of Us? We live it as an ordinary person in the United States: day one, week one, month one, year one, and twenty years later.

Along the way we check the real science and the real disasters behind the story: the fungus that controls ants, the 2003 blackout, life before antibiotics, and how Chernobyl turned into a wildlife refuge.

An independent, fan-made look at the story. Not affiliated with Sony Interactive Entertainment, Naughty Dog or HBO."""

FONTES = """SOURCES
- Hughes et al., "Behavioral mechanisms and morphological symptoms of zombie ants dying from fungal infection", BMC Ecology (2011)
- Robert & Casadevall, "Vertebrate endothermy restricts most fungi as potential pathogens", Journal of Infectious Diseases (2009)
- U.S.-Canada Power System Outage Task Force, Final Report on the August 14, 2003 Blackout (2004); NYISO blackout report
- CDC, "Achievements in Public Health, 1900-1999: Healthier Mothers and Babies", MMWR (1999)
- Deryabina et al., "Long-term census data reveal abundant wildlife populations at Chernobyl", Current Biology (2015)
- Ready.gov (FEMA), emergency water storage guidance
- Thaler, Arnott & Goodale, "Neural correlates of natural human echolocation in early and late blind echolocation experts", PLoS ONE (2011)
- Ward-Perkins, The Fall of Rome and the End of Civilization (2005)
- The Last of Us (Naughty Dog, 2013) and The Last of Us (HBO, 2023) for the story details

Story details are from the game and the series. The real-world facts are from the sources above.
Illustrations: AI-generated in a custom style. Narration: synthetic voice."""

MUSICA = ('Music (calm moments): "No Copyright - Royalty Free 12 hours JAZZ Music" by 741Hz, '
          "https://www.youtube.com/watch?v=HqPsROn8e8k\n"
          'Music (tense moments): "Songs for the Collapse of Society (No AI)" by Joe Mathews | Composer, '
          "https://www.youtube.com/watch?v=J5P4hy7q4TY")

# as 3 primeiras aparecem acima do título; mais de 15 anulam todas
HASHTAGS = "#TheLastOfUs #ZombieApocalypse #Survival"


def mmss(s: float) -> str:
    s = int(s)
    return f"{s // 60}:{s % 60:02d}"


def main() -> None:
    tempos = json.loads((AQUI / "tempos.json").read_text(encoding="utf-8"))
    cenas = json.loads((AQUI / "roteiro.json").read_text(encoding="utf-8"))["cenas"]
    linhas = []
    for c in cenas:
        if c["inicio_capitulo"]:
            t = 0 if c["id"] == "001" else tempos["cenas"][c["id"]]
            linhas.append(f"{mmss(t)} {CAPITULOS[c['capitulo']]}")
    texto = f"{TOPO}\n\nCHAPTERS\n" + "\n".join(linhas) + f"\n\n{FONTES}\n{MUSICA}\n\n{HASHTAGS}\n"
    assert len(texto) <= 5000, f"descrição com {len(texto)} caracteres (limite do YouTube: 5000)"
    (AQUI / "descricao.md").write_text(texto, encoding="utf-8")
    print(texto)


if __name__ == "__main__":
    main()
