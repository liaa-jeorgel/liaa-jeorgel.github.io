# Verificação da revisão — 10 de Novembro de 2026

## Conteúdo e documentos

- Pipeline: quatro etapas concluídas e quatro planeadas, conforme as informações de consolidação fornecidas pelo autor. Actividade actual e próxima fase identificadas; treino e avaliação continuam planeados.
- Contagens da tabela comparadas automaticamente com o pedido: 50.904 origens em cada horizonte; elegíveis 49.124/49.068/48.984; excluídas 1.780/1.836/1.920. Em cada linha, elegíveis + excluídas = origens. Não se somam horizontes como observações distintas.
- Relatórios técnicos `implementacao_etapa3_incremento7.md` e `diagnostico_final_fontes_meteorologicas.md` efectivamente lidos na aplicação separada. Contêm caminhos pessoais e referências locais: não foram incluídos nos downloads públicos.
- Word de consolidação não encontrado nos locais pesquisados (repositório, anexos, Unipampa, Downloads e Documents). Resultados atribuídos ao relatório a partir do pedido do autor, sem alegar leitura do Word.
- Marco sem data separado das entregas de 29/10 e 28/10, em ordem decrescente. Data de edição do site: 10/11/2026.

## Verificações automáticas efectivamente executadas

- `node --check assets/main.js`: passou.
- `git diff --check`: passou.
- Parser HTML: 15 IDs únicos e 22 referências. Âncoras resolvidas; ficheiros locais ligados existentes. Nenhum download aponta para documento inexistente.
- PNG de partilha: assinatura/dimensões verificadas, 1200 × 630, 46.105 bytes; `og:image` actualizado.
- HTML, CSS, JavaScript e favicon somam aproximadamente 38,3 KB sem compressão. Incluindo PNG e SVG social preservado, o conjunto continua abaixo de 300 KB. É uma soma de ficheiros, não uma medição de transferência em rede.

## Testes no navegador

Utilizei o Playwright e o Chromium já instalados na aplicação separada, sem acrescentar dependências ao site. Servidor HTTP local, sem publicação. O sandbox bloqueou inicialmente o servidor e o Chromium; os testes foram executados com autorização fora do sandbox.

Testes a **360, 768 e 1440 px**, altura 900 px:

- Página carregada, título correcto, quatro estados concluídos e quatro planeados.
- `document.documentElement.scrollWidth <= innerWidth` nas três larguras, com e sem JavaScript.
- Sem erros JavaScript de página.
- Menu móvel aberto por botão e ligação; `aria-expanded` actualizado; Escape fecha e devolve foco ao botão.
- Ligação «Problema» navega para a secção existente, com título abaixo do cabeçalho.
- Registo datado focado e aberto por Enter.
- Sem JavaScript: navegação visível, tabela acessível no documento e registo expansível funcional, nas três larguras.
- Teste adicional com Tab e Enter para «Saltar para o conteúdo». A primeira execução revelou que o destino não recebia foco; corrigido com `tabindex="-1"` no `main` e teste repetido com sucesso.
- Respostas HTTP observadas para HTML, CSS e JavaScript: 200.

Capturas locais foram geradas nas três larguras. Inspeccionei a captura integral de 360 px e capturas de 1440 px do início e dos resultados. A revisão visual detectou o botão móvel visível no desktop; o CSS foi corrigido para o ocultar acima de 760 px e os testes responsivos foram repetidos. A versão de 768 px foi verificada automaticamente e capturada, sem inspecção visual detalhada.

## Limites e pendências

- Lighthouse e axe-core não encontrados nas ferramentas instaladas consultadas; não foram executados e não há pontuações declaradas.
- Não executei teste com leitor de ecrã nem auditoria automática de contraste. A verificação de acessibilidade abrange semântica, tabela com caption e scope, teclado, foco, menu e funcionamento sem JavaScript.
- Não repeti as 240 verificações científicas nem a amostragem de 1.200 instantes; estes números pertencem ao relatório de consolidação.
- Os links externos de referência foram preservados; não houve nova auditoria de disponibilidade externa nesta revisão.
- Nenhum commit, push ou publicação foi realizado. A pasta `.git` foi preservada.

## Revisão visual com a aplicação — 10/11/2026

- Acesso efectivo ao endereço local 5173 por Chromium/Playwright, sem carregar ficheiros, processar dados ou alterar configurações da aplicação. Captura visual inspeccionada.
- Leitura dos estilos da aplicação e comparação com valores calculados: destaque `#f96501`, destaque forte `#b84b00`, fundo suave `#fff3e8` e texto `#171717`.
- No site, valores calculados confirmados para botão primário, secundário, estados concluído e planeado e pilha tipográfica. Hover primário e secundário verificados; sem alegar que esses hovers existiam na aplicação.
- Repetidos os testes responsivos a 360, 768 e 1440 px: sem deslocamento horizontal, sem erros de página, menu e Escape funcionais, foco devolvido ao botão, âncora Problema abaixo do cabeçalho e expansão por Enter.
- Repetidos os cenários sem JavaScript nas três larguras: menu visível, tabela presente, detalhes funcionais e ausência de deslocamento horizontal.
- Capturas após harmonização: inspecção visual do início a 1440 px, incluindo cabeçalho, e a 360 px. Sem nova inspecção visual detalhada de 768 px.
- Sintaxe JavaScript, diff sem erros de espaços, IDs únicos (15), âncoras e recursos locais (22 referências) verificados novamente.
- Soma actual de HTML/CSS/JS/favicon: **39,589 bytes**; HTML e todos os assets: **85,488 bytes**. Sem compressão; não é uma medição de rede. Mantém-se abaixo de 300 KB.
- Favicon, ilustração conceptual, SVG social e PNG social harmonizados. Sem dependências ou fontes externas acrescentadas.
- Lighthouse não executado nesta revisão. Não se atribuem pontuações nem certificação global de acessibilidade.
- Alterações limitadas ao repositório do site. Sem commit, push ou publicação.

## Experiência de utilização e transparência — 10/11/2026

### Conteúdo e estrutura

- Oito etapas com estado, resumo visível e detalhes de entradas, operação, saídas, verificação e suporte. Quatro concluídas e quatro planeadas, sem simulação de execução.
- Indicadores explicados e ligados à integração/série; fonte comum explícita. Tabela com universo, unidade, interpretação e descrição acessível. Valores originais preservados; não se atribuem totais a motivos individuais de exclusão.
- Critérios de elegibilidade expansíveis; definições de PM2.5, lag, baseline, série multivariada, alvo, MAE, RMSE e R².
- Diário com IDs permanentes, índice e ligações às etapas; marco sem data preservado. Documentos técnicos e pendência do Word mantidos explicitamente.
- Aplicação consultada novamente no endereço 5173 e CSS lido. Paleta confirmada: #f96501, #b84b00, #fff3e8, #171717. Captura real da interface inicial incluída, sem a equiparar a resultado científico. A imagem publicada foi recortada para não incluir a área de carregamento e caminhos locais; legenda indica data de captura e ausência de dados carregados.

### Testes efectivamente executados

- Chromium/Playwright a 360, 768 e 1440 px, altura 960 px, com movimento reduzido: título e estado inicial presentes; secção activa Início, Etapas e Evolução confirmadas nos destinos correspondentes.
- Menu móvel: abertura, Escape e retorno do foco. Âncora Etapas abaixo do cabeçalho. Detalhe da série aberto por Enter; ligação aos critérios abre o detalhe correspondente e posiciona-o abaixo do cabeçalho.
- Ligação directa numa nova navegação a `#entrega-2026-10-29` abre a entrega. Imagem real carrega com largura original de 1200 px. Tabela comparada exactamente com os números confirmados.
- Ausência de scroll horizontal nas três larguras, incluindo os detalhes das oito etapas abertos. Sem erros JavaScript de página.
- Sem JavaScript nas três larguras: menu visível, navegação até Etapas, destinos sem cobertura do cabeçalho, detalhes funcionais e ausência de scroll horizontal.
- A primeira execução verificou a abertura dos critérios antes de o evento `hashchange` ser entregue; o teste foi ajustado para aguardar a navegação. As três larguras passaram na execução final.
- Capturas de início e resultados geradas nas três larguras; inspecção visual do início a 1440 px e dos resultados a 360 px. Não houve inspecção visual detalhada de todas as secções em todas as larguras.
- Após a última execução visual, a identificação institucional e a explicação da próxima actividade foram explicitadas e os destinos de secção tornados focáveis. São ajustes de texto/semântica, verificados estaticamente; não se repetiu toda a suite visual após esses ajustes.
- Sintaxe JavaScript e `git diff --check` passaram. Parser de IDs/âncoras/recursos e igualdade da tabela passaram. Não há downloads para ficheiros ausentes.
- Contraste calculado pela fórmula de luminância relativa sRGB, para os pares principais de texto: #171717 / #ffffff: 17.93:1; #525252 / #fafafa: 7.49:1; #b84b00 / #ffffff: 5.19:1; #b84b00 / #fff3e8: 4.76:1; #ffffff / #b84b00: 5.19:1. Todos superam 4,5:1. Isto não equivale a uma auditoria integral de acessibilidade.
- Tamanho actual HTML/CSS/JS/favicon: **58,684 bytes**; HTML com todos os assets: **135,593 bytes** sem compressão. Não é medição de rede. Captura WebP fora da área inicial com `loading="lazy"` e dimensões explícitas.

### Limites

Lighthouse e leitor de ecrã não executados. Sem testes com utilizadores; as conclusões são de inspecção técnica e visual. Os resultados científicos foram preservados a partir das fontes já descritas, sem nova auditoria de dados. Word de consolidação continua pendente. Nenhuma alteração na aplicação, commit, push ou publicação.

## Modo escuro automático — 10/11/2026

- Implementado com `prefers-color-scheme` em `assets/style.css`, sem botão, JavaScript ou armazenamento de preferência. `color-scheme` e `theme-color` acompanham o tema do sistema.
- Testes com Chromium/Playwright a 360, 768 e 1440 px, em esquema claro e escuro: fundo do `body` `#fff`/`#101010`, texto `#525252`/`#c6c6c6`, sem deslocamento horizontal e sem erros de página.
- Auditoria por estilos calculados no tema escuro: 468 nós de texto, nenhum abaixo de 4,5:1 (3:1 para texto grande); nenhum bloco de fundo claro com área superior a 5.000 px².
- Impressão em sistema escuro: fundo branco e texto escuro confirmados.
- A ilustração SVG recebeu classes para adaptar gradiente, grelha, edifícios, colina, partículas, sinal, horizontes e rótulo.
- Não foram alterados conteúdo científico, estrutura, dependências ou comportamento sem JavaScript. Sem commit, push ou publicação.

## Navegação lateral — 16/11/2026

Testes Chromium/Playwright sobre o ficheiro local a 360, 768 e 1440 px: apenas uma secção visível; selecção de Etapas; ligação interna da série aos critérios de exclusão abre Materiais e os detalhes; Voltar restaura Etapas; Enter selecciona Projectos relacionados; estado `aria-current` correcto; menu móvel fecha com Escape e devolve foco; ausência de scroll horizontal e erros JavaScript. No computador, a área principal começa à direita da barra lateral. Sem JavaScript, as nove secções permanecem disponíveis. Captura de 1440 px inspeccionada. Sintaxe JavaScript e diff verificados. Não houve publicação ou push.

## Redesenho académico, tecnológico e animado — 16/11/2026

- Referências: Stanford HAI consultado por web e Chromium, com captura inspeccionada; MIT Media Lab consultado por web, mas timeout no navegador; Senseable City Lab apareceu na pesquisa e foi aberto, sem texto extraível e com timeout de captura por fontes. Não se afirma uma comparação visual completa dos três sites nem um ranking de qualidade.
- CSS reorganizado, preservando suporte a modo escuro e o destaque laranja. Sem bibliotecas ou fontes externas acrescentadas. SVG original conceptual, sem dados fictícios.
- Seis cenários Chromium/Playwright: 360/768/1440 px × claro/escuro, com movimento reduzido. Em todos: início visível, uma secção de cada vez, selector de 6 h actualiza texto e nó, menu para Etapas, ligação aos critérios abre Materiais, tabela científica exactamente preservada, Voltar funciona, teclado Enter selecciona relacionados, Escape fecha menu móvel e devolve foco, sem erros de página ou scroll horizontal.
- Teste complementar com movimento activado: órbita animada; pausa/retoma global e pausa local do diagrama confirmadas pelos estilos calculados. Sem JavaScript, as nove secções e os detalhes continuam disponíveis e não há scroll horizontal a 360 px.
- Percurso adicional das nove secções em 360/768/1440 px: visibilidade exclusiva, ligações do menu e ausência de scroll horizontal. Link de salto por Tab/Enter verificado.
- Capturas geradas nos seis cenários. Inspeccionadas as capturas do início em claro/1440 e escuro/360, e a primeira captura móvel clara. Corrigida a posição inicial para preservar a barra de identificação do capítulo no topo.
- Parser HTML: 37 IDs únicos e 69 referências, com âncoras e ficheiros locais válidos. Contagens da tabela comparadas exactamente com os valores anteriores. Sintaxe JavaScript e `git diff --check` passaram.
- Contraste matemático sRGB dos pares principais: #20221f/#fffefa: 15.88:1; #525650/#fffefa: 7.42:1; #676d61/#f5f4ee: 4.84:1; #b84b00/#fffefa: 5.15:1; #b84b00/#fff0e4: 4.66:1; #c1caba/#171d19: 10.13:1; #202a20/#e3e8d8: 11.89:1; #a0b28f/#19231e: 7.12:1; #c0c5b9/#161c18: 9.83:1; #ffb17c/#161c18: 9.75:1. Todos ≥4,5:1; isto não é uma auditoria completa de acessibilidade. Cores de metadados e foco receberam ajuste final, verificado estaticamente.
- HTML/CSS/JS/favicon: **82,388 bytes**; HTML e todos os assets: **159,297 bytes**, sem compressão. Não é medição de transferência em navegador. Mantém-se abaixo de 300 KB.
- Lighthouse não encontrado por `command -v lighthouse`; não foi executado. Não houve testes com utilizadores ou leitor de ecrã nesta revisão.
- Sem alterações na aplicação de processamento, sem commit, push ou publicação. Pendência do Word de consolidação preservada.

## Retorno ao menu superior — 16/11/2026

Chromium a 360, 768 e 1440 px: nove secções visíveis, margem lateral eliminada, barra de dashboard removida, menu superior e compacto funcionais. Enter navega para Etapas sem cobertura do título pelo cabeçalho; estado da secção corrente correcto. Ligação aos critérios abre os detalhes; Voltar funciona; Escape fecha o menu e devolve foco. Sem erros JavaScript ou scroll horizontal. Captura de 1440 px inspeccionada. Sintaxe e diff verificados. Sem publicação.

## Barra de leitura fixa

Testes Chromium/Playwright executados sobre o ficheiro local a 360, 768 e 1440 px:

- Início 0%, meio aproximadamente 50% e fundo 100%, calculados pela área total de scroll.
- Altura calculada de 3 px; ocultar a barra não altera a posição do cabeçalho.
- Inserção de conteúdo de teste no DOM altera o denominador e recalcula o progresso automaticamente.
- Resize recalcula o percentual de acordo com as novas dimensões.
- Ao ocultar temporariamente o conteúdo durante o teste e eliminar o scroll, a barra oculta-se.
- Movimento reduzido desactiva a transição; sem erros JavaScript de página.
- Com movimento activado, transição calculada de 100 ms e preenchimento completo confirmado pela matriz de transformação no fundo da página.

Os elementos temporários existiram apenas no navegador de teste. Conteúdo e design do site preservados. Sintaxe JavaScript e `git diff --check` verificados; sem publicação.

## Tabela comparativa de projectos

Acrescentadas cinco linhas (PM2.5 como referência e quatro projectos dos colegas), comparando dados, tarefa e diferenças metodológicas. Síntese baseada nos resumos e fontes já identificados nos cartões, sem nova consulta ao portal, sem comparação de desempenho e com a ressalva de autoria de Alisson preservada. Chromium a 360, 768 e 1440 px: cinco linhas e cabeçalhos semânticos confirmados; sem scroll horizontal na página; região da tabela focável com foco visível e deslocamento por setas em larguras pequenas; ligação ao cartão de EMG funcional e título abaixo do menu. IDs, âncoras, sintaxe JavaScript e diff verificados. Sem publicação.

## Comparador de projectos em foco

Cartões removidos do HTML. Chromium a 360/768/1440 px: cinco selectores, apenas um `aria-pressed=true`, mudança do conteúdo por foco e hover, navegação por setas, Escape para a referência, ligação externa correcta do projecto seleccionado, três dimensões comparativas, tabela integral expansível e ausência de scroll horizontal na página. Mantidas as ressalvas de Alisson/Gabriel e a participação de Maria Eduarda. Toque confirmado num contexto móvel emulado de 390 px. Sem JavaScript, a tabela integral fica aberta e os controlos interactivos ocultos. Capturas de 360 e 1440 px inspeccionadas. Texto das opções não seleccionadas mantém contraste, sem redução de opacidade. IDs/âncoras, sintaxe e diff verificados. Não houve nova consulta ao portal nem publicação.

## Mapa comparativo — leitura por linhas e colunas

Chromium a 360, 768 e 1440 px: cinco colunas de projectos, quatro dimensões, selecção única realçando as cinco células da coluna correspondente; selecção por foco, setas, hover e clique; títulos, autoria com ressalvas e links do detalhe correctos. Toque confirmado em contexto móvel emulado. Nenhum scroll horizontal na página; deslocamento restrito ao mapa, com a coluna de dimensões fixa. Sem JavaScript, mapa estático e tabela integral disponíveis. Capturas de 360/1440 px inspeccionadas. Removidos os estilos obsoletos do comparador anterior; preservados o conteúdo científico, fontes e ressalvas. IDs/âncoras, sintaxe e diff verificados. Sem nova consulta ao portal ou publicação.

## Cartões das etapas metodológicas

Chromium a 360/768/1440 px: oito cartões, quatro estados concluídos e quatro planeados; Enter abre o cartão; outra selecção mantém apenas um aberto; quatro campos de detalhe preservados; ligação aos critérios funcional e ligação directa à auditoria abre os detalhes. Sem erros JavaScript ou deslocamento horizontal. Sem JavaScript, abertura e exclusividade nativas confirmadas. Toque confirmado num contexto móvel emulado. Captura de 1440 px inspeccionada. IDs/âncoras, sintaxe e diff verificados. Conteúdo científico preservado, sem publicação.

## Modal das etapas

A primeira tentativa de teste foi impedida por falha da revisão automática de autorização por limite de utilização. Após o pedido do autor para avançar, a nova tentativa foi autorizada. O primeiro teste detectou que a circulação nativa de Tab podia sair do conteúdo do diálogo; foi acrescentado controlo explícito de Tab/Shift+Tab.

Execução final em Chromium a 360, 768 e 1440 px: Enter abre a modal; cartões mantêm-se fechados; quatro dimensões de detalhe presentes; foco por Tab permanece na janela; Escape fecha e devolve foco; botão e clique fora fecham; ligação directa para uma etapa abre a modal; fonte interna fecha a janela e abre os critérios. Sem erros JavaScript ou scroll horizontal. Sintaxe JavaScript e diff verificados. Sem publicação.

## Evolução didáctica com apontadores

Chromium a 360/768/1440 px: sete apontadores (seis fases e próximo passo), apenas um estado actual com `aria-current="step"`, duas datas no percurso e próximo passo explicitamente planeado. Enter numa ligação abre o relato da exportação; ligação da actividade actual abre a modal da série multivariada. Sem erros JavaScript ou deslocamento horizontal. Sem JavaScript, o percurso continua disponível. Captura de 1440 px inspeccionada. IDs/âncoras, sintaxe JavaScript e diff verificados. Não foram criadas datas ou métricas; os registos documentais existentes foram preservados. Sem publicação.

## Cartões e modal na evolução

O percurso de evolução usa sete cartões com resumo, indicação de data, estado actual e próximo passo. Detalhes abrem na modal partilhada com as etapas; relatos completos e IDs existentes mantidos, com novos IDs permanentes nos marcos.

A primeira autorização de teste excedeu o prazo sem executar o comando. A repetição permitida foi autorizada e executada em Chromium a 360, 768 e 1440 px. Confirmados: sete cartões; Enter abre modal; data 28/10/2026 preservada; Tab contido; Escape fecha e devolve foco; estado «Estou aqui» correcto; ligação da modal da evolução abre a modal da série temporal; ligação directa ao marco abre a janela; fonte abre o relato de 29/10. Sem erros de página ou scroll horizontal. Sintaxe JavaScript, IDs/âncoras e diff verificados. Não foi repetido teste sem JavaScript nesta revisão. Sem publicação.

## Single Page e overlay entre secções

Removidos elemento, estilos, estado e função do efeito de livro; verificação estática confirma ausência de `book-folio`, `turnBookPage`, `lastBook`, `rotateY` e `skewY` nos ficheiros de execução. Conteúdo mantido numa única página contínua.

Chromium a 360/768/1440 px: nove secções visíveis; overlay activado ao atravessar a fronteira Início/Contexto e no regresso; keyframes sem rotação, skew ou perspectiva; camada sem intercepção de cliques e abaixo do menu; desaparecimento ao terminar; ausência de scroll horizontal e erros de página. Movimento reduzido impede a activação. Navegação até ao rodapé confirmada com progresso de leitura a 100%. IDs, âncoras, sintaxe e diff passaram. Sem publicação.

## Página educativa PM2.5 — 17/11/2026

### Preservação e rigor

- O anexo inicial continha requisitos, mas não o texto integral. Após clarificação, o autor forneceu os parágrafos e as cinco referências; a implementação usa esse conteúdo, não uma substituição editorial.
- Dez blocos de texto comparados automaticamente, normalizando espaços, com os parágrafos fornecidos: definição, origens, composição, saúde, estudo de Di, unidade, introdução às directrizes, percentil e dois parágrafos de Luanda. Todos presentes integralmente. Cinco referências completas, descrições, data fornecida e DOI confirmados no HTML.
- Definição aerodinâmica preservada; distinções µm/µg/m³ e horizonte/agregação explícitas. Tabela: média anual 5 µg/m³, média de 24 h 15 µg/m³. Preservadas as notas do percentil 99, três a quatro dias, protecção da saúde versus limites legais e impossibilidade de aplicar directamente os valores a concentrações horárias.
- Grupo 1 explicado como evidência de carcinogenicidade, sem escala de intensidade de risco. Estudo de Di identificado como exposição prolongada em aproximadamente 61 milhões de beneficiários do Medicare nos EUA, sem extrapolação quantitativa para Luanda. Horizontes 1/3/6 h identificados como objectivos da investigação.

### Fontes: verificação do agente em 17/11/2026

Esta lista é independente da frase de data de consulta fornecida pelo autor:

1. EPA, *Particulate Matter (PM) Basics*: página efectivamente aberta e conteúdo lido. Apresenta actualização de 18/09/2026; não se inventou um ano de publicação para a referência fornecida, que não o indicava.
2. WHO, directrizes 2021: página institucional `https://www.who.int/publications/i/item/9789240034228` aberta e título/ano confirmados. Q&A oficial das directrizes também consultado, incluindo a nota de percentil 99. O PDF IRIS e a tabela NCBI encontraram, respectivamente, 403 e verificação de navegador; não se afirma leitura integral desses recursos nesta revisão. Valores da tabela do autor preservados.
3. WHO, *Ambient (outdoor) air pollution*: página aberta, título e data 24/10/2024 confirmados. Página institucional complementar sobre tipos de poluentes também aberta para definição/composição; não foi acrescentada como sexta referência à bibliografia original.
4. IARC, *Outdoor Air Pollution*, volume 109: catálogo numérico `https://publications.iarc.who.int/538` aberto e título/volume confirmados. Catálogo indica 2015, enquanto o texto fornecido indica 2016; referência mantida como fornecida, divergência registada para revisão. Uma tentativa com um slug terminado em 2016 devolveu outro livro e foi descartada. O comunicado IARC de 2013 foi efectivamente aberto para a definição de Grupo 1.
5. Di et al.: artigo completo em `https://pmc.ncbi.nlm.nih.gov/articles/PMC5766848/` efectivamente aberto e autores, DOI, 2017 e coorte de 60.925.443 confirmados. A abertura directa do PubMed devolveu conteúdo incompleto e o DOI devolveu 403 pela ferramenta; não se declara acesso integral por esses destinos. Links originais mantidos, com alternativa PMC. Nenhum resultado numérico adicional foi transposto para o projecto de Luanda.

### Testes da página e integração

- Chromium/Playwright a 360, 768 e 1440 px, em claro e escuro, com movimento reduzido: botão do Contexto abre `pm25.html` na mesma aba; recarregamento directo funcional; um H1; sete secções e sete destinos do índice; cinco referências.
- Índice móvel inicialmente compacto, aberto por Enter. Destino Concentrações abaixo do cabeçalho; tabela comparada exactamente com os valores fornecidos. Citação [2] leva a `ref-2` e o regresso retoma a passagem citada com foco. Sem erros JavaScript de página ou scroll horizontal.
- Barra partilhada a 0% no topo e 100% no fundo, posicionada abaixo do cabeçalho. Regresso ao Contexto funcional nos seis cenários.
- Sem JavaScript a 360 e 1440 px: sete secções visíveis, índice e percursos de formação disponíveis, navegação por âncoras e ausência de scroll horizontal.
- Servidor HTTP efémero em loopback: entrada pelo Contexto, recarregamento de `/pm25.html`, HTML/CSS/JS sem respostas locais 4xx/5xx. Também confirmadas a modal de série temporal da página principal e a barra partilhada a 100%. Servidor encerrado após o teste.
- Capturas claras de 1440/360 px do início, saúde e interpretação inspeccionadas. Corrigida duplicação de indicadores no summary do índice. Sem nova auditoria visual integral de todas as secções em cada largura.
- Parser: IDs únicos nas duas páginas (52 na principal; 28 na educativa), recursos e âncoras locais resolvidos, ausência de parâmetros `utm_source`. Todas as citações e backlinks apontam para IDs existentes.
- Sintaxe dos três scripts (`main.js`, `education.js`, `reading-progress.js`) e `git diff --check` passaram. Lighthouse não encontrado por `command -v lighthouse`; não executado. Sem teste com leitor de ecrã ou utilizadores.

Nenhuma publicação, commit ou push realizado.

## Vistas de contexto e dinâmica C4 — 17/11/2026

### Inspecção e bases

Inspeccionados HTML, CSS, JavaScript e documentação existentes no repositório do site; lidos também, apenas em consulta, o README da aplicação separada e passagens do relatório `implementacao_etapa3_incremento7.md`. Referências oficiais C4 de contexto e dinâmica abertas pela ferramenta web. As fases metodológicas não são representadas como contentores; não se infere integração directa com a API, sensores locais ou arquitectura dos modelos futuros.

As operações de preparação e exportação têm suporte documental. A conclusão histórica da preparação mantém a atribuição ao marco informado pelo autor. As limitações e pendências arquitecturais estão no README.

### Testes efectivamente executados

- Chromium/Playwright em seis cenários: 360/768/1440 px × claro/escuro, com movimento reduzido.
- Nova secção imediatamente depois de Início e antes do Contexto; título «Como o projecto funciona» único. Secção metodológica e IDs anteriores preservados.
- Vista de contexto: três entidades (fonte externa, pessoa e aplicação), uma aplicação dentro da fronteira. Vista dinâmica: oito interacções numeradas; fontes, intervenientes, sentido e operação legíveis em texto.
- Primeiro teste já verificou os seis cenários. Revisão visual posterior explicitou o pedido de diagnóstico/preparação para não sugerir execução automática e alongou as setas entre as linhas dos participantes. A suite completa foi repetida após estes ajustes, com sucesso.
- Link de fonte activado por foco/Enter abre a modal existente. Todos os destinos internos distintos dos diagramas foram percorridos: etapas e fases futuras abrem as modais; papel, sistema e materiais abrem os detalhes correctos; seis campos confirmados em cada destino.
- Nos destinos fora de modal, título/summary permanece abaixo do cabeçalho. Sem erros JavaScript de página ou scroll horizontal.
- Sem JavaScript a 360/1440 px: ambas as vistas e a lista numerada disponíveis; link de fonte navega para a etapa; detalhe nativo abre e contém os seis campos. Sem scroll horizontal.
- Capturas geradas em todos os cenários; inspeccionadas as vistas clara/1440 de contexto e dinâmica e clara/360 de contexto e dinâmica. Não houve inspecção visual detalhada de todas as secções em todas as cores/larguras.
- Parser: `index.html` com 69 IDs únicos e 112 referências; `pm25.html` com 28 IDs e 52 referências. Âncoras e ficheiros locais válidos, incluindo marcadores SVG. Sem alteração no conteúdo da página educativa.
- Sintaxe de `main.js`, `education.js` e `reading-progress.js` e `git diff --check`: passaram. Não houve necessidade de novo JavaScript para os diagramas.
- HTML principal + todos os assets: 250.590 bytes sem compressão, antes das alterações de documentação. É soma de ficheiros, não medição de transferência em navegador.

### Limites

Não foram executados Lighthouse, leitor de ecrã ou testes com utilizadores nesta revisão. Não foram testadas a aplicação de processamento, chamadas à OpenWeather, exportações reais ou auditorias científicas. As medições de desempenho operacional e a arquitectura das fases futuras permanecem pendentes. Não houve commit, push ou publicação.

## Revisão — substituição dos cartões metodológicos por vista C4

Verificações executadas em Chromium local, com Playwright, em 360, 768 e 1440 px, com e sem JavaScript e preferência de movimento reduzido:

- Oito ligações do novo percurso conduzem aos detalhes correspondentes. Com JavaScript, Enter abre a modal; os seis campos estão presentes e Escape restitui o foco à ligação de origem.
- Sem JavaScript, a navegação por âncora revela os detalhes textuais; cada descrição pode abrir pelo controlo nativo.
- Nenhum scroll horizontal nos seis cenários; nenhum erro JavaScript de página.
- Sintaxe de JavaScript e `git diff --check` verificadas nesta revisão.

A vista mantém um investigador e um sistema; as quatro fases futuras são ligações metodológicas, sem arquitectura inventada. Permanecem pendentes testes com leitor de ecrã, outros motores de navegador e utilizadores. Não foram reexecutadas verificações científicas nem alterada a aplicação separada. Sem publicação ou envio ao GitHub.
- Inspecção visual das capturas de 360 e 1440 px: participantes, numeração, sentidos das relações e texto legíveis; a identidade cromática e tipográfica foi preservada.

## Revisão de UI e UX — estrutura e navegação

Executado nesta revisão, em Chromium local:

- Dez destinos do menu em 320, 360, 768, 1024 e 1440 px: ordem coerente com as secções, indicação de secção activa correcta, destinos abaixo do cabeçalho, sem scroll horizontal da página e sem erros JavaScript.
- Em 360/1440 px: abertura de detalhes C4 conserva a posição de fundo; Escape devolve o foco à ligação original. Voltar entre dois detalhes reabre o detalhe anterior e Voltar à secção fecha a modal. Setas do teclado no mapa comparativo mudam o foco e o projecto seleccionado.
- Menu em 568 × 260 px: último destino alcançável; Escape fecha o menu e devolve o foco ao botão.
- Regressão dos oito destinos metodológicos em 360/768/1440 px, com e sem JavaScript: seis campos preservados e descrições nativas acessíveis. Testes com preferência de movimento reduzido.
- Inspecção visual da captura do menu aberto em 320 px: nomes legíveis e hierarquia preservada.

Ajustados: numeração antiga das secções, reconhecimento do destino “Resultados e materiais”, distinção entre arquitectura e metodologia, deslocamento desnecessário do fundo ao abrir modais e tratamento de histórico com janela aberta. O conteúdo científico foi preservado. Estes testes são uma revisão técnica de usabilidade; não substituem testes com utilizadores, leitor de ecrã ou uma auditoria completa de acessibilidade. Outros motores de navegador permanecem pendentes.

## Botão flutuante da aplicação — 23/11/2026

Adicionado acesso “Abrir aplicação” na página principal e na página educativa. O destino é o endereço HTTP fornecido pelo autor, com `#preparacao`; abre numa nova aba, indicada no nome acessível. Não requer JavaScript. Foram verificados em Chromium local, sem JavaScript, a 320 e 1440 px: URL exacto, foco por teclado, área de toque mínima de 44 px, posição fixa no início e no fim da página e ausência de scroll horizontal. Inspeccionada a captura do rodapé a 320 px. A disponibilidade do serviço remoto não foi testada. Nenhuma publicação realizada.

### Refinamento visual do acesso à aplicação

Texto alterado para “Explorar dados de PM2.5”, com indicação visível “Abrir aplicação · nova aba”. Ícone SVG conceptual com partículas e traçado de sinal; não representa uma medição em tempo real. As animações de entrada terminam em menos de cinco segundos, o foco/hover realça o sinal, e a regra de movimento reduzido desactiva os efeitos. O controlo geral de pausa do site também se aplica às animações CSS. Repetidas as verificações locais em 320/1440 px, nas duas páginas: destino preservado, foco acessível, botão dentro do ecrã no início/fim, sem scroll horizontal. Captura de 320 px inspeccionada. Sem publicação.
