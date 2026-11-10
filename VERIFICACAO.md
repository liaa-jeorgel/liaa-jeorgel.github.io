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
