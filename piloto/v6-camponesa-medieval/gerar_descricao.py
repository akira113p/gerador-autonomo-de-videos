"""Monta a descrição do YouTube (inglês) com capítulos, fontes, créditos e hashtags. Rode depois do montar.py.

  python piloto/v6-camponesa-medieval/gerar_descricao.py                 # versão ACE-Step: tempos.json -> descricao.md
  SUFIXO=_jazz python piloto/v6-camponesa-medieval/gerar_descricao.py    # versão jazz: tempos_jazz.json -> descricao_jazz.md

Regras do YouTube: só as ~150 primeiras letras aparecem na busca (por isso o gancho com as palavras-chave vem
primeiro); capítulos começam em 0:00, são 3 ou mais e duram 10 s ou mais; limite de 5000 caracteres.
"""

import json
import os
from pathlib import Path

AQUI = Path(__file__).resolve().parent

CAPITULOS = {
    "0": "Intro: what does your lord take?",
    "1": "Who you are: a real peasant from 1279",
    "2": "Michaelmas: ploughing, seed and week-work",
    "3": "Winter: your house, your fire, your smoke",
    "4": "Spring: Lady Day and the hungry months",
    "5": "What a peasant really ate and drank",
    "6": "Harvest, and the myth of the 150-day work year",
    "7": "Court day: getting fined by your neighbors",
    "8": "The bills: lord, church and the myth of the first night",
    "9": "Alice, the children and the price of school",
    "10": "How long you lived, and what you owned",
    "11": "The rain: famine, plague and why it all changed",
}

TOPO = """What would your life be like as a medieval peasant? We live one year in an English village around 1300, following a real tenant from a 1279 survey: three days a week of unpaid work for the lord, a fee to marry off a daughter, a tax on dying, and a court that fines you for brewing ale.

Along the way we test three popular myths (the lord's "right of the first night", the 150-day work year, and "everyone died at thirty"), see what a peasant really owned, and watch what happens when the rain starts in 1315. The Black Death comes later, and it changes everything."""

FONTES = """SOURCES
- Hundred Rolls extent of Alwalton, Huntingdonshire (1279), translated in the Fordham Medieval Sourcebook; Warwick University manor documents
- Walter of Henley's Husbandry, translated by Elizabeth Lamond (1890); Dorothea Oschinsky, Walter of Henley and Other Treatises on Estate Management and Accounting (1971)
- University of Nottingham, glossary and guide to manorial records; Morden manorial court rolls (Merton Historical Society); Campop, University of Cambridge, on law in medieval England
- Judith Bennett, Ale, Beer, and Brewsters in England: Women's Work in a Changing World, 1300-1600 (1996)
- Christopher Dyer, Standards of Living in the Later Middle Ages (1989); Dyer, "Changes in Diet in the Late Middle Ages: the Case of Harvest Workers" (1988); Dyer, Making a Living in the Middle Ages (2002)
- Woolgar, Serjeantson and Waldron (eds.), Food in Medieval England: Diet and Nutrition (2006)
- Chris Briggs, on the household possessions of the 14th and 15th century peasantry (coroners' and escheators' records)
- Lucie Laumonier, "Was there school for the medieval peasant?" (Medievalists.net, 2020); Jeremy Goldberg
- Gregory Clark, "Growth or stagnation? Farming in England, 1200-1800", Economic History Review (2018); Allen and Weisdorf, Economic History Review (2010)
- Broadberry, Campbell and van Leeuwen, English medieval population (Warwick working paper)
- Philip Slavin, "The Great Bovine Pestilence and its economic and environmental consequences in England and Wales, 1318-50", Economic History Review (2012), and Experiencing Famine in Fourteenth-Century Britain (2019)
- Statute of Labourers (1351), Avalon Project, Yale; Mark Bailey, Economic History Review (2025)
- The Luttrell Psalter, British Library, Add MS 42130 (c. 1320-1340)
- Dartmoor National Park Authority, medieval longhouses; Alcock and Miles, The Medieval Peasant House in Midland England (2012)

Some details of ordinary life are reconstructed from general accounts; Hugh is based on a real tenant named in the 1279 survey, but his wife, children and daily life are illustrative.
Illustrations: AI-generated in a custom style and checked for anachronisms. Narration: synthetic voice."""

MUSICA = {
    "": "Music: AI-generated (ACE-Step 1.5).",
    "_jazz": 'Music: "No Copyright - Royalty Free 12 hours JAZZ Music" by 741Hz, '
             "https://www.youtube.com/watch?v=HqPsROn8e8k",
}

# as 3 primeiras aparecem acima do título; mais de 15 anulam todas
HASHTAGS = "#MedievalHistory #History #MiddleAges"


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
