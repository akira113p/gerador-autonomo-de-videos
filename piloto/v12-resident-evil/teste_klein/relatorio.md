# Teste FLUX.2 klein 4B fp8 com referência (v12 Resident Evil)

Cenas testadas: 46, 55, 59, 61, 74, 87, 90, 104, 111, 120. Referências: image 1 = `p0.png`; image 2 = cena 001/002/004 do ChatGPT (003 e 005 não serviram: 005 é ícone; a cena 10/11/13 da tabela ainda não existia). Folha de contato: `folha.png` (feita antes das 3 regenerações; as imagens `046`, `059` e `090` já são as versões novas).

## Tempo
- Primeira rodada: 33 a 44 s por imagem, média 38 s (não os ~16 s esperados; o upload das referências e a carga dos modelos pesam, ou a GPU estava dividida).
- Regeração (3 imagens): média 35 s.

## Resultado
- Boas de primeira: 7 de 10 (55, 61, 74, 87, 104, 111, 120). Com 1 regeração: 10 de 10.
- Personagem: igual à folha P0 em todas (cabeça branca, gorro cinza, parca azul, botas pretas). Estilo bate com o ChatGPT (traço grosso, paleta fria, neve).

## Problemas por tipo
- Composição/cena ruim (2): 46 (personagem flutuando diante do para-brisa, pedido de "visto por trás pelo vidro traseiro" confundiu); 59 (túnel de pedra derretido, carros deformados, personagem e botas ficaram marrons/bege).
- Personagem sem parte do traje (1): 90 sem gorro quando ele está longe/pequeno no meio da multidão.
- Vazamento da referência de estilo (1): 74 copiou o personagem grande, a caneca e a janela da cena 001 (a "image 2" traz objetos, não só estilo).
- Detalhe de narrativa errado (1): 104, a toalha ensanguentada foi parar num figurante pequeno à frente, não no homem da frente (o homem a entrega).
- Texto errado: nenhum. Anatomia: sem dedos/membros quebrados; pessoas de fundo bem. Anacronismo: nenhum (carros anos 90, capacetes, helicóptero de dois rotores ok).
- Segunda rodada: 46, 59 e 90 ficaram boas.

## Regras de prompt que funcionaram
- Molde da tarefa, mais "wearing the grey beanie and navy parka" quando a figura aparece pequena ou longe.
- Descrever a posição do personagem de forma simples e concreta ("stands on the snowy shoulder beside a stopped car"), sem pontos de vista complicados (atrás do vidro, de costas).
- Trocar "tunnel de montanha" (pedra, vira lama) por "smooth concrete road tunnel": material descrito, não o nome genérico.
- Listar poucos objetos e dar a cor de cada (camper van branco, luzes traseiras vermelhas); silhuetas "with writhing tentacles" saíram ótimas sem gore.
- Usar como image 2 uma cena exterior do ChatGPT para exteriores e uma interior para interiores; evitar a cena com personagem em primeiro plano grande (001/003), que vaza.
- Mudar o seed e o trecho de composição basta; 1 regeração resolve.

## Veredito
Serve para as ~155 cenas locais. Contar ~2 tentativas em 30% das cenas (~40 s cada, ~1,5 h de GPU no total). Ajustar: usar como image 2 só cenas sem personagem grande em primeiro plano (ex.: 002 ou uma de rua/estrada), frase curta por cena, repetir "grey beanie, navy parka" no prompt, e checar sempre o gorro e o objeto narrado (toalha, cor, mão).
