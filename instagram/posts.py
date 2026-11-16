"""Conteúdo dos carrosséis "Especialidade da semana". Textos em pt-PT, tirados da DBV Wiki.

Cada post tem 5 slides: capa, 3 slides de conteúdo e o slide final com o convite para a wiki.
Tipos de slide de conteúdo:
  ("lista", título, [itens])           itens podem ter "**negrito**"
  ("pares", título, [(termo, texto)])  termo em destaque + explicação
  ("numeros", título, [(número, texto)])
  ("passos", título, [itens])          lista numerada
"""

POSTS = [
    {
        "slug": "acampamento-de-inverno",
        "titulo": "Acampamento de Inverno",
        "nivel": "Nível II",
        "gancho": "Vem aí o frio. Estás preparado?",
        "slides": [
            ("lista", "Onde há inverno a sério em Portugal", [
                "**Serra da Estrela**",
                "**Gerês**",
                "**Montesinho**",
                "**Marão**",
                "Exige preparação a sério e líderes com experiência. Primeiro tens de ter **Arte de Acampar**.",
            ]),
            ("pares", "O segredo: três camadas", [
                ("1 · Base", "Afasta o suor da pele. Nunca algodão."),
                ("2 · Quente", "Polar ou penas, para guardar o calor."),
                ("3 · Exterior", "Impermeável e corta-vento."),
                ("À noite", "Saco-cama com conforto abaixo de 0 ºC e um isolante grosso por baixo."),
            ]),
            ("lista", "Regras que salvam", [
                "Vê os **avisos do IPMA** antes de saíres.",
                "Diz a alguém o teu **percurso e a hora de regresso**.",
                "**Hipotermia** começa com tremores e confusão: abriga, troca a roupa molhada, dá bebida quente e doce.",
                "Para derreter neve, põe primeiro **um pouco de água no fundo do tacho**.",
                "Óculos de sol evitam a **cegueira da neve**.",
            ]),
        ],
        "legenda": (
            "❄️ Acampamento de Inverno — a especialidade para quem não tem medo do frio.\n\n"
            "Em Portugal, o inverno a sério está na Serra da Estrela, no Gerês, em Montesinho e no Marão. "
            "Desliza para veres o sistema das três camadas e as regras de segurança que todo o Desbravador "
            "devia saber antes de acampar na neve.\n\n"
            "📖 Requisitos completos e mais dicas em dbv.pt (link na bio).\n"
            "💾 Guarda para o próximo acampamento e partilha com a tua patrulha."
        ),
        "hashtags": "#desbravadores #desbravadoresportugal #especialidades #acampamento #campismo "
                    "#serradaestrela #inverno #aventura #pathfinders #dbv",
    },
    {
        "slug": "nos",
        "titulo": "Nós",
        "nivel": "Nível II",
        "gancho": "Consegues fazer 20 nós de memória?",
        "slides": [
            ("lista", "O que vais aprender", [
                "Os termos da corda: chicote, laçada, volta, amarra…",
                "Cuidar das cordas e conhecer os **tipos de corda**",
                "Costuras, como a **falcaça**, que impede a ponta de desfiar",
                "Fazer uma corda de 2 m com materiais da natureza",
                "**20 nós de memória** e um quadro com **25 ou mais**",
            ]),
            ("pares", "Estática ou dinâmica?", [
                ("Estática", "Quase não estica. Para rapel, resgates e cordas fixas."),
                ("Dinâmica", "Estica para amortecer uma queda. Para escalada."),
                ("Regra de ouro", "Nunca uses uma corda estática para escalar."),
            ]),
            ("pares", "Conhece as cordas", [
                ("Sisal", "Natural e áspero."),
                ("Nylon", "Forte e elástico."),
                ("Poliéster", "Estica pouco e resiste ao sol."),
                ("Polipropileno", "Leve, e flutua."),
            ]),
        ],
        "legenda": (
            "🪢 Nós — uma das especialidades mais úteis de todas.\n\n"
            "Acampamentos, construções, resgates, rapel… os nós estão em todo o lado. Desliza para "
            "veres a diferença entre corda estática e dinâmica e os tipos de corda que tens de conhecer.\n\n"
            "Dica: um quadro de nós feito em madeira é um ótimo trabalho para expor na sala do clube.\n\n"
            "📖 Requisitos completos e mais dicas em dbv.pt (link na bio).\n"
            "💬 Qual é o teu nó preferido? Diz nos comentários!"
        ),
        "hashtags": "#desbravadores #desbravadoresportugal #especialidades #nos #nosdemarinheiro "
                    "#escutismo #acampamento #aventura #pathfinders #dbv",
    },
    {
        "slug": "astronomia",
        "titulo": "Astronomia",
        "nivel": "Nível I",
        "gancho": "Portugal tem dos céus mais escuros da Europa.",
        "slides": [
            ("lista", "Sabias que…", [
                "O **Alqueva** foi o primeiro destino do mundo certificado como *Starlight Tourism Destination*.",
                "O interior de Portugal tem dos céus mais escuros da Europa.",
                "A **Ursa Maior**, a **Cassiopeia** e a **estrela Polar** veem-se todo o ano a partir de cá.",
            ]),
            ("numeros", "Os números do céu", [
                ("384 000 km", "até à Lua"),
                ("150 milhões km", "até ao Sol"),
                ("300 000 km/s", "a velocidade da luz"),
            ]),
            ("lista", "8 estrelas para ver de Portugal", [
                "Sírio · Vega · Arcturo · Capela",
                "Betelgeuse · Rigel · Aldebarã · Polar",
                "E a **estrela da manhã**, que também é a **estrela da tarde**? Não é uma estrela: é o planeta **Vénus**.",
            ]),
        ],
        "legenda": (
            "✨ Astronomia — a especialidade para quem gosta de olhar para cima.\n\n"
            "Sabias que o Alqueva foi o primeiro destino do mundo certificado para observar estrelas? "
            "Desliza para veres os números do céu e as 8 estrelas que consegues encontrar a partir de Portugal.\n\n"
            "🔭 Dica: o Stellarium é gratuito e ajuda a planear a observação.\n\n"
            "📖 Requisitos completos e mais dicas em dbv.pt (link na bio).\n"
            "💾 Guarda para a próxima noite de acampamento."
        ),
        "hashtags": "#desbravadores #desbravadoresportugal #especialidades #astronomia #estrelas "
                    "#alqueva #ceuestrelado #natureza #pathfinders #dbv",
    },
    {
        "slug": "orientacao",
        "titulo": "Orientação",
        "nivel": "Nível II",
        "gancho": "Mapa, bússola e… para onde é o norte?",
        "slides": [
            ("lista", "O que vais aprender", [
                "Ler um **mapa topográfico** e 20 dos seus símbolos",
                "As partes de uma **bússola**",
                "Tirar e seguir um **azimute**",
                "Corrigir a **declinação**",
                "Uma caminhada de **3 km** com 5 pontos de controlo",
            ]),
            ("pares", "Palavras-chave", [
                ("Azimute", "O ângulo medido a partir do norte, no sentido dos ponteiros do relógio."),
                ("Declinação", "A diferença entre o norte magnético e o geográfico. Em Portugal é de 1 a 2 graus para oeste."),
                ("Carta 1:25 000", "As cartas militares, os mapas topográficos mais usados em Portugal."),
            ]),
            ("passos", "Tirar um azimute em 3 passos", [
                "Aponta a **seta de direção** para o alvo.",
                "Roda o **limbo** até a agulha ficar dentro da seta de orientação.",
                "**Lê o valor** no limbo. Esse é o teu azimute.",
            ]),
        ],
        "legenda": (
            "🧭 Orientação — uma das habilidades base de qualquer Desbravador.\n\n"
            "Em Portugal a orientação é também um desporto, com provas da Federação Portuguesa de Orientação "
            "em todo o país. Desliza para aprenderes as palavras-chave e a tirar um azimute em 3 passos.\n\n"
            "📍 Dica: muitos parques e escolas têm percursos permanentes de orientação — ótimos para treinar.\n\n"
            "📖 Requisitos completos e mais dicas em dbv.pt (link na bio).\n"
            "👥 Marca quem é o melhor orientador da tua patrulha."
        ),
        "hashtags": "#desbravadores #desbravadoresportugal #especialidades #orientacao #bussola "
                    "#mapa #caminhada #aventura #pathfinders #dbv",
    },
]
