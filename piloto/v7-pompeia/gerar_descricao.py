"""Monta a descrição do YouTube (inglês) com capítulos, fontes, créditos e hashtags. Rode depois do montar.py.

  python piloto/v7-pompeia/gerar_descricao.py                 # versão ACE-Step: tempos.json -> descricao.md
  SUFIXO=_jazz python piloto/v7-pompeia/gerar_descricao.py    # versão jazz: tempos_jazz.json -> descricao_jazz.md

Regras do YouTube: só as ~150 primeiras letras aparecem na busca (por isso o gancho com as palavras-chave vem
primeiro); capítulos começam em 0:00, são 3 ou mais e duram 10 s ou mais; limite de 5000 caracteres.
"""

import json
import os
from pathlib import Path

AQUI = Path(__file__).resolve().parent

CAPITULOS = {
    '0': 'Intro: the last day of your city',
    '1': 'Which day is it, really?',
    '2': 'Before sunrise: the bakery',
    '3': 'Morning: the walls talk',
    '4': 'Mid-morning: money, freedmen and a six-year-old councillor',
    '5': 'Noon: lunch at the snack bar',
    '6': 'Early afternoon: the arena',
    '7': "One o'clock: the cloud",
    '8': 'Afternoon: a rain of stones',
    '9': 'Night: the darkness',
    '10': 'The next morning',
    '11': 'What Pompeii teaches us',
}

TOPO = """What would your life be like in Pompeii on the last day? We spend the final twenty-four hours of the Roman town hour by hour, as Felix, a freed slave and baker, using Pliny the Younger's two eyewitness letters for the eruption and the town's own walls (election posters, graffiti, snack bars, bakeries) for everyday life.

Along the way: why the date of the eruption is still debated (August or October?), what a Roman bakery really looked like, the "pizza" painting that wasn't pizza, a six-year-old city councillor, gladiator fans who started a riot, and what we do and do not know about who escaped. No bodies and no plaster casts are drawn."""

FONTES = """SOURCES
- Pliny the Younger, Letters 6.16 and 6.20 (to Tacitus), on the eruption of Vesuvius in AD 79
- Parco Archeologico di Pompei: the 2018 charcoal inscription and the 2024 test of charcoal durability, the 2020 thermopolium of Regio V, the 2023 bakery with enslaved workers and the flatbread painting, the August 2025 announcements (victims, survivors, reoccupation)
- Sigurdsson et al. (1985), "The eruption of Vesuvius in A.D. 79", National Geographic Research; Luongo et al. (2003), Journal of Volcanology and Geothermal Research
- Strabo, Geography 5.4.8; Tacitus, Annals 14.17 (the riot of AD 59)
- Mary Beard, "Myths of Vesuvius" and Pompeii: The Life of a Roman Town; Zuchtriegel (2024) on the date; Foss (2022) on the manuscripts of Pliny
- CIL X 846 (the temple of Isis and the six-year-old Numerius Popidius Celsinus); the wax tablets of Caecilius Iucundus
- Eric Poehler, The Traffic Systems of Pompeii (2017); Smithsonian Magazine and National Geographic coverage of the bakery, the thermopolium and the House of the Vettii
- Pompeii Online (election notices) and World History Encyclopedia (graffiti and gladiator notices)
- USGS Volcano Hazards Program (glossary: Plinian eruption, pumice, pyroclastic surges)

Some details of ordinary life are reconstructed from general accounts; Felix and his bakery are fictional. This video draws no bodies and no plaster casts.
Illustrations: AI-generated in a custom style and checked for anachronisms. Narration: synthetic voice."""

MUSICA = {
    "": "Music: AI-generated (ACE-Step 1.5).",
    "_jazz": 'Music: "No Copyright - Royalty Free 12 hours JAZZ Music" by 741Hz, '
             "https://www.youtube.com/watch?v=HqPsROn8e8k",
}

# as 3 primeiras aparecem acima do título; mais de 15 anulam todas
HASHTAGS = "#Pompeii #History #AncientRome"


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
