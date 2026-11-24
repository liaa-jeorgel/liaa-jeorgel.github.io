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

## Melhoria orientada às recomendações do professor — 24/11/2026

### Dados conferidos nesta entrega

Foram lidos os cinco CSV indicados pelo autor, sem modificar os insumos ou a aplicação:

- PM2.5: 50.904 posições horárias únicas e consecutivas, 49.896 valores observados, 1.008 ausências, cobertura 98,0198%, 30 episódios; maior ausência 120 h, intervalo delimitador 121 h. Flags de observado/ausente coerentes. Valores originais preservados; não houve imputação.
- Meteorologia: 51.890 linhas, 51.744 timestamps únicos; 146 duplicações equivalentes nas cinco variáveis seleccionadas, sem conflitos nelas. Temperatura K→°C e direcção 360°→0°. Presença em todas as 50.904 horas da grade PM2.5. Não foi verificado se colunas meteorológicas não seleccionadas diferem nas duplicações.
- h1/h3/h6: 49.124/49.068/48.984 linhas e 39 atributos cada. Verificados todos os timestamps dos alvos e os valores correspondentes, lags e médias de PM2.5 e meteorologia e ausência de atributos não finitos. Reconstituídas as origens elegíveis (histórico completo anterior de 24 h e alvo exacto disponível); conjuntos coincidem integralmente, sem diferenças nestas verificações. Exclusões relativamente à grade: 1.780/1.836/1.920.
- Manifesto com nomes e SHA-256 em `assets/data/audit.json`; scripts de conferência e geração em `scripts/`. Não há autenticação do fornecedor, nova validação física ou medição de desempenho preditivo. A preparação estatística não certifica representatividade espacial. O relatório multivariado recebido continua identificado como `engineering_fixture`.

### Alterações entregues

- Gráfico real de médias diárias na apresentação e em Resultados; vistas por ano, faixa horária de ausências, tabela mensal e dados derivados descarregáveis. Dias parciais identificados; não há suavização adicional ou interpolação.
- Meteorologia no mesmo período e exemplo horário de alvos históricos 1/3/6 h, explicitamente distintos de previsões.
- Objectivo reduzido a frase e três blocos; evolução “previsto, entregue, evidência e falta”. Textos e descrições extensas preservados em `metodo.html`, com aviso de documentação histórica e ligação para o estado actual. C4 de contexto continua depois de Resultados e materiais; o cenário completo é acessível na página interna.
- Vídeo educativo de 177,37 s no leitor (2:57), 1280×720, H.264/AAC, 6.404.117 bytes, narração sintética portuguesa e 48 cues WebVTT. Transcrição e roteiro disponíveis. Imagens desenhadas por código com dados reais e cidade esquemática identificada; não há filmagem local nem gravação do autor. O acesso flutuante é ocultado durante a passagem pela área do vídeo para não tapar controles/legendas.
- Referências metodológicas de RF, LSTM e métricas numa comparação na página interna; não é revisão sistemática nem comparação de resultados de estudos de PM2.5. Página educativa com acesso ao mapa OpenAQ Explorer, sem alegar cobertura ou validação de Luanda.

### Verificações executadas

- Chromium, larguras 320/768/1440 px, com e sem JavaScript, movimento reduzido: dez secções e destinos do menu, títulos abaixo do cabeçalho, selecção anual, mapa comparativo por teclado. Sem erros de página ou deslocamento horizontal da página. Gráficos/tabelas grandes têm regiões de deslocamento próprias.
- Modo escuro em 360/1440 px: navegação, páginas de método e educação, permalinks de etapa/marco, modais e ausência de respostas locais HTTP ≥400. Sem overflow horizontal da página ou erros JS nesses cenários.
- Reproduzido o vídeo em Chromium, metadados 177,375 s, 1280×720, faixa de legendas `pt` com 48 cues e estado `showing`. Seek para 100 s e reprodução posterior confirmados com o ficheiro carregado como Blob (100,000 → 104,933 s); a legenda activa nesse instante corresponde à frase da cena 6. O servidor temporário Python não suporta pedidos Range, portanto o teste por Blob distingue o ficheiro da limitação da pré-visualização. Entrega por HTTP de produção com Range e Safari/Firefox ainda não testados.
- FFmpeg confirma H.264/AAC e sinal de áudio: média −19,3 dB e pico −5,4 dB, sem silêncio total. Os tempos das legendas usam os silêncios detectados no início/fim de cada frase; a repartição interna é proporcional ao número de palavras, não palavra a palavra. Não houve revisão humana integral da pronúncia nem de todos os quadros.
- Barra de progresso confirmada em 0% no início e 100% no fim, com o novo conteúdo.
- Parser: IDs únicos e referências/ficheiros locais válidos nas três páginas; XML de todos os SVG derivados válido. Sintaxe de `main.js`, `data-explorer.js`, `education.js` e `reading-progress.js`; `git diff --check` passou.
- Capturas inspeccionadas: resultados em 320 e 1440 claro; início, evolução e resultados em 360/1440 escuro; gráfico integral, apresentação final e leitor com legendas em 1440 claro. Não foram inspeccionados todos os estados de cada secção em todas as combinações.
- Cerca de 2.050–2.080 palavras inicialmente visíveis com JS nos cenários testados (aproximadamente 30% menos que as 2.960 da revisão anterior); sem JS há mais texto porque a comparação integral fica expandida. Não é a mesma contagem do portal. A página continua mais extensa que o exemplo MulitaMiner; a referência não foi tratada como limite obrigatório de palavras.

### Pendências e limites

Não foram executados treino, persistência, divisão cronológica ou avaliação preditiva. A gravação da aplicação a executar a preparação e a demonstração em aula continuam pendentes: a consulta GET da referência local não concluiu nos 12 s observados; não se conclui daí que a aplicação esteja indisponível. Pedidos de escrita foram bloqueados na consulta e não se executaram importações ou processamento. O vídeo entregue é educativo e não comprova execução da aplicação.

Permanecem pendentes revisão integral de acessibilidade com leitor de ecrã, testes com utilizadores, Safari/Firefox, Lighthouse e desempenho de rede em produção. Nenhuma avaliação, nota ou comentário pessoal do portal foi importado para o site. Os caminhos locais dos insumos não foram publicados. Não houve alteração ao código da aplicação, commit, push ou publicação.

Verificação final adicional em 360/1440 px: acesso flutuante visível no início, oculto junto ao vídeo e novamente visível ao regressar à apresentação, sem overflow. Os controles do vídeo ficam livres dessa sobreposição.

## Refinamento visual da concentração — 24/11/2026

Alterado apenas o painel de concentração e os SVG correspondentes (incluindo a miniatura que os reutiliza). Curva diária com preenchimento gradual, maior média diária anotada, legenda e ausências com cor distinta; três indicadores por período e leitura diária com cursor e controlo nativo de intervalo. Não há suavização, interpolação, classes de risco ou novas previsões.

Executado em Chromium a 360/1440 px, modos claro/escuro, com movimento reduzido:

- Indicadores de todo o histórico e 2020/2025/2026 comparados com o CSV diário: média ponderada pelas horas observadas, máximo horário e cobertura conferem nas duas casas apresentadas.
- Dia 31/03/2025: “Sem observação”, 0/24 horas; sem ponto desenhado a zero. Home e seta direita no controlo de intervalo percorrem os dias, com valor textual acessível actualizado.
- Clique real na curva actualiza o dia em foco. Movimentos acima de 10 px não seleccionam um dia, preservando o deslocamento táctil.
- Sem overflow horizontal da página e sem erros JS nos quatro cenários; a área do gráfico permite deslocamento próprio em ecrãs pequenos.
- Sem JavaScript, gráfico e tabela acessíveis. Com consulta do CSV bloqueada, gráfico estático continua disponível e indicadores de todo o histórico são ocultados quando se escolhe outro período.
- Parser confirma IDs únicos e destinos locais das três páginas, e XML dos SVG válido. Sintaxe de `data-explorer.js` e `git diff --check` passaram.
- Inspeccionadas capturas do painel em 1440 claro e 360 escuro e captura de viewport da curva final em 1440 claro. A imagem de painel completo inclui artefactos de composição dos elementos fixos; a leitura real foi conferida adicionalmente na captura de viewport.

Dados de origem, relatório, contagens, CSV derivados, vídeo e aplicação não foram alterados. Leitor de ecrã e outros motores de navegador não foram testados nesta revisão. Sem publicação.

## Botões de acção e movimento discreto — 24/11/2026

Links de acção (CTA, consultas, downloads, registos e ligações finais) passaram a usar um único botão de contorno discreto, com variante compacta em texto denso. Navegação, migalhas, citações, backlinks e links dentro de texto mantêm a aparência de link; os nós dos diagramas C4 e o botão flutuante da aplicação preservam o desenho próprio. Foram identificados 27 links em `index.html`, 41 em `metodo.html` e 12 em `pm25.html`. Os rótulos “Consultar método” dos cartões compactos e “Explorar este marco” dos cartões de jornada receberam o mesmo tratamento visual sem alterar os seus alvos.

A camada partilhada `assets/motion.js` aplica entradas únicas por `IntersectionObserver`, com verificação de reserva por `scroll`/`requestAnimationFrame`, animação apenas de opacidade e deslocação de 14 px, e respeito a `prefers-reduced-motion` e ao botão “Pausar movimento”. O cabeçalho ganha elevação mínima após sair do topo; a troca de período no gráfico tem crossfade curto. Sem JavaScript, nenhum conteúdo fica oculto.

Verificado em Chromium local: sintaxe de todos os JS, `git diff --check`, ausência de erros de consola e de scroll horizontal nas três páginas; todos os botões de acção visíveis com borda, raio e sem sublinhado. A secção 09 continua oculta e os seus links mantêm o estilo caso seja reactivada. Lighthouse: `index.html` 0,97 / 1 / 1, `metodo.html` 0,97 / 1 / 1 e `pm25.html` 1 / 1 / 1 (acessibilidade / boas práticas / SEO). A única falha restante é de contraste no `hero`, pré-existente; nenhum botão novo foi sinalizado. Nenhum commit, push ou publicação.

## Mapa global na secção 02 — 24/11/2026

### Pesquisa e critérios

- Fonte consultada: WHO Ambient Air Quality Database V8.0, actualizada a 30/06/2026, em `https://www.who.int/data/gho/data/themes/air-pollution/who-air-quality-database`. O ficheiro Excel oficial foi descarregado e analisado localmente: 45.742 registos e 125 países.
- Para cada uma das 19 cidades foi escolhido o registo mais recente da V8.0 com média anual de PM2.5 numérica e cobertura temporal de pelo menos 50%; os anos ficam entre 2014 e 2024. Ano, valor e cobertura foram lidos directamente da base. A selecção inicial apurou valores antigos em alguns casos; foi corrigida para privilegiar o ano mais recente, mesmo quando a linha não traz coordenadas.
- As posições desenhadas são aproximações do centro urbano, usadas apenas para localizar a cidade no globo; não são coordenadas de estações de medição nem resultados espaciais. A OMS adverte que a base não serve para classificar as cidades mais poluídas nem para comparações directas entre países; essa ressalva está no mapa e na tabela textual.
- Angola não tem registos na V8.0 (`AGO rows 0`); Luanda aparece como foco do estudo, sem valor numérico atribuído. A análise do projecto continua baseada em estimativas OpenWeather, sem validação por sensores locais.
- Contornos: Natural Earth `ne_110m_admin_0_countries` (domínio público), simplificados com Ramer–Douglas–Peucker e embutidos como SVG inline. Angola recebe caminho próprio e destaque; a Antártida foi omitida.

### Implementação

- `index.html` e `metodo.html`: figura na coluna esquerda de `.context-grid`, imediatamente abaixo do texto «A qualidade do ar começa por aquilo que nem sempre conseguimos ver.». A figura agrupa lead e mapa em `.context-left`.
- SVG com 20 nós (19 cidades + Luanda), 21 arcos esquemáticos, rótulos nos pontos de referência, legenda, três controlos, leitura acessível actualizada e 20 botões de selecção. As linhas ligam regiões; não representam transporte de ar nem fluxos de dados.
- `<details>` com tabela de 20 linhas, `caption`, `scope`, unidade `µg/m³`, ano e cobertura; funciona sem JavaScript. A fonte OMS e os contornos Natural Earth estão citados no rodapé da figura.
- `assets/world-map.js`: melhoria progressiva, sem pedidos remotos. Selecciona por clique, ponto, foco e teclado (Enter/Espaço); alterna as ligações e aplica o zoom centrado em Luanda. Respeita `prefers-reduced-motion` e a classe `motion-paused` do botão «Pausar movimento». Sem JavaScript, o SVG, os rótulos e a tabela permanecem visíveis.
- `assets/style.css`: traços e nós uniformes, sem escala de cores comparativa; animações curtas de desenho e entrada, desactivadas na impressão, no movimento reduzido e quando o movimento está pausado. O painel expansível recebeu `position:relative` para manter o indicador `+` dentro do resumo.

### Verificações executadas

- `node --check` em todos os scripts e `git diff --check`: passaram.
- Chromium local, `index.html` e `metodo.html`: 20 nós, 21 ligações, 20 botões de selecção e 20 linhas na tabela; leitura inicial «Luanda, Angola». Sem erros de consola e sem deslocamento horizontal da página.
- Interacção por clique e por Enter: Lima e Deli actualizam o painel com ano, média e cobertura correctos; apenas as ligações do ponto seleccionado ficam realçadas. O controlo «Focar Luanda» centra o mapa (matriz `2.2` com translação `-681,-450`) e «Vista global» repõe a transformação. «Ligações» esconde os arcos e actualiza `aria-pressed`.
- O botão global «Pausar movimento» remove as animações dos pulsos e dos nós e mantém os traços completos; o painel expansível e os controlos conservam foco visível.
- Lighthouse após o mapa: `index.html` 0,97 / 1 / 1 e `metodo.html` 0,97 / 1 / 1 (acessibilidade / boas práticas / SEO). A única falha continua a ser contraste pré-existente no `hero`; nenhum elemento do mapa foi sinalizado.
- Nenhum commit, push ou publicação.

## Melhoria do vídeo — 24/11/2026

### Conteúdo e rigor

- O roteiro passou de 8 para 9 cenas. Foi acrescentada uma cena sobre o contexto global da OMS V8.0: Angola sem registos, Luanda sem valor oficial atribuído e o mapa do site descrito como ligação esquemática, sem ranking nem comparação entre países.
- Os números das cenas foram lidos de `assets/data/audit.json`: 49.896 observações, 98,02% de cobertura, 1.008 horas ausentes em 30 episódios, maior lacuna de 120 horas e 121 horas entre as observações que a delimitam, 39 atributos por horizonte e 49.124/49.068/48.984 linhas em t+1/t+3/t+6. Nenhum desses números foi estimado para o vídeo.
- A cena horária usa o exemplo real de 02/12/2020 às 12h UTC. Os três pontos são identificados como alvos históricos, não previsões. A cena final atribui persistência, Random Forest e LSTM e MAE/RMSE à fase futura; não apresenta qualquer resultado preditivo.
- A ressalva sobre a origem atribuída à OpenWeather e sobre a conferência dos CSV foi mantida e reforçada: verificar ficheiros não autentica a origem física nem substitui sensores locais.
- O texto do leitor em `index.html` passou a indicar legendas alinhadas à fala e a distinção entre alvos históricos e previsões. `README.md` e esta verificação foram actualizados com a nova duração, tamanho e número de cues.

### Visuais e edição

- Cenas redesenhadas em 1280×720 com hierarquia tipográfica constante, cartões, gráfico real de médias diárias, ilustração horária com os alvos em t+1/t+3/t+6, globo esquemático com África realçada e quadro de etapas de preparação.
- A transição entre cenas é um crossfade de 0,65 s, com entrada/saída suaves no vídeo e no áudio. Foi removido o zoom contínuo da versão anterior: as cenas são estáticas e legíveis, sem movimento que distraia da leitura.
- A capa foi regenerada a partir da primeira cena. O ficheiro passou de cerca de 2,6 MB para 6,1 MB apesar da remoção do zoom, sobretudo pelo aumento de 8 para 9 cenas e pela narração mais longa; a codificação usa `crf 26`, `preset slow` e `tune stillimage`.

### Narração e legendas

- A voz sintética Joana (macOS) foi mantida, a 156 palavras/minuto, com 0,28 s entre frases e 0,70 s no fim de cada cena.
- `scripts/make_narration.py` converte cada fala para WAV mono a 22,05 kHz e detecta os silêncios inicial/final com `silencedetect=noise=-45dB:d=0.18`. Os tempos guardados em `/tmp/pm25-video/scenes.json` alimentam directamente a faixa WebVTT.
- As 48 cues foram repartidas proporcionalmente ao número de palavras dentro da parte falada de cada frase, com limite de 12 palavras/cue. Não é reconhecimento automático palavra a palavra; a última cue termina em 02:57,315, dentro da duração do vídeo.
- `assets/video/transcricao.txt` e `assets/video/producao.json` foram regenerados; o segundo inclui agora o número de cues e o método de alinhamento.

### Técnico e verificações

- MP4 H.264 High/level 4.0, yuv420p, 24 fps, 1280×720; áudio AAC mono 48 kHz a 80 kb/s; `+faststart` para reprodução progressiva. Sem autoplay e com `preload="none"` no site.
- `py_compile` passou em `scripts/make_narration.py` e `scripts/render_video.py`; `git diff --check` passou após as alterações.
- Chromium local: metadados 177,375 s, 1280×720, faixa `pt` com 48 cues em modo `showing`; seek para 100 s e reprodução até 104,933 s com o ficheiro carregado como Blob; legenda activa em 100 s corresponde à frase correcta. Sem erros de consola e sem deslocamento horizontal da página.
- FFmpeg: média de volume −19,3 dB e pico −5,4 dB, sem silêncio total. Não houve revisão humana integral da pronúncia, nem testes em Safari/Firefox ou com leitor de ecrã.
- Nenhum commit, push ou publicação.

## Evolução visual — 24/11/2026

Substituídas as linhas de entrega por percurso de seis etapas seleccionáveis, detalhe com visual próprio, previsto/entregue/pendência e evidência, indicação do ponto actual e acesso à próxima fase. Sem alterar dados científicos ou estados. JavaScript progressivo em `assets/evolution-explorer.js`, sem bibliotecas novas ou rotação automática.

Executado em Chromium, 320/768/1440 px, claro/escuro e movimento reduzido: seis etapas seleccionáveis, um detalhe visível, três campos por etapa, correspondência de âncora e painel, teclado (setas/Home/End), botões de navegação, acesso à próxima fase, deeplink para série e título abaixo do cabeçalho. Sem erros JS e sem scroll horizontal da página. Corrigida a largura mínima do contentor móvel para manter o deslocamento apenas na lista horizontal. Sem JS em 360/1440: seis detalhes visíveis e âncoras funcionais. Inspeccionadas capturas estáveis em 1440 claro e detalhe em 360 claro. Parser confirma IDs e referências locais válidas; sintaxe JS e diff verificados. Leitor de ecrã, Safari e Firefox não testados. Não houve publicação.

## Simplificação editorial e prioridade aos dados — 24/11/2026

### Alterações

- Acessos a Dados e Vídeo no início e no menu, preservando o acesso à evolução. Vídeo é subdestino da secção de materiais; não foi criada uma fase científica nova.
- Repetições reduzidas; protocolo pormenorizado de avaliação preservado em página interna. Lista de cidades do mapa recolhida num controlo nativo, com todos os pontos e a tabela mantidos. Secção de projectos relacionados permanece oculta como estava antes desta revisão.
- Vistas adaptadas ao ecrã até 650 px: concentração, temperatura e exemplo de horizontes. Ampliação opcional para o SVG integral e regresso à vista completa, sem bibliotecas adicionais. O SVG integral e os valores de origem permanecem inalterados.
- Guia para gravação autêntica e narração do autor em `metodo.html#guia-gravacao`. Não foram substituídas a voz sintética nem a apresentação educativa por uma simulação de gravação.
- Corrigida a indicação do menu: secções ocultas deixam de participar no cálculo da secção activa e a última secção é reconhecida no fundo da página, mesmo quando não pode atingir o limiar do cabeçalho.

### Verificações executadas

Chromium local, movimento reduzido, larguras 320/360/768/1440 px (360 em modo escuro):

- Dados e Vídeo levam aos destinos, indicam correctamente o elemento activo e mantêm os títulos abaixo do cabeçalho.
- Os três gráficos mostram a vista completa sem overflow da região no telemóvel; ampliação cria uma área interna deslocável, e o botão restitui a vista completa. A página não apresenta deslocamento horizontal.
- Selecção de 2025/2026 sincroniza o SVG móvel e integral; selecção de ano durante ampliação e posterior regresso verificadas.
- Home e seta direita no controlo diário, activação por Enter do botão de ampliação e selecção real por clique/toque: verificadas. Dia sem observação mantém o texto de ausência e não é convertido em zero.
- Lista expandida de cidades continua a permitir selecção e leitura no mapa. Não houve erros JS nem respostas HTTP locais >=400 nesses cenários.
- Sem JavaScript a 360 px: os três SVG móveis carregam ajustados ao ecrã, a tabela de concentração abre e todos os seis detalhes da evolução ficam disponíveis.
- Leitura inicial: 1.596 palavras a 320/360, 1.568 a 768 e 1.590 a 1440 px, por `innerText` após carregamento sem abrir detalhes; a contagem varia com controlos responsivos e não é comparável directamente à avaliação do portal.
- Todos os destinos do menu por teclado em 360/1440; valores e coordenadas da consulta diária nas duas vistas; links do protocolo e guia de gravação: verificados.
- SVG móveis de concentração confrontados com os agregados de origem: todos os 2.110 valores diários disponíveis na vista integral e os 31/365/363/363/364/360/264 nas vistas de 2020–2026 estão presentes, nas coordenadas esperadas dentro da precisão de arredondamento do desenho. Ausências continuam a interromper os segmentos. Nenhuma reamostragem.
- Parser: 67 IDs/87 referências no índice; 79 IDs/133 referências em método; 28 IDs/55 referências na página educativa; IDs únicos e âncoras/ficheiros locais válidos. XML dos SVG novos válido. Sintaxe dos scripts alterados e `git diff --check`: passaram.
- Inspeccionadas capturas de viewport do gráfico a 320 claro e início a 360 escuro. Capturas adicionais em 768/1440 geradas. Não foi realizada inspecção humana de todos os estados de ampliação em todas as larguras.

### Pendências

Não houve teste com utilizadores, leitor de ecrã, Safari/Firefox ou auditoria integral de acessibilidade nesta revisão. A nova voz e a gravação real da aplicação dependem de material autêntico; o vídeo e as suas fontes não foram alterados. Dados de origem, aplicação separada, ficheiros CSV e resultados científicos não foram modificados. Nenhum commit, push ou publicação.

## Atalhos flutuantes dos dados — 24/11/2026

Adicionadas três âncoras visuais imediatamente depois das estatísticas em Resultados e materiais: concentração, cobertura das duas fontes e três horizontes. Barra sticky confinada à secção, indicação activa e altura observada para reservar espaço nos destinos (incluindo vídeo). Sem novos componentes de processamento ou alteração dos dados.

Testes executados em Chromium a 320/768/1440 px, com movimento reduzido: três destinos por teclado, indicação activa, barra abaixo do cabeçalho, títulos abaixo da barra, ausência de overflow horizontal da página e de erros JS. Ao sair para Como funciona, a barra deixa a área visível. A indicação activa regressa à concentração durante deslocamento inverso. Sem JS a 360 px: ligação nativa à cobertura funcional e título desobstruído. Capturas de 320 e 1440 px inspeccionadas. IDs/âncoras locais, sintaxe JS e diff verificados. Outros navegadores e leitor de ecrã não testados nesta revisão. Não houve publicação.

### Ajuste posterior: atalhos sem flutuação

Retirado `position: sticky` da navegação de dados, incluindo o posicionamento móvel e a reserva dinâmica da sua altura. Os três botões permanecem abaixo das estatísticas e deslocam-se normalmente com a página. Mantidos os destinos e a indicação activa. Conferidas a sintaxe JavaScript e a ausência de problemas de whitespace; não repetida a suite de navegador nesta alteração de posicionamento.

## Separadores dos dados — 24/11/2026

Os três botões alternam o conteúdo correspondente no mesmo local, sem scroll ou comportamento flutuante. Aplicados papéis tablist/tab/tabpanel, selecção explícita, roving tabindex e navegação por setas/Home/End. Os links directos continuam válidos; a navegação global revela um painel oculto antes de posicionar o destino. Sem JS, as três áreas permanecem disponíveis. A transição de 200 ms respeita movimento reduzido e pausa global.

Chromium a 320 (escuro)/768/1440 px, movimento reduzido: os três cliques conservaram scrollY (tolerância inferior a 2 px); apenas um painel visível; selecção e painel correspondem; sem overflow horizontal da página ou erros JS. Teclado, foco, selecção de ano e carga dos gráficos passaram. Links directos ao painel de horizontes e à região interna de temperatura revelaram o conteúdo correcto. Sem JS a 360 px: três painéis acessíveis e ligação nativa funcional. Captura móvel inspeccionada. Parser de IDs/âncoras, sintaxe JS e diff verificados. Leitor de ecrã e outros navegadores não testados. Sem alteração dos dados nem publicação.

## Vídeo explicativo animado — 24/11/2026

Substituída a peça anterior por dez cenas didácticas: problema e dimensão das partículas, contexto global, duas fontes alinhadas, revelação do histórico, ausência sem preenchimento, operações da aplicação, atributos do passado, três alvos históricos, amostras elegíveis e comparação futura. Valores derivados dos mesmos CSV; ausência de resultados preditivos reiterada. Posições dos lags e blocos de lacuna identificados como esquemáticos. Média de três horas calculada dos valores reais anteriores à origem, sem usar a hora de origem ou alvos futuros.

Entregue: MP4 1280×720, 24 fps, H.264/AAC, 178,116 s no leitor, 3.192.996 bytes; voz sintética Joana; 48 cues de legendas, dez capítulos WebVTT, transcrição, poster e manifesto regenerados. Sem música, clonagem de voz ou gravação da aplicação. O guião e os scripts de produção foram actualizados; nada mudou nos ficheiros científicos de origem.

Verificações executadas:

- Chromium em 360 (escuro)/768/1440 px com movimento reduzido: dez capítulos presentes; selecção via Enter e clique em cinco pontos (incluindo primeiro e último); seek confirmado com tolerância <0,7 s; selecção não inicia reprodução automaticamente. Reprodução posterior e pausa funcionais.
- Leitor confirma 1280×720 e duração dentro de 2–3 minutos; faixas de capítulos (dez cues) e legendas disponíveis. Sem erros JS ou ficheiros HTTP locais em falta. Sem overflow horizontal da página. Sem JS a 360 px: ligações temporais nativas, transcrição e layout acessíveis.
- Pré-visualização com suporte HTTP Range para testar o seek sem a limitação do servidor Python simples. Entrega em produção permanece não testada.
- Botão adicional de ecrã inteiro verificado em Chromium; resultado assíncrono observado. O código oferece instrução de controlo nativo em caso de recusa pelo navegador. Ocultação do acesso flutuante junto ao vídeo/chapítulos conferida após a actualização dos observadores.
- FFmpeg: duração 2:58,12; áudio AAC presente, média −19,2 dB e pico −5,6 dB. Verificadas as 48 legendas em ordem, sem sobreposição temporal e dentro do filme. Alinhamento é proporcional dentro da fala detectada; não foi feita revisão humana integral da pronúncia e de cada palavra.
- Comparação de frames em instantes diferentes confirmou alteração visual nas cenas de cidade, série, lacunas, preparação, atributos, alvos e amostras. Inspeccionados frames finais das cenas 1/5/7/8/10 e capturas do leitor em 360 escuro/1440 claro, além dos capítulos em 360 claro. Área inferior sem diagramas foi reservada para as legendas.
- Sintaxe JS, parser de IDs/âncoras/ficheiros, validade dos links MP4 com fragmento temporal e diff verificados. Caches Python de compilação repostos ao estado anterior para não incluir alterações binárias incidentais.

Limites: testes com utilizadores, leitor de ecrã, Safari/Firefox e revisão audiovisual humana completa continuam pendentes. A voz do autor, imagens locais autênticas e gravação real da aplicação não foram fabricadas. Sem alteração da aplicação, commit, push ou publicação.

## Mapa: OpenWeather e estatísticas de Luanda — 24/11/2026

### Fonte e cálculo

Lido o CSV preparado de PM2.5 indicado anteriormente pelo autor. SHA-256 confere com `assets/data/audit.json`. Novo gerador `scripts/build_map_statistics.py`: oito períodos (histórico e 2020–2026), grade única e horária, média das concentrações presentes, máximo, mínimo, contagens e cobertura. Média de todo o histórico confere com a auditoria anterior dentro de 1e-9. Valores de referência: média 24,440456148789483 µg/m³; máximo horário 568,32 µg/m³; cobertura 98,01980198019803%; 49.896 observações em 50.904 horas, 1.008 ausentes. Anos parciais 2020/2026 reconhecidos a partir dos limites UTC reais.

A referência geográfica não autentica a origem física dos ficheiros. Não foi executado treino nem criada validação instrumental. As estatísticas não são valores OMS, não medem toda a cidade e não foram calculadas do ficheiro meteorológico. Dados OMS anteriores permaneceram intactos e separados.

### Entrega

Vista padrão OpenWeather com Luanda, select por período, média/máximo/cobertura, contagens, período UTC e JSON descarregável. Fonte declarada em cada vista. OMS V8.0 acessível por controlo separado; nenhum valor OMS é apresentado como OpenWeather. Outros pontos da vista OpenWeather informam que falta histórico da respectiva cidade neste site. Sem API, credenciais ou conteúdo remoto carregado pelo mapa. Marcadores continuam geográficos e aproximados, sem alegar estações certificadas ou movimentos de ar. Tabelas das duas fontes mantidas separadas, com acesso sem JS.

### Verificações executadas

- Chromium em 360 (escuro)/768/1440 px, movimento reduzido: valores apresentados nos oito períodos confrontados com o JSON calculado; média, máximo e cobertura conferem. 2020/2026 mostram aviso de ano parcial.
- Nova Iorque na vista OpenWeather: sem histórico, sem reutilização de 7,07 da OMS. Troca para OMS apresenta a média e fonte correctas; Luanda na OMS informa ausência de valor. Voltar a OpenWeather restaura os indicadores de Luanda.
- Troca de fonte por teclado, selecção de marcadores por Enter, foco em Luanda, vista global e lista de cidades: passaram. Sem erros JS, sem pedidos de rede externos e sem overflow horizontal da página.
- Verificação interna dos contentores de fontes, cabeçalho e estatísticas em 320/650/768/1024/1440: scrollWidth não excede clientWidth; números e controlos não ficam cortados.
- Sem JS em 360 px: indicadores de Luanda legíveis, tabela OpenWeather de oito períodos e tabela OMS de vinte cidades acessíveis por details.
- Capturas inspeccionadas: indicadores em 360 escuro e mapa/selectores em 1440 claro. Não houve inspecção visual de todas as combinações e períodos.
- Sintaxe de `world-map.js`, parser de IDs/âncoras/ficheiros locais e `git diff --check`: passaram. Sem alteração aos CSV originais, dados OMS, vídeo ou aplicação.

### Limites

Não foram recolhidos históricos OpenWeather de outras cidades, autenticada a origem física, medido desempenho preditivo ou validada representatividade por sensores de Luanda. A API oficial foi consultada como documentação, sem pedidos autenticados. Revisão por leitor de ecrã, outros navegadores e teste com utilizadores continuam pendentes. Não houve commit, push ou publicação.

## Rodapé partilhado — 24/11/2026

Rodapé actualizado no índice, método e página educativa, com identidade académica, navegação, materiais, acesso à aplicação e regresso ao início. Mantidas a paleta e a tipografia existentes; sem dependências novas ou contactos inventados.

Chromium: nove cenários (três páginas × 320/768/1440 px, 320 em escuro), movimento reduzido. Links recebem foco por teclado, regresso ao início aponta para a âncora correcta, atalho de vídeo no índice funciona, aplicação usa nova aba com noopener/noreferrer. Sem overflow horizontal da página ou erros JS. Texto final fica acima do acesso flutuante. Sem JS a 360 px: âncora nativa para materiais funcional. Inspeccionadas capturas do rodapé do índice em 1440 claro e 320 escuro. Parser valida IDs e destinos locais das três páginas; sintaxe JS e diff verificados.

A verificação detectou incompatibilidade anterior do script de mapa partilhado com a versão OMS da página de método (ausência do bloco JSON de estatísticas OpenWeather). A inicialização foi protegida e mantém essa página em vista OMS, sem inventar estatísticas nem remover controlos. Testes nas três páginas repetidos e passaram. Não foram executados leitor de ecrã ou testes noutros navegadores nesta revisão. Sem publicação.

## Feedback de exploração — 24/11/2026

Implementados leitores de valores por rato/toque nos três gráficos, indicadores de posição, controlos nativos e realces discretos em cartões. Dados provenientes dos CSV existentes, sem alteração de conteúdos científicos.

Executado em Chromium: 360 px escuro e 1440 px claro, movimento reduzido; hover dos três gráficos, lacuna de PM2.5 de 31/03/2025 sem valor zero, Escape e reabertura, temperatura inicial de 27,20 °C, setas/Home/End, alvo histórico de +1 h de 10,49 µg/m³. Toque em 360 px confirmou alvo de +3 h de 8,75 µg/m³. Sem erros JS ou overflow horizontal nos cenários. Sem JS em 360 px, os três painéis e os gráficos permanecem acessíveis. Capturas inspeccionadas: concentração em 360 escuro e temperatura em 1440 claro. Sintaxe JS, IDs/destinos locais e diff verificados.

Pendentes: leitores de ecrã, Safari/Firefox, dispositivos físicos e testes com utilizadores. Não foi executada medição formal de desempenho; eventos de movimento são agrupados com requestAnimationFrame. Sem publicação.
