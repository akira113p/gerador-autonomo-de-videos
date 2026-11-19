---
tags: [pesquisa, imagem, referencia, edicao, comfyui, flux2-klein]
data: 2026-10-19
hardware: RTX 4060 Laptop 8 GB VRAM (~5 GB úteis), 16 GB RAM
---

# Imagem local com imagens de referência (personagem e estilo)

Data da pesquisa: 2026-10-19. Nada foi instalado, baixado ou rodado. Tempos são estimativas por escala, não medições.

Legenda: [verificado] = página oficial (Hugging Face, API do HF, docs da BFL/ComfyUI) ou o código/arquivos locais dizem isso; [estimativa] = conta minha; [não verificado] = não deu para confirmar sem testar.

Fluxo pedido: ~12 a 15 imagens do primeiro minuto vêm do ChatGPT; as ~150 a 200 restantes saem da IA local usando essas imagens como referência (personagem bonequinho + estilo cartoon). Regra: só licença que permite uso comercial.

## Resposta curta

- **Opção principal: FLUX.2 [klein] 4B distilled, fp8, edição com 2 referências no ComfyUI.** Apache 2.0, 4 passos, até 4 imagens de referência, e a versão local do ComfyUI (0.39.0) já tem tudo. Download novo: **~4,4 GB** (modelo fp8 4,07 GB + VAE 0,34 GB). O text encoder é o mesmo Qwen3-4B que o Z-Image usa, e o `qwen_3_4b_fp8_mixed.safetensors` já instalado deve servir.
- **Tempo esperado: 30 a 60 s por imagem 1344x768 com 2 referências** [estimativa], contra 68 s do Z-Image Turbo hoje. Isso dá ~2 a 3,5 h de GPU para 200 imagens.
- **Reserva (instalação):** o mesmo klein 4B em GGUF Q8_0 (4,3 GB) ou Q4_K_M (2,6 GB) com o nó ComfyUI-GGUF, se o fp8 der erro. **Reserva (técnica):** SDXL + IP-Adapter Plus, mais fraco para manter o personagem. Z-Image Turbo img2img serve só como complemento (variar uma imagem que já existe).
- **Não servem nesta máquina:** Qwen-Image-Edit (13 GB no menor quant útil), Z-Image Edit/Omni (não lançados), FLUX.2 klein 9B (licença não comercial), FLUX.1 Kontext dev (não comercial).

## 1. FLUX.2 [klein] 4B

### Licença [verificado]
- 4B (distilled e base): **Apache 2.0**. O `LICENSE.md` do repositório é o texto padrão da Apache 2.0, sem cláusula extra além da marca registrada (seção 6: não usar o nome/logo FLUX/BFL de forma que sugira endosso). https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/main/LICENSE.md
- As variantes fp8 e nvfp4 do 4B também são Apache 2.0 (API do HF: `black-forest-labs/FLUX.2-klein-4b-fp8`, `-base-4b-fp8`, `-4b-nvfp4`).
- **9B é FLUX Non-Commercial License. Não usar.** (também `klein-9b-kv`, "license: other", gated). Blog: https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence
- O card pede filtros de NSFW/conteúdo protegido e menciona marca d'água de pixel e C2PA no código de inferência deles; o uso no ComfyUI não exige isso, mas vale saber.

### Edição com uma e várias referências [verificado]
- Um modelo só faz texto para imagem, edição com 1 referência e edição com várias. Doc da BFL: **klein aceita até 4 imagens de referência** (`input_image` a `input_image_4`). https://docs.bfl.ai/guides/prompting_unified_reference
- No prompt, as imagens são chamadas pela posição: "image 1", "image 2" (doc de edição da BFL e o template oficial do ComfyUI: "stylize the handbag in image1 with the colours and logo from image 2"). https://docs.bfl.ai/flux_2/flux2_image_editing
- Klein não reescreve o prompt ("o que você escreve é o que o modelo recebe"): escrever em prosa, descritivo, em inglês, e fechar com "Style: ... Mood: ..." para manter estética (BFL).
- Texto dentro da imagem sai impreciso (card). Texto/número/mapa continua sendo desenhado em código (`cartoes.py`).

### Arquivos necessários [verificado pela API do HF]

| Arquivo | Tamanho | URL | Pasta |
|---|---|---|---|
| `flux-2-klein-4b-fp8.safetensors` (distilled, **principal**) | 4,07 GB | https://huggingface.co/black-forest-labs/FLUX.2-klein-4b-fp8/resolve/main/flux-2-klein-4b-fp8.safetensors | `C:/ai-local/comfyui/models/diffusion_models/` |
| `flux2-vae.safetensors` | 0,336 GB | https://huggingface.co/Comfy-Org/flux2-klein-4B/resolve/main/split_files/vae/flux2-vae.safetensors | `models/vae/` |
| `qwen_3_4b_fp8_mixed.safetensors` | 5,63 GB | **já instalado** (`models/text_encoders/`) | — |
| `flux-2-klein-base-4b-fp8.safetensors` (base, opcional) | 4,09 GB | https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4b-fp8/resolve/main/flux-2-klein-base-4b-fp8.safetensors | `models/diffusion_models/` |
| `flux-2-klein-4b.safetensors` (bf16, não precisa) | 7,75 GB | repositório `Comfy-Org/flux2-klein-4B`, `split_files/diffusion_models/` | — |
| `qwen_3_4b.safetensors` (bf16, só se o fp8_mixed falhar) | 8,04 GB | https://huggingface.co/Comfy-Org/flux2-klein-4B/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors | `models/text_encoders/` |

Pontos que contam:
- **O `ae.safetensors` instalado é o VAE do FLUX.1/Z-Image (16 canais). Klein usa o VAE do FLUX.2 (`flux2-vae.safetensors`). Não são intercambiáveis; baixar o novo.** O `ae.safetensors` do Z-Image vem do FLUX.1. Os repositórios `Comfy-Org/flux2-dev` e `Comfy-Org/flux2-klein-4B` têm cada um um `flux2-vae.safetensors` com tamanho e hash ligeiramente diferentes (336.213.556 e 336.211.292 bytes); o template oficial do klein aponta para o do `flux2-dev`. Usar o do `flux2-klein-4B` e, se der erro, trocar pelo do `flux2-dev` [não verificado qual é o canônico].
- **Text encoder é o Qwen3-4B**, o mesmo do Z-Image: o `qwen_3_4b.safetensors` (8,04 GB) do repositório `Comfy-Org/flux2-klein-4B` e o do `Comfy-Org/z_image_turbo` têm o mesmo tamanho e o **mesmo sha256** (`6c671498...edfc5a`). [verificado]
- Reaproveitar o `qwen_3_4b_fp8_mixed.safetensors`: o código local confirma que o `CLIPLoader` com tipo `flux2` detecta Qwen3-4B pela mesma rotina e monta `klein_te(... model_type="qwen3_4b")` (`comfy/sd.py`, linhas ~1937-1939). Deve carregar. **Não verificado:** se o fp8 do encoder muda a qualidade de edição (os templates oficiais usam o bf16 de 8 GB). Testar com o fp8_mixed primeiro; se o resultado vier estranho, baixar o bf16 (+8 GB) — o que cabe nos 77 GB livres do C:.
- `qwen_3_4b_fp4_flux2.safetensors` (3,85 GB) é NVFP4, formato de RTX 50. Na 4060 não usar.
- O nvfp4 do modelo (2,46 GB) também é para RTX 50. Não usar.
- **Download total para a opção principal: ~4,4 GB** (ou ~12,4 GB se precisar do encoder bf16).

### Versão do ComfyUI [verificado localmente]
- Local: **0.39.0** (`comfyui_version.py`). A doc do ComfyUI só diz "atualize para a versão mais recente" sem número mínimo; o suporte a Flux2/klein já está no código local: `comfy/supported_models.py` (`class Flux2`, detecta `qwen3_4b` e `qwen3_8b`), `comfy/sd.py` (`CLIPType.FLUX2`), `comfy_extras/nodes_flux.py` (`EmptyFlux2LatentImage`, `Flux2Scheduler`, `FluxKVCache`, `FluxKontextMultiReferenceLatentMethod`), `comfy_extras/nodes_edit_model.py` (`ReferenceLatent`).
- Os templates oficiais já estão instalados no venv: `C:/ai-local/venv-comfy/Lib/site-packages/comfyui_workflow_templates_json/templates/image_flux2_klein_image_edit_4b_distilled.json` (e `..._4b_base.json`). Também há o blueprint `C:/ai-local/comfyui/blueprints/Image Edit (Flux.2 Klein 4B).json`. No ComfyUI: menu Templates > "Flux.2 Klein 4B image edit (distilled)". Não precisa escrever o workflow do zero.
- **Não há suporte a GGUF no núcleo** (nenhuma ocorrência de "gguf" em `comfy/`, `comfy_extras/`, `nodes.py`) e `custom_nodes/` só tem exemplos. O fallback GGUF exige instalar o nó ComfyUI-GGUF (custom node de terceiros; conferir a licença do repositório antes).

### Nós do workflow oficial (distilled) [verificado nos JSON locais]
Dos templates do ComfyUI (subgrafo "Image Edit (Flux.2 Klein 4B Distilled)"):
`UNETLoader` (fp8, `default`) / `CLIPLoader` (Qwen3-4B, tipo `flux2`) / `VAELoader` (flux2-vae) → `LoadImage` ×N → `ImageScaleToTotalPixels` (nearest-exact, 1 MP) → `VAEEncode` → `ReferenceLatent` encadeado (um por imagem, sobre o condicionamento do `CLIPTextEncode`) → `ConditioningZeroOut` (negativo) → `CFGGuider` (**cfg 1**) + `KSamplerSelect` (**euler**) + `Flux2Scheduler` (**4 passos**, largura, altura) + `EmptyFlux2LatentImage` + `RandomNoise` → `SamplerCustomAdvanced` → `VAEDecode` → `SaveImage`.
A versão base usa 20 passos e cfg 5 com prompt negativo de verdade (blueprint local).

### VRAM e tempo
- BFL: "cabe em ~13 GB" no bf16 (RTX 3090/4070 para cima). [verificado] Isso é a conta do bf16 inteiro na GPU.
- Doc do ComfyUI, medido numa **RTX 5090**: distilled 4B ~1,2 s e 8,4 GB de VRAM; base 4B ~17 s e 9,2 GB. [verificado, mas GPU muito mais rápida; não é o nosso caso]. A página de template do ComfyUI diz "~8 GB". Nenhum valor dessas fontes é de edição com referência na 4060.
- fp8 corta o modelo para 4,07 GB e é "até 1,6x mais rápido" que o bf16 (blog BFL, medido em RTX 50). A 4060 (Ada) tem tensor cores de fp8, então deve ganhar algo, mas isso **não foi confirmado**.
- Blogs divergem 3x a 6x para a 4060 em texto para imagem 1024x1024, 4 passos: de 5 s a 15-30 s. [blog, não confiável]
- **Cabe em 8 GB?** O modelo (4,07 GB) mais o encoder (5,6 GB) não ficam juntos na VRAM; o ComfyUI carrega o encoder, codifica o prompt e libera, e o gerenciador de memória descarrega pesos para a RAM (a opção dynamic VRAM é padrão neste ComfyUI, `comfy/cli_args.py`). Com ~5 GB úteis, a pressão vem das ativações: cada referência de 1 MP soma ~4.096 tokens à sequência (saída 1344x768 = ~4.032 tokens). Com 2 referências a sequência fica ~3x maior que no texto para imagem. Deve rodar com offload parcial; **a memória de pico não foi medida**. RAM de 16 GB: encoder + modelo em RAM (~10 GB) cabe, mas feche navegador e Chrome.
- **Estimativa de tempo** [estimativa por escala sobre os 68 s do Z-Image Turbo, 6B, 8 passos]: klein 4B tem ~2/3 dos parâmetros e metade dos passos, então texto para imagem em torno de 20-25 s; cada referência de 1 MP custa cerca de +50-70% do tempo de computação. Referências em ~0,5 MP e o nó `FluxKVCache` (guarda K/V das referências e só calcula uma vez; nó experimental, existe no código local) reduzem isso. Faixa a planejar: **30 a 60 s por imagem com 2 referências, 20 a 35 s com 1**. 200 imagens = 2 a 3,5 h de GPU, com o PC ocioso.

### Detalhes de uso que importam para o canal
- Resolução de saída: 1344x768 (múltiplo de 16, ~1 MP) vale. No template, a saída copia o tamanho da imagem 1 (`GetImageSize`); para fixar 16:9, trocar por números fixos em `EmptyFlux2LatentImage` e `Flux2Scheduler`.
- Referências: personagem em imagem 1 (folha de personagem em fundo liso, ou o frame do ChatGPT em que ele aparece mais claro), estilo/cenário em imagem 2. Reduzir cada uma para 0,5 a 0,7 MP no `ImageScaleToTotalPixels` (valor 0.5-0.7 no último parâmetro de megapixels) para ganhar tempo.
- Cenários mais escuros nos vídeos sérios: pedir no prompt ("dim torchlight", "dark stone interior"), mantendo a imagem 2 de estilo na mesma paleta.
- Seeds: `RandomNoise` em "fixed" para refazer uma imagem sem mudar o resto.

## 2. Z-Image Turbo img2img (já instalado)

[Não verificado em teste; é o que o ComfyUI faz por construção.] Montagem: `LoadImage` → `VAEEncode` (com o `ae.safetensors` atual) → `KSampler` com a mesma configuração do txt2img (8 passos, cfg 1) e **denoise < 1**.
- Denoise ~0,3-0,45: mantém composição e cores, muda detalhe e acabamento. Serve para "limpar" uma imagem, igualar paleta, ou refazer mão/rosto de uma imagem quase certa.
- Denoise ~0,5-0,65: o prompt já manda mais; ainda segue o layout geral, troca objetos.
- Denoise > 0,7: perde a composição; é quase txt2img.
- **Limite principal: não há "referência de personagem".** O modelo só vê a imagem como ponto de partida de ruído, não como identidade. Não transporta o bonequinho para outra cena nem muda a pose/cena. Ele ajuda só a variar uma imagem que já tem o personagem na pose e posição desejadas.
- O núcleo do ComfyUI tem os blueprints "Canny/Depth/Pose to Image (Z-Image-Turbo)" e "ControlNet (Z-Image-Turbo)" (`C:/ai-local/comfyui/blueprints/`): controlam pose/contorno, não identidade; precisam de modelos extras (não verificei tamanho e licença deles).
- Quando serve: refinamento e variação, ou como segundo passo depois do klein.

## 3. Z-Image Edit, Z-Image Omni, Z-Image Base

- **Z-Image (Base, `Tongyi-MAI/Z-Image`)**: lançado em 2026-01-27, Apache 2.0, 50 passos com CFG. Repackaging do ComfyUI: bf16 12,31 GB, **int8_convrot 6,2 GB**, mesmo `qwen_3_4b` e `ae.safetensors`. [verificado: API do HF e README do GitHub] É texto para imagem; não edita com referência. Seu valor aqui seria como base melhor para treinar LoRA de estilo (mais variável que o Turbo), mas isso não foi testado.
- **Z-Image-Omni-Base e Z-Image-Edit: ainda "To be released"** na tabela de modelos do repositório oficial https://github.com/Tongyi-MAI/Z-Image, e a organização `Tongyi-MAI` no HF só lista Z-Image-Turbo, Z-Image, MAI-UI-8B/2B e MAI-Gym-9B (API em 2026-10-19). Resultados com "Z-Image-Edit" na busca do HF são de terceiros (`Anjoe/z-image-edit`, `zenlm/zen-image-edit`), não o modelo oficial; não usar sem examinar licença e origem.
- O ComfyUI local já tem o nó `TextEncodeZImageOmni` (`comfy_extras/nodes_zimage.py`, aceita até 3 imagens e `image_encoder`), ou seja, o código existe para quando o Omni sair. **Sem pesos, não há como usar hoje.** Reavaliar quando o repositório oficial publicar. Tamanho e licença do Omni/Edit: não existem para confirmar.

## 4. Qwen-Image-Edit (2509 / 2511) em GGUF

- Licença: **Apache 2.0** (`Qwen/Qwen-Image-Edit-2509`, `-2511`, `Comfy-Org/Qwen-Image-Edit_ComfyUI`, `unsloth/Qwen-Image-Edit-2511-GGUF`). [verificado]
- Tamanhos GGUF (`unsloth/Qwen-Image-Edit-2511-GGUF`; `QuantStack/Qwen-Image-Edit-2509-GGUF` é parecido): Q2_K 7,5 GB, Q3_K_M 9,9 GB, **Q4_K_M 13,2 GB**, Q5_K_M 15,0 GB, Q8_0 21,8 GB. Os fp8 e int8 do Comfy-Org têm ~20,5 GB. [verificado]
- Mais o text encoder Qwen2.5-VL 7B: fp8_scaled 9,38 GB (nvfp4 6,11 GB é para RTX 50) e o VAE 0,25 GB (`Comfy-Org/Qwen-Image_ComfyUI`). [verificado]
- **Não cabe de forma útil:** ~5 GB de VRAM útil e 16 GB de RAM contra 13 GB de modelo + 9 GB de encoder ⇒ troca para o disco a cada imagem. Q2_K e Q3 degradam. Tempo: minutos por imagem, mesmo com LoRA "Lightning" de 4 passos [estimativa; não medido]. É o modelo mais forte em manter personagem, mas só vale se o usuário alugar GPU, o que contraria o orçamento de US$ 0. Descartado.
- Exigiria também o nó ComfyUI-GGUF (não há GGUF no núcleo).

## 5. Outras opções

| Opção | Licença | Cabe? | Veredito |
|---|---|---|---|
| **SDXL + IP-Adapter Plus** (`h94/IP-Adapter`) | Pesos do IP-Adapter Apache 2.0; SDXL base: OpenRAIL++ (uso comercial permitido, com restrições de uso) [verificado] | Sim: SDXL ~7 GB fp16 em 8 GB sem problema; `ip-adapter-plus_sdxl_vit-h.safetensors` 0,85 GB; encoder CLIP ViT-H (`models/image_encoder/model.safetensors`) 2,53 GB | **Reserva técnica.** Transfere estilo e traços gerais, mas identidade exata do bonequinho (cabeça redonda, contorno, proporção) tende a derivar. Evitar as variantes "face"/FaceID: costumam depender de InsightFace, cujos pesos têm restrição de uso não comercial [não verificado]; para bonequinho nem fazem sentido. Exige nós de terceiros (ComfyUI_IPAdapter_plus) [não verificado] |
| **LoRA do personagem/estilo** treinada com as imagens do ChatGPT | Depende do modelo base; o resultado é do usuário | Não treina nesta máquina: a BFL diz mínimo de 12 GB de VRAM e 32 GB de RAM para klein 4B base, outras fontes dizem 24 GB (conflito). Com 8 GB + 16 GB RAM: **não viável** [não testado]. Treino em GPU grátis na nuvem (Colab/Kaggle) é uma opção sem custo, mas depende de termos e limites de tempo [não verificado] | Melhor consistência a longo prazo, caro de fazer. Considerar só se a edição por referência falhar. Precisa de 15-40 imagens do mesmo estilo, o que o primeiro minuto não dá (12-15) sem aumentar o conjunto |
| **OmniGen2** (`OmniGen2/OmniGen2`) | Apache 2.0 [verificado] | `omnigen2_fp16.safetensors` 7,93 GB + `qwen_2.5_vl_fp16.safetensors` 7,51 GB (Comfy-Org). Sem quant oficial; pesado e lento | Descartado: mais pesado que o klein e, pela minha leitura, pior em consistência [não testado] |
| **Step1X-Edit** (v1p2) | Apache 2.0 [verificado] | 12,4 B de parâmetros no transformer, mais um VLM | Não cabe. Descartado |
| **Mage-Flow-Edit** (Microsoft, no Comfy-Org) | MIT (tag do repositório Comfy-Org) | `mage_flow_edit_turbo_int8_convrot` 4,16 GB, mas o encoder `qwen3vl_4b_bf16` tem 8,88 GB. O card oficial em `microsoft/Mage-Flow` não abriu (401): parâmetros, número de referências e passos **não verificados** | Candidato a testar depois do klein; não conheço a qualidade |
| **Boogu Image Edit**, **LongCat-Image-Edit**, **JoyAI-Image-Edit**, **Bernini-R** | Apache 2.0 (tags) | Boogu fp8 10,3 GB + encoder 10,6 GB; LongCat bf16 12,5 GB; Joy int8 16,4 GB + encoder 10 GB; Bernini-R é de vídeo (Wan) | Não cabem em 5 GB úteis |
| **Krea-2** (tem LoRA "style reference" e "kidsdrawing") | "krea-2-community-license" (`other`) | 13 GB int8 | Licença não é padrão; não li os termos. Descartado |
| **FLUX.1 Kontext dev** | Não comercial | — | Proibido pela regra do projeto |
| **FLUX.2 [klein] 9B / FLUX.2 dev** | Não comercial | — | Proibido pela regra do projeto |

## 6. Recomendação

### Principal: FLUX.2 [klein] 4B distilled fp8, com 2 referências

**Instalação (não executada)**
1. Baixar `flux-2-klein-4b-fp8.safetensors` (4,07 GB) para `C:/ai-local/comfyui/models/diffusion_models/` (URL na tabela acima, repositório `black-forest-labs/FLUX.2-klein-4b-fp8`, sem gate).
2. Baixar `flux2-vae.safetensors` (0,34 GB) para `C:/ai-local/comfyui/models/vae/`.
3. Manter `qwen_3_4b_fp8_mixed.safetensors` em `models/text_encoders/` (já está).
4. Subir o ComfyUI como hoje (`cd C:/ai-local/comfyui && ../venv-comfy/Scripts/python.exe main.py --port 8188`), abrir o template "Flux.2 Klein 4B image edit (distilled)" e trocar os nomes dos arquivos: UNET `flux-2-klein-4b-fp8.safetensors`; CLIP `qwen_3_4b_fp8_mixed.safetensors` (tipo `flux2`); VAE `flux2-vae.safetensors`.
5. Exportar o workflow em formato API e chamá-lo por script a partir de `prompts.py`, como já se faz com o Z-Image.

**Workflow (ordem dos nós)**
`UNETLoader` → (opcional `FluxKVCache`) → `CFGGuider`;
`CLIPLoader` (tipo `flux2`) → `CLIPTextEncode` (prompt) → `ReferenceLatent` (personagem) → `ReferenceLatent` (estilo) → positivo do `CFGGuider`; esse mesmo condicionamento → `ConditioningZeroOut` → negativo;
para cada referência: `LoadImage` → `ImageScaleToTotalPixels` → `VAEEncode`;
`EmptyFlux2LatentImage` 1344x768 + `Flux2Scheduler` + `KSamplerSelect` (euler) + `RandomNoise` → `SamplerCustomAdvanced` → `VAEDecode` → `SaveImage`.

**Parâmetros iniciais**
| Parâmetro | Valor |
|---|---|
| Passos | 4 (`Flux2Scheduler` com a mesma largura/altura do latente) |
| CFG | 1 |
| Sampler | euler |
| Saída | 1344x768 |
| Referências | 2 (imagem 1 = personagem, imagem 2 = estilo/cenário); até 4 permitido |
| Escala das referências | 0,5 a 1,0 MP (começar em 0,6 por velocidade; subir se o personagem perder detalhe) |
| Seed | fixa para refazer; aleatória para explorar |
| `FluxKVCache` | testar ligado (ganho de velocidade, nó experimental) |
| Fallback de qualidade | `flux-2-klein-base-4b-fp8`: 20 passos, cfg 5, prompt negativo real. ~5x mais lento [estimativa], mais fiel ao texto |

**Tempo estimado:** 30 a 60 s por imagem (2 referências, 1344x768) [estimativa]. Medir 5 imagens antes de assumir.

### Como escrever o prompt (edição por referência)

Regras, todas de BFL/ComfyUI: nomear as imagens por posição ("image 1", "image 2"); dizer o que vem de cada uma; descrever a cena nova em prosa e em inglês (CLAUDE.md já manda descrever só o que deve aparecer e evitar negações, o que vale para o klein também); fechar com "Style: ... Mood: ...". O prompt do klein é literal: ele não reescreve nada, então o personagem (cabeça redonda branca, contorno preto) deve ser descrito em uma frase curta em todos os prompts, para não depender só da imagem.

Frase-molde: `Use image 1 for the character's design, image 2 for the art style and color palette. New scene: <cena>. Style: <estilo>. Mood: <clima>.`

**Exemplo 1 — cena nova, mesmo personagem e estilo**
> Use image 1 for the character and image 2 for the art style. The same round-headed white stick figure with a thick black outline is now standing at a wooden market stall in an ancient Roman street, holding a small bread loaf and looking at a coin in the other hand. Flat colors, simple shapes, warm terracotta buildings in the background. Keep the character exactly as in image 1. Style: flat cartoon stick-figure explainer, thick black outlines. Mood: lively, curious.

**Exemplo 2 — cenário mais escuro para vídeo sério**
> Use image 1 for the character and image 2 for the line style and flat-color look. The stick figure from image 1 is sitting alone on a low stone bench inside a dim medieval cottage, one candle on a wooden table lighting his face and hands from the left, the rest of the room in deep brown and navy shadows. Same thick black outline and flat colors as image 2, but a darker palette. Style: flat cartoon stick-figure explainer, dark muted palette. Mood: tense, quiet.

**Exemplo 3 — mudar pose e expressão mantendo todo o resto**
> Edit image 1: keep the background, colors and art style exactly as they are, and change only the stick figure's pose. He now raises both arms above his head in surprise, with wide round eyes and an open mouth. Use image 2 only as the reference for how this character's face and body look. Style: flat cartoon stick-figure explainer, thick black outlines. Mood: surprised.

Dica: em edições de uma única imagem de entrada, basta "Change X to Y" (o template oficial usa "Change the bag color to blue."). Para 3 ou 4 referências, escrever "image 3 for the prop" etc.

### Reserva

1. **Reserva de instalação (mesmo modelo):** `unsloth/FLUX.2-klein-4B-GGUF` (Apache 2.0): `flux-2-klein-4b-Q8_0.gguf` 4,3 GB (melhor qualidade) ou `flux-2-klein-4b-Q4_K_M.gguf` 2,6 GB (cabe com folga na VRAM), mais o nó ComfyUI-GGUF (custom node) e a pasta `models/unet/`. Mesmo workflow, troca-se o `UNETLoader` pelo carregador GGUF. Use se o fp8 der erro de formato ou pico de memória.
2. **Reserva técnica:** SDXL + IP-Adapter Plus (`ip-adapter-plus_sdxl_vit-h.safetensors` 0,85 GB + encoder ViT-H 2,53 GB), com Z-Image Turbo img2img (denoise ~0,4) para limpar. Mais barato em VRAM, mas manter o mesmo personagem é bem mais difícil. Vale só se o klein falhar na consistência.
3. **Plano C:** gerar mais imagens no ChatGPT (fluxo anterior do vídeo 3) para as cenas em que o personagem aparece grande, e usar a IA local para cenário, objetos e planos sem o personagem (Z-Image Turbo txt2img, como hoje).

## 7. Riscos e dúvidas (o que só dá para saber testando)

1. **Consistência do personagem.** O klein 4B foi vendido por edição com várias referências, mas não achei teste independente de consistência de personagem em estilo de bonequinho com 150+ imagens. Pode variar proporção, espessura do contorno ou número de dedos. Teste: 10 cenas diferentes com a mesma folha de personagem e comparar lado a lado.
2. **Tempo e memória reais na 4060.** Todos os números de tempo são estimativas; os oficiais foram medidos numa RTX 5090. Medir tempo e pico de VRAM com 1, 2 e 3 referências.
3. **O `qwen_3_4b_fp8_mixed` como encoder do klein.** Deve carregar (mesma detecção no código), mas o efeito na fidelidade ao prompt não foi medido; o oficial é o bf16 (8,04 GB, mesmo hash do Z-Image).
4. **Formato do fp8 da BFL no ComfyUI 0.39.** O template oficial usa exatamente `flux-2-klein-4b-fp8.safetensors`, então deve carregar. Não verifiquei o formato interno do arquivo nem se a 4060 usa kernel fp8 nativo ou converte (o que mudaria a velocidade).
5. **Número de referências útil.** BFL diz até 4; o ganho de 3-4 referências com sequência muito maior pode estourar a VRAM e o tempo. Começar com 2.
6. **Texto dentro da imagem e objetos antigos.** Klein também erra texto (card). Os problemas do projeto (objeto antigo sai moderno, mapa e número em código) continuam; anacronismos precisam ser conferidos em toda imagem, como já está no `CLAUDE.md`.
7. **Direitos das imagens de referência.** As do ChatGPT são do usuário na prática pelos termos do serviço; conferir os termos atuais antes de usá-las como entrada de treino (LoRA).
8. **Disponibilidade futura.** Z-Image Omni/Edit e Mage-Flow-Edit podem mudar o quadro: reverificar `Tongyi-MAI` no HF e o card da Microsoft (que não abriu nesta pesquisa).
9. **Política do YouTube.** O fluxo continua dentro do risco já registrado: imagem de IA em lote precisa de autoria real no roteiro (ver [[fase6-politica-youtube]]). A ferramenta de imagem não muda isso.

## Fontes

- Card BFL klein 4B (Apache 2.0, 4 passos, ~13 GB, multi-referência): https://huggingface.co/black-forest-labs/FLUX.2-klein-4B
- Licença Apache 2.0 do 4B: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/main/LICENSE.md
- FP8 oficial 4B: https://huggingface.co/black-forest-labs/FLUX.2-klein-4b-fp8
- Repackaging ComfyUI (VAE, encoder, tamanhos): https://huggingface.co/Comfy-Org/flux2-klein-4B
- Blog BFL (4B Apache, 9B não comercial, fp8/nvfp4): https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence
- Docs BFL (até 4 referências em klein, "image 1/2"): https://docs.bfl.ai/guides/prompting_unified_reference e https://docs.bfl.ai/flux_2/flux2_image_editing
- Doc ComfyUI klein (arquivos, pastas, tempos na 5090): https://docs.comfy.org/tutorials/flux/flux-2-klein
- GGUF klein 4B: https://huggingface.co/unsloth/FLUX.2-klein-4B-GGUF , https://huggingface.co/leejet/FLUX.2-klein-4B-GGUF
- Z-Image oficial (tabela de modelos, Omni/Edit não lançados): https://github.com/Tongyi-MAI/Z-Image
- Z-Image repackaging: https://huggingface.co/Comfy-Org/z_image_turbo , https://huggingface.co/Comfy-Org/z_image
- Qwen-Image-Edit: https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI , https://huggingface.co/unsloth/Qwen-Image-Edit-2511-GGUF , https://huggingface.co/QuantStack/Qwen-Image-Edit-2509-GGUF , https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI
- IP-Adapter: https://huggingface.co/h94/IP-Adapter
- OmniGen2: https://huggingface.co/Comfy-Org/Omnigen2_ComfyUI_repackaged ; Step1X-Edit: https://huggingface.co/stepfun-ai/Step1X-Edit-v1p2
- Treino de LoRA klein (requisitos conflitantes): https://docs.bfl.ai/flux_2/flux2_klein_training , https://huggingface.co/blog/black-forest-labs/flux-2-klein-lora
- Arquivos locais lidos: `C:/ai-local/comfyui/comfyui_version.py`, `comfy/supported_models.py`, `comfy/sd.py`, `comfy_extras/nodes_flux.py`, `comfy_extras/nodes_edit_model.py`, `comfy_extras/nodes_zimage.py`, `blueprints/Image Edit (Flux.2 Klein 4B).json`, templates em `C:/ai-local/venv-comfy/Lib/site-packages/comfyui_workflow_templates_json/templates/`.
