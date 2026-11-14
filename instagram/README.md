# Instagram @dbv.forge

O Instagram é a vitrine; **dbv.pt** é a central (link na bio).

## Bio

```
DBV Forge 🔥 | Desbravadores Portugal
🏕️ Wiki de especialidades e classes
🖨️ Impressão 3D para clubes e acampamentos
🎮 Apps e jogos para Desbravadores
👇 Tudo em dbv.pt
```
Link: `https://dbv.pt`

## Calendário — primeiras 4 semanas

Ritmo: **carrossel à terça e ao domingo** (Especialidade da semana) + **Reel do Forge à quinta** +
stories quase todos os dias. Hora: **20h–21h**, quando líderes e Desbravadores estão em casa.

**Sábado:** o público é adventista e muita gente não usa redes sociais do pôr do sol de sexta ao pôr
do sol de sábado. Não publicar nesse período (nem à sexta à noite); o domingo à noite rende mais.

| Data | Formato | Conteúdo | Ficheiros |
|---|---|---|---|
| Sáb 14/11 ✅ | Carrossel | Acampamento de Inverno (publicado) | `carrosseis/01-acampamento-de-inverno/` |
| Dom 15/11 20h | Story | Story do Acampamento de Inverno com link para a wiki | `01-.../story.png` + `story-link.txt` |
| Qui 19/11 | Reel | Forge: timelapse de uma impressão (porta-chaves ou logótipo) | precisa de vídeo teu |
| Dom 22/11 | Carrossel + story | Nós | `carrosseis/02-nos/` |
| Ter 24/11 | Carrossel + story | Astronomia | `carrosseis/03-astronomia/` |
| Qui 26/11 | Reel | Forge: "da ideia à peça" (modelo no ecrã → impressão → peça na mão) | precisa de vídeo teu |
| Dom 29/11 | Carrossel + story | Orientação | `carrosseis/04-orientacao/` |
| Ter 01/12 | Carrossel + story | próxima especialidade (gerar com `gerar.py`) | — |
| Qui 03/12 | Reel | Forge: peça de Natal para o clube | precisa de vídeo teu |

Cada pasta tem os slides `1.png` a `5.png`, a `legenda.txt` (legenda + hashtags), o `story.png` e o
`story-link.txt` com o endereço da especialidade na wiki.

## Stories

Story do carrossel (só pela app, porque o sticker de link não existe no computador):
1. Novo story → escolhe o `story.png` da galeria.
2. Sticker → **Link** → cola o endereço do `story-link.txt` → texto do botão: "Ver na Wiki".
3. Põe o sticker no espaço livre por baixo de "Requisitos completos e dicas na DBV Wiki 👇".
4. Opcional: sticker de **sondagem** "Já tens esta especialidade?" (Sim / A fazer / Ainda não).

Outros stories fáceis: bastidores da impressora (10 s a imprimir já chegam) e destaques fixos no
perfil: **Wiki**, **Forge**, **Encomendas**.

Agendar: o Instagram só agenda stories pelo Meta Business Suite, com conta profissional ligada a
uma página do Facebook. Por agora publica-se à mão.

## Crescer

1. **Posts em colaboração (Collab)** com clubes e regiões: o post aparece nos dois perfis. Começa pelos
   clubes onde já conheces alguém.
2. **Oferece uma peça a um clube** em troca de um post a marcar a @dbv.forge.
3. **Eventos**: conteúdo antes de cada Camporí/evento regional, stories durante, repost dos clubes depois.
4. Responde a **todos** os comentários e mensagens nas primeiras semanas.
5. Segue e interage com clubes, líderes e regiões de Portugal (não comprar seguidores).

## Gerar mais carrosséis

1. Acrescenta um post em `posts.py` (slug da especialidade na wiki + textos dos slides).
2. `python -I instagram/gerar.py` (precisa do Google Chrome). Os PNG ficam em `carrosseis/`.

As insígnias e a área vêm da DBV Wiki e ficam em `_fonte/`.
