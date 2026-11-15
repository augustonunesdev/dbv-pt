# CLAUDE.md

Contexto para sessões do Claude Code neste repositório. Ler também o `README.md` (estrutura, ver em
local, publicação) e o `instagram/README.md` (bio, calendário, stories, crescimento).

## O que é

`dbv.pt` é a página central dos projetos DBV (Desbravadores em Portugal): liga a cada projeto, e cada
projeto vive no seu próprio repositório. Este repo é só a página central (`site/`, HTML estático sem
build, CSS dentro do `index.html`) e o material do Instagram @dbv.forge (`instagram/`).

- **Projetos no ar:** DBV Wiki (`https://wiki.dbv.pt`, repo `dbv-wiki` em `D:\projects\dbv-wiki`) e
  DBV Forge (impressão 3D, só na região do autor, encomendas por WhatsApp, ainda sem site).
- **Ideias, ainda sem código:** Missões DBV (estilo Habitica para Desbravadores), Registo Virtual de
  classes/especialidades (a intenção é que venha a ser o registo oficial em Portugal), jogos.
- Projeto novo = repositório novo, ligado a partir de um cartão na página central.

## Idiomas

- Conversa com o autor: **português do Brasil**.
- Tudo o que é publicado (site, posts, legendas): **português de Portugal** ("telemóvel", "ecrã",
  "tu" em vez de "você", etc.).

## Publicação e produção

- O Caddy que serve `dbv.pt` está no repo `dbv-wiki` (`frontend/Caddyfile` + `docker-compose.prod.yml`),
  que monta `../dbv-pt/site` em `/srv-hub`. Mudar rotas/domínios = mexer no `dbv-wiki` e reconstruir
  só o serviço `caddy` lá (`docker compose -f docker-compose.prod.yml up -d --build caddy`).
- Mudar a página = commit + push aqui e depois, na VPS, `cd /home/ubuntu/dbv-pt && git pull`.
  Não é preciso reconstruir nada.
- VPS: `ssh -i ~/.ssh/dbv_vps -o IdentitiesOnly=yes ubuntu@51.161.102.33`. O autor quer que o Claude
  faça o deploy ele próprio, quando o pedir.
- Na VPS este repo é clonado pelo alias SSH `github-dbv-pt` (deploy key só de leitura,
  `~/.ssh/github_dbv_pt`). O GitHub não deixa usar a mesma deploy key em dois repos: cada repo novo
  precisa de chave e alias próprios, e adicionar a chave pede o 2FA do autor.
- A secção "Mais vistas na Wiki" lê `https://wiki.dbv.pt/api/articles/top?period=week`; o CORS do wiki
  tem de continuar a aceitar `https://dbv.pt`.
- O `gh` CLI não está instalado no PC do autor.

## Instagram

- Gerar posts: textos em `instagram/posts.py`, PNGs 1080x1350 com `instagram/gerar.py` (Chrome
  headless). Calendário e estado de cada post no `instagram/README.md`; atualizar quando algo é
  publicado.
- O público é adventista: **nada de publicar ou agendar do pôr do sol de sexta ao pôr do sol de
  sábado.**
- Quem publica é o autor (o Chrome do PC está logado noutra conta de Instagram). Stories com sticker de
  link só pela app: gerar `story.png` + `story-link.txt` e o autor publica no telemóvel.
- O autor é dev sénior mas diz não perceber de redes sociais: decidir a estratégia por ele e explicar
  o porquê, em vez de lhe perguntar.

## Marca

- Todos os projetos usam azul-petróleo `#145660` + laranja `#f46e2c`. Logótipos em `site/assets/`:
  `logo-*.svg` só ícone (`-claro` para fundos escuros), `marca-*.svg` com nome (vertical) e
  `marca-*-horizontal.svg`, para `dbv-pt`, `dbv-wiki` e `dbv-forge`.
- dbv.pt = escudo português com o triângulo vazado dos Desbravadores; Wiki = livro aberto com o
  triângulo; Forge = a forja em D com a chama (a versão antiga com detalhes laterais foi descartada).
- Texto das marcas em Montserrat (800 em "DBV"/"dbv.pt", 500 no nome), convertido em paths (ícones
  desenhados numa grelha de 200x200, fáceis de editar à mão).
- Contacto público: `dbvwiki@gmail.com`; Instagram `@dbv.forge`.
