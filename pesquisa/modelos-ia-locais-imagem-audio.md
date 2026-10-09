---
tags: [pesquisa, modelos-locais, imagem, audio, hardware]
data: 2026-10-08
hardware: RTX 4060 Laptop 8 GB VRAM, 16 GB RAM
---

# Modelos de IA locais e grátis (imagem e áudio) para a RTX 4060 de 8 GB

Data da pesquisa: 2026-10-08. Orçamento do canal: US$ 0 (ver [[../docs/decisoes]]). Canal monetizado: só licença que permite uso comercial.

Legenda: [verificado] = página oficial (Hugging Face, GitHub do projeto, API do HF) diz isso; [blog] = só blogs de terceiros, que divergem entre si nos números de VRAM; [não verificado] = não confirmei.

Nada foi testado na máquina. Tempos e VRAM reais exigem teste. A GPU já usa ~2,9 GB com o sistema, então sobram ~5 GB: fechar o Chrome antes de gerar.

## Lista final recomendada

| Função | 1ª escolha | Alternativas | Evitar |
|---|---|---|---|
| Imagem | Z-Image Turbo (int8/FP8/GGUF) | SDXL + LoRA de estilo; FLUX.1 schnell GGUF | FLUX.1 dev, FLUX.2 dev (não comercial) |
| Voz, narração EN | Kokoro-82M | Piper (já integrado no OpenMontage, qualidade menor) | XTTS-v2, F5-TTS, Fish Audio S2 (não comercial) |
| Voz, dublagem/clonagem | Chatterbox Multilingual, Qwen3-TTS | Kokoro (sem clonagem) | idem |
| Transcrição | Parakeet TDT v3 (EN) | Whisper large-v3-turbo (muitos idiomas) | — |
| Música | Biblioteca livre (YouTube Audio Library, Pixabay) | ACE-Step 1.5 turbo | MusicGen (pesos não comerciais) |

## Imagem

- **Z-Image Turbo**: Apache 2.0, 6B parâmetros, 8 passos. [verificado] https://huggingface.co/Tongyi-MAI/Z-Image-Turbo. O card diz que cabe "confortavelmente em 16 GB"; para 8 GB seriam as versões FP8/GGUF da comunidade [blog]. Pontos fracos: texto dentro da imagem e poucos LoRAs [blog].
- **SDXL** (Juggernaut XL, RealVisXL, DreamShaper XL): roda folgado em 8 GB, milhares de LoRAs, prompt adherence inferior ao FLUX [blog]. Escolha quando o canal precisar de um estilo visual específico (gravura, óleo).
- **FLUX.1 schnell** GGUF: Apache 2.0, segue melhor o prompt. [verificado] licença; VRAM com quantização varia de 7 a 12 GB conforme a fonte [blog].
- **FLUX.1 dev**: licença não comercial. Evitar.
- **FLUX.2 klein 4B**: Apache 2.0, mas ~13 GB de VRAM segundo a BFL, então não cabe sem quantização. A versão 9B é não comercial. [verificado] https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence
- Fontes de blog: https://easywithai.medium.com/best-local-ai-image-models-in-2026-6ab39649030e , https://localaimaster.com/blog/sdxl-vs-flux-local , https://botmonster.com/ai/best-local-image-generation-models-2026/

### O que no OpenMontage não serve para esta GPU
- `tools/_comfyui/workflows/flux2-txt2img.json` usa `flux2-dev-nvfp4` (32B, NVFP4 é para RTX 50, licença dev não comercial). Não usar na 4060.
- `tools/graphics/qwen_image_21.py` declara 16 GB de VRAM e 32 GB de RAM.
- `tools/graphics/local_diffusion.py` tem SD 2.1 base como padrão (fraco). Trocar por SDXL.

## Voz

| Modelo | Clona voz | Idiomas | Licença |
|---|---|---|---|
| Kokoro-82M | Não (54 vozes prontas) | 8 (en, es, fr, ja, zh, hi, it, pt) | Apache 2.0 |
| Chatterbox | Sim | 23 | MIT |
| Qwen3-TTS 0,6B / 1,7B | Sim (~3 s de áudio) | 10, inclui pt-BR | Apache 2.0 |

- Kokoro: [verificado] https://huggingface.co/hexgrad/Kokoro-82M (Apache 2.0, 82M, 54 vozes). Que seja "#1 na TTS Arena" só aparece em blogs, não confirmei.
- Chatterbox e Qwen3-TTS: licença e idiomas [blog] https://ocdevel.com/blog/20250720-tts , https://localaimaster.com/blog/kokoro-vs-xtts-vs-chatterbox . Pacote de português do Brasil do Chatterbox é alegação da Resemble https://resemble.ai/learn/models/chatterbox-multilingual . Docs do Qwen3-TTS listam pt-BR https://www.mintlify.com/QwenLM/Qwen3-TTS/concepts/languages
- Não achei teste independente comparando os três em português do Brasil. **Antes de escolher a voz da dublagem, fazer teste cego com o mesmo roteiro nos três.**
- Não comerciais, evitar: XTTS-v2 (CPML), Fish Audio S2 (licença de pesquisa), Voxtral (CC BY-NC) [blog]. F5-TTS: pesos não comerciais, não reconferi.

## Transcrição

- Inglês: Parakeet TDT / Canary têm WER menor (~6–7% no Open ASR Leaderboard contra ~7,8% do Whisper large-v3-turbo) e são muito mais rápidos [blog]. https://northflank.com/blog/best-open-source-speech-to-text-stt-model-in-2026-benchmarks , https://codesota.com/speech/stt-leaderboard
- Muitos idiomas: Whisper large-v3-turbo (99 idiomas, contra 25 do Parakeet v3) [blog]. Útil para a dublagem.
- Para a legenda do canal, o roteiro já existe, então a transcrição importa pouco.
- O OpenMontage integra faster-whisper e WhisperX (`tools/analysis/transcriber.py`).

## Música

- **ACE-Step 1.5**: MIT. Variante 2B turbo recomendada para 6–8 GB; a XL (4B) exige ≥12 GB. [verificado] https://github.com/ACE-Step/ACE-Step-1.5 . Relato de terceiros de que roda "extremamente lento" em 8 GB [blog]. Testar antes de depender.
- O OpenMontage usa a v1 (3,5B) via ComfyUI (`tools/audio/comfyui_music.py`, `ace-step-1-t2a.json`).
- Biblioteca livre é mais segura e dá menos trabalho. O OpenMontage tem `pixabay_music.py`.
- Stable Audio Open (efeitos, ~47 s, licença grátis abaixo de US$ 1 milhão de receita) e MusicGen (não comercial): [não verificado], vêm da minha memória.

## Peso em disco

Tamanhos dos arquivos pela API do Hugging Face [verificado], exceto onde há "~".

| Modelo | Arquivos | Total |
|---|---|---|
| Z-Image Turbo (int8) | modelo 6,2 GB, text encoder Qwen3-4B fp8 5,6 GB, VAE 0,3 GB | ~12,2 GB |
| Z-Image Turbo (bf16) | 12,3 GB + text encoder 8,0 GB | ~20,7 GB (não cabe na VRAM) |
| SDXL base fp16 | checkpoint único 6,9 GB (+ LoRAs) | ~7 GB |
| FLUX.1 schnell GGUF Q4_K_S | 6,8 GB + T5-XXL fp8 ~4,9 GB + CLIP-L ~0,25 GB + VAE ~0,3 GB | ~12,3 GB |
| Kokoro-82M | 0,33 GB | ~0,4 GB |
| Chatterbox multilíngue | t3 2,1 GB + s3gen 1,1 GB + extras | ~3,3 GB |
| Qwen3-TTS 1,7B / 0,6B | 3,9 + 0,7 GB / 1,8 + 0,7 GB | ~4,5 GB / ~2,5 GB |
| Whisper large-v3-turbo | | ~1,6 GB (estimado) |
| Parakeet TDT 0.6B v3 | 2,5 GB (GGUF q8: 0,7 GB) | 2,5 GB |
| ACE-Step 1.5 turbo | DiT 4,8 + LM 1,7B 3,7 + embedding 1,2 + VAE 0,3 | ~10 GB (~7 GB com LM 0,6B) |

- Tudo: ~54 GB de modelos, ~65 GB com o ambiente PyTorch/CUDA (5–8 GB) e ComfyUI.
- Mínimo (Z-Image, Kokoro, Chatterbox, Whisper): ~17,5 GB, ~25 GB com ambiente.
- Os repositórios do HF têm arquivos duplicados (`.pt` e `.safetensors`). Baixar só o necessário.
- A versão `nvfp4` do Z-Image (4,5 GB) é para RTX 50; na 4060 usar int8 ou GGUF.

## Lacunas
- Nenhum modelo foi testado na máquina: tempo por imagem, tempo real da voz e VRAM de pico são desconhecidos.
- Qualidade em português do Brasil dos três TTS: sem comparação independente.
- Os números de VRAM dos blogs divergem; confiar nos de página oficial.

## Próximo passo sugerido
Instalar Z-Image Turbo (ComfyUI) e Kokoro, medir tempo e VRAM reais, e só então decidir se SDXL, Qwen3-TTS e ACE-Step entram.
