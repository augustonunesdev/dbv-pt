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

## Calendário — primeiras 4 semanas (a partir de 17/11/2026)

Ritmo: **carrossel à terça e sexta** (Especialidade da semana) + **Reel do Forge à quinta** + stories
quase todos os dias. Melhor hora para publicar: 19h–21h, quando líderes e Desbravadores estão em casa.

| Data | Formato | Conteúdo | Ficheiros |
|---|---|---|---|
| Ter 17/11 | Carrossel | Acampamento de Inverno | `carrosseis/01-acampamento-de-inverno/` |
| Qui 19/11 | Reel | Forge: timelapse de uma impressão (porta-chaves ou logótipo) | precisa de vídeo teu |
| Sex 20/11 | Carrossel | Nós | `carrosseis/02-nos/` |
| Ter 24/11 | Carrossel | Astronomia | `carrosseis/03-astronomia/` |
| Qui 26/11 | Reel | Forge: "da ideia à peça" (modelo no ecrã → impressão → peça na mão) | precisa de vídeo teu |
| Sex 27/11 | Carrossel | Orientação | `carrosseis/04-orientacao/` |
| Ter 01/12 | Carrossel | próxima especialidade (gerar com `gerar.py`) | — |
| Qui 03/12 | Reel | Forge: peça de Natal para o clube | precisa de vídeo teu |

Cada pasta tem os slides `1.png` a `5.png` e a `legenda.txt` (legenda + hashtags) pronta a colar.

## Stories (fáceis, quase diários)

- No dia de cada carrossel: partilha o post nos stories com o **sticker de link** para a página da
  especialidade na wiki (ex.: `https://wiki.dbv.pt/clubes/exploradores/wiki/nos`).
- Sondagem: "Já tens esta especialidade? Sim / A fazer / Ainda não".
- Bastidores da impressora (10 s de vídeo a imprimir já chegam).
- Destaques fixos no perfil: **Wiki**, **Forge**, **Encomendas**.

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
