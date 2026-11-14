# dbv.pt

Página central dos projetos DBV, servida em **https://dbv.pt**. Liga a cada projeto, que vive no seu
próprio repositório:

| Projeto | Onde | Repositório |
|---|---|---|
| DBV Wiki | https://wiki.dbv.pt | `dbv-wiki` |
| DBV Forge (impressão 3D) | encomendas por WhatsApp | (ainda sem site próprio) |
| Missões DBV, Registo Virtual, Jogos | a caminho | — |

## Estrutura

```
site/              tudo o que é publicado, tal e qual (HTML estático, sem build)
  index.html
  robots.txt
  assets/          logótipos do DBV Forge (SVG recortados ao conteúdo)
```

A secção "Mais vistas na Wiki esta semana" é preenchida no browser a partir de
`https://wiki.dbv.pt/api/articles/top?period=week` (o CORS do wiki já aceita `https://dbv.pt`). Se a
API não responder, a secção fica escondida.

## Ver localmente

```
cd site
python -m http.server 8766
```

Abre http://127.0.0.1:8766. A secção da Wiki não aparece em local, porque a API só aceita pedidos
vindos de `dbv.pt`.

## Publicação

Por agora, o proxy (Caddy) que serve `dbv.pt` é o do repositório `dbv-wiki`, porque é ele que tem as
portas 80/443 da VPS. Esse Caddy monta a pasta `site/` deste repositório em `/srv-hub`, só de leitura:

- VPS: este repositório está em `/home/ubuntu/dbv-pt`, ao lado de `/home/ubuntu/dbv-wiki`.
- Publicar uma alteração: `cd /home/ubuntu/dbv-pt && git pull`. Não é preciso reconstruir nada.
- Em `dbv.pt` só `/`, `/robots.txt` e `/assets/*` vêm daqui; `/ads.txt` vem do wiki e todos os
  outros caminhos redirecionam (301) para o mesmo caminho em `wiki.dbv.pt`, para não partir links
  antigos.

Quando houver mais projetos na VPS, o plano é passar o proxy para este repositório, já que o `dbv.pt` é
quem concentra tudo.
