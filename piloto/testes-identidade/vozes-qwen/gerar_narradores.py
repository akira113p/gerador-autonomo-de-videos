"""Gera os 6 narradores: amostra de design (a_) e clone num texto novo (b_). Roda no venv-qwen."""

import gc
import json
import sys
import time
from pathlib import Path

import numpy as np
import soundfile as sf
import torch

sys.path.insert(0, "D:/programacao/projetos/videos/v1 geracao de videos/ferramentas")
from qwen_tts_run import BASE_MODEL, DESIGN_MODEL, load, split_sentences  # noqa: E402

DIR = Path(__file__).parent
REF_TEXT = (DIR / "ref.txt").read_text(encoding="utf-8").strip()
TEST_TEXT = (DIR / "teste.txt").read_text(encoding="utf-8").strip()
PERSONAS = json.loads((DIR / "narradores.json").read_text(encoding="utf-8"))
log = {}

torch.manual_seed(42)
model = load(DESIGN_MODEL)
for name, instruct in PERSONAS.items():
    t0 = time.time()
    wavs, sr = model.generate_voice_design(text=REF_TEXT, language="English", instruct=instruct)
    sf.write(DIR / f"a_{name}.wav", wavs[0], sr)
    log[name] = {"design_s": round(time.time() - t0, 1), "design_audio_s": round(len(wavs[0]) / sr, 1)}
    print("design", name, log[name], flush=True)
del model
gc.collect()
torch.cuda.empty_cache()

model = load(BASE_MODEL)
for name in PERSONAS:
    t0 = time.time()
    prompt = model.create_voice_clone_prompt(ref_audio=str(DIR / f"a_{name}.wav"), ref_text=REF_TEXT)
    pieces = []
    for paragraph in [p for p in TEST_TEXT.split("\n\n") if p.strip()]:
        for sentence in split_sentences(paragraph):
            wavs, sr = model.generate_voice_clone(text=sentence, language="English", voice_clone_prompt=prompt)
            pieces += [np.asarray(wavs[0], np.float32), np.zeros(int(sr * 0.15), np.float32)]
        pieces.append(np.zeros(int(sr * 0.45), np.float32))
    wav = np.concatenate(pieces)
    sf.write(DIR / f"b_{name}.wav", wav, sr)
    log[name].update({"clone_s": round(time.time() - t0, 1), "clone_audio_s": round(len(wav) / sr, 1)})
    print("clone", name, log[name], flush=True)

(DIR / "tempos.json").write_text(json.dumps(log, indent=1), encoding="utf-8")
