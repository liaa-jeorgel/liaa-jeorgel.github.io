# PM2.5 / Luanda

## Versão orientada aos dados — 24/11/2026

A apresentação actual está em `index.html`; as explicações científicas completas anteriores foram preservadas em `metodo.html`, identificado como documentação detalhada. Esta revisão prevalece sobre descrições históricas abaixo sobre ausência de gráfico, de vídeo ou materiais pendentes. `pm25.html` conserva o texto educativo e acrescenta acesso ao mapa mundial OpenAQ, sem o apresentar como validação de Luanda.

- Série real na apresentação inicial e em Resultados e materiais: médias diárias de PM2.5, selecção de ano, faixa horária de lacunas, tabela mensal acessível e CSV derivados para download.
- Temperatura no mesmo período e exemplo horário com os alvos históricos em t+1, t+3 e t+6. Os alvos não são previsões; médias diárias não são máximos horários nem garantem dias completos.
- Objectivo numa frase e três blocos; evolução com previsto, entregue, evidência e falta; aprofundamento C4 e método numa página interna.
- Mapa global na secção 02 com contornos Natural Earth e 19 cidades seleccionadas da base OMS V8.0 (2026); Angola realçada e Luanda identificada como foco do estudo, sem valor OMS. As posições são aproximadas, as ligações são esquemáticas e não representam fluxos de ar ou dados; os valores não são usados para classificar cidades nem comparar países.
- Vídeo educativo próprio de 2:57, 1280×720, cerca de 6,1 MB, H.264/AAC, narração sintética Joana (macOS), 48 cues de legendas WebVTT alinhadas à fala e transcrição. Nove cenas incluem contexto global com a ressalva da OMS, contagens auditadas e a distinção entre alvos históricos e previsão. Não reproduz filmagem local, não imita o autor e não é gravação de execução da aplicação. `preload="none"`; não inicia automaticamente.
- Conferência independente de cinco CSV fornecidos pelo autor: `assets/data/audit.json` contém nomes e SHA-256 dos insumos, contagens e resultados. Os insumos originais (cerca de 80 MB) não foram copiados para o site; apenas derivados e o PDF de preparação disponibilizado foram incluídos.

### Reproduzir os derivados

Python 3, biblioteca padrão. Os cinco argumentos são caminhos locais escolhidos pelo responsável, não URLs da aplicação:

```sh
python3 scripts/build_site_data.py --pm25 /caminho/pm25.csv --h1 /caminho/h1.csv --h3 /caminho/h3.csv --h6 /caminho/h6.csv --weather /caminho/meteorologia.csv
python3 scripts/build_site_charts.py
```

O gerador verifica grade horária única, flags, valores finitos, timestamps exactos dos alvos, todos os 39 atributos e a igualdade entre as origens elegíveis reconstruídas e cada CSV supervisionado. Meteorologia: temperatura declarada em Kelvin convertida para °C; direcção 360° normalizada para 0°; duplicações colapsadas apenas quando equivalentes nas cinco variáveis seleccionadas. `pressure` é usado como pressão ao nível do mar conforme a declaração fornecida no relatório; isso não autentica a semântica física do fornecedor. Não há treino, imputação, remoção de extremos ou nova execução do motor da aplicação.

O exemplo horário é 02/12/2020 às 12h UTC, com histórico de 24 h e alvos exactos. Agregações diárias usam apenas os valores presentes; o CSV derivado inclui horas observadas/esperadas/ausentes. Médias meteorológicas são calculadas nas horas da grade PM2.5, incluindo as horas em que o PM2.5 está ausente. Não se calcula média aritmética de direcção do vento.

### Reproduzir o vídeo

No macOS, com a voz portuguesa Joana instalada e um ambiente Python com Pillow e imageio-ffmpeg:

```sh
python3 scripts/make_narration.py
python3 scripts/render_video.py
```

Roteiro público: `assets/video/roteiro.json`. A narração usa `say`; temporários em `/tmp/pm25-video`. Os silêncios no início/fim de cada frase são detectados para posicionar as legendas, que depois são repartidas proporcionalmente dentro da fala; não é reconhecimento palavra a palavra. As imagens são desenhadas por código com os derivados dos dados; as transições são curtas e não há zoom. A voz é sintética, não gravada pelo autor. O leitor nativo disponibiliza pausa, legendas e controles; não há reprodução automática.

### Limites que permanecem

A origem física e o produto OpenWeather não foram autenticados. O relatório multivariado recebido mantém a classificação `engineering_fixture`; não se removeu essa classificação nem se transferiu a aprovação para os dados históricos. A presente conferência é dos CSV fornecidos, cujas contagens e atributos coincidem com o relatório; não é validação científica integral ou certificação operacional. A hipótese de atraso de 1 h continua retrospectiva. A diferença espacial de aproximadamente 3,57 km vem das coordenadas declaradas, sem equivalência ambiental demonstrada.

Persistência, treino RF/LSTM, avaliação e definição do protocolo cronológico continuam pendentes. A documentação primária dos métodos está comparada em `metodo.html#literatura`, sem alegar revisão sistemática ou transferir métricas de outros trabalhos. O gráfico e o vídeo não estabelecem causas de picos.

A demonstração em aula e uma gravação da aplicação a executar a preparação não são comprovadas por esta entrega. A consulta de referência da aplicação local foi tentada em modo de leitura, mas não concluiu durante a observação. Não foram executadas operações de escrita, importação ou processamento nessa aplicação. Nenhum código da aplicação foi alterado, e não houve commit, push ou publicação.

---

Site académico individual de **Jeorgel Chitende**, na disciplina Laboratório de Inteligência Artificial Aplicada, PPGES / Universidade Federal do Pampa — UNIPAMPA.

**Previsão de Curto Prazo de PM2.5 com IA em Contexto Urbano Angolano.**

Site estático, sem backend, frameworks, fontes externas, cookies, analytics ou dependências de execução. A aplicação de processamento de dados permanece separada deste repositório. Nenhuma publicação foi realizada nesta entrega.

## Execução local

Na raiz do repositório:

```sh
python3 -m http.server 8000
```

Abrir http://localhost:8000. Encerrar com Ctrl+C. Também é possível abrir `index.html` directamente, embora um servidor local reproduza melhor o ambiente de publicação.

## Modo escuro

O site segue automaticamente o tema claro ou escuro do sistema através de `prefers-color-scheme`. Não existe botão de tema nem preferência guardada: a página acompanha a alteração do sistema sem JavaScript. A impressão força sempre o tema claro. As cores estão centralizadas em `:root` e no bloco `@media (prefers-color-scheme: dark)` de `assets/style.css`; a ilustração SVG usa classes próprias para receber a variante escura.

## Organização

- `index.html`: conteúdo científico, navegação, metodologia e diário.
- `assets/style.css`: estilos responsivos e variáveis de cores, espaçamentos e tipografia em `:root`.
- `assets/main.js`: menu móvel com estado acessível, fecho por ligação e tecla Escape.
- `assets/motion.js` e `assets/world-map.js`: entradas discretas partilhadas e interacção progressiva do mapa global da secção 02.
- `assets/favicon.svg`: ícone original, sem logótipos institucionais.
- `assets/social.png`: imagem de partilha PNG 1200 × 630 usada em `og:image`. O SVG anterior é preservado como arte de origem da primeira versão.
- `materiais/`: destino dos relatórios e imagens reais; ficheiros ainda não fornecidos.
- `.nojekyll`: permite servir os ficheiros directamente pelo GitHub Pages.

O conteúdo, os links, as âncoras e os detalhes expansíveis funcionam sem JavaScript. Sem JavaScript, o menu permanece visível também no telemóvel.

## Estado científico desta revisão — 10/11/2026

A aquisição, auditoria, limpeza e integração e construção da série temporal multivariada estão **Concluídas**, conforme os dados do relatório de consolidação fornecidos pelo autor no pedido desta revisão. A actividade actual é a **consolidação e demonstração da série temporal multivariada**. A próxima fase é a baseline de persistência; treino, validação e avaliação de Random Forest e LSTM continuam planeados.

Resultados atribuídos ao relatório: 50.904 instantes horários UTC; 49.896 instantes com PM2.5; 39 atributos temporais; cinco variáveis meteorológicas, incluindo pressão **ao nível do mar**. As amostras elegíveis/excluídas são 49.124/1.780 (1 h), 49.068/1.836 (3 h) e 48.984/1.920 (6 h), em universos independentes de 50.904 origens por horizonte. O relatório regista 240/240 verificações e 1.200 instantes amostrados; o site não executou uma nova auditoria científica destes dados.

As ausências de concentrações foram preservadas sem imputação. A disponibilidade de uma hora para ambas as fontes é uma hipótese retrospectiva, sem comprovação de latência operacional. Não há resultados preditivos publicados.

### Documentos efectivamente consultados

Encontrados na pasta `docs` da aplicação separada `previsao-pm25-luanda`, em Unipampa / AL5132:

- `implementacao_etapa3_incremento7.md`, de 28/10/2026: exportação PDF, testes controlados e dependência da validação meteorológica nessa data.
- `diagnostico_final_fontes_meteorologicas.md`, de 29/10/2026: diagnóstico de leitura, erros de mapeamento, unidades e semântica da pressão; não executou integração histórica.

Ambos contêm caminhos pessoais, hashes, identificadores e referências a artefactos locais. Foram consultados, mas não copiados para os downloads públicos. Os seus estados históricos são apresentados com a data correspondente, sem os confundir com o marco posterior de consolidação informado pelo autor.

### Pendências

- `Relatorio_Semanal_Etapa3_Pipeline_Atualizado(1).docx` não foi encontrado no repositório, anexos, Unipampa, Downloads ou Documents. Não foi consultado nem copiado. Os resultados de consolidação foram transcritos do pedido, sem alegar validação independente do Word.
- Quando disponibilizado, verificar o conteúdo e eventuais dados sensíveis; copiar o Word **sem alterações** para `materiais/relatorio-consolidacao-etapa3.docx` e só então criar ligações no marco e na secção de materiais. Se houver conteúdo sensível, resolver a disponibilização antes de o tornar público, sem alterar silenciosamente o original.
- A data exacta do marco de consolidação não foi indicada. Manter o marco separado das entregas datadas; não usar data de upload nem de edição do site.
- O pré-preenchimento de configuração de demonstração consta apenas como proposta. Não foi verificado no código/testes da aplicação e não é anunciado como implementado.
- A disponibilização pública de outros materiais exige revisão de dados pessoais e referências locais. Não existem links de download para documentos ausentes.
- Contactos pessoais, novas referências científicas e resultados preditivos só serão incluídos quando fornecidos.

As fontes públicas EPA e OpenWeather permanecem as da versão anterior; não foi feita nova consulta web nesta revisão.

## Editar conteúdos e acrescentar entregas

Editar os textos directamente no HTML. Alterar os estados de forma individual apenas com suporte documental; evitar substituições globais. A área `REGISTOS DATADOS` em `index.html` contém as entregas. Inserir cada entrega **antes das anteriores**, dentro de `.dated-entries`, usando o modelo abaixo. Preservar o marco sem data na área `.milestone`, separada. Substituir todos os campos e incluir apenas ficheiros existentes.

```html
<details>
  <summary>
    <span class="timeline-meta"><time datetime="AAAA-MM-DD">DATA REAL</time> · ENTREGA</span>
    <span class="timeline-title">Título confirmado</span>
    <span class="expand">Ver detalhes <span aria-hidden="true">+</span></span>
  </summary>
  <div class="entry-body">
    <h4>Objectivo</h4><p>Objectivo da entrega.</p>
    <h4>Actividades realizadas</h4><p>Preparei… / Analisei…</p>
    <h4>Resultados e evidências</h4><p>Resultado verificável.</p>
    <h4>Decisões e dificuldades</h4><p>Decidi… / Identifiquei…</p>
    <h4>Próximos passos</h4><p>Pretendo…</p>
    <h4>Materiais associados</h4>
    <p><a href="materiais/NOME-REAL.pdf">Consultar relatório (PDF)</a></p>
  </div>
</details>
```

Usar primeira pessoa do singular nos relatos. A data de uma entrega não é necessariamente a data da edição do site.

## Adicionar relatórios, apresentações e imagens

1. Copiar o material para `materiais/` com nome descritivo, sem espaços ou acentos.
2. Adicionar link real no registo correspondente e na secção `#materiais`, indicando formato e, se conhecido, tamanho.
3. Para download, adicionar o atributo `download` a um link local. Não criar links antes de o ficheiro existir.
4. Imagens devem ser optimizadas (WebP ou PNG), com `alt` descritivo, dimensões explícitas e `loading="lazy"` fora da área inicial.
5. Substituir a mensagem de ausência de materiais quando existirem evidências. Cada gráfico deve identificar período, unidade, origem e limitações; publicar métricas apenas com avaliação documentada.

## Publicação no GitHub Pages — manual

O destino previsto é https://liaa-jeorgel.github.io, organização `liaa-jeorgel`, repositório `liaa-jeorgel.github.io`.

1. Rever os conteúdos e os estados pendentes.
2. Fazer commit dos ficheiros e enviar para a branch `main` do repositório indicado.
3. Em GitHub → **Settings → Pages → Build and deployment**, seleccionar **Deploy from a branch**.
4. Seleccionar **main** e **/(root)**; guardar.
5. Aguardar a conclusão da publicação e verificar o endereço público, âncoras e ficheiros.

Não é necessário build ou workflow próprio. O `index.html` já está na raiz. Não se deve copiar a aplicação de processamento nem chaves da OpenWeather para este site público.

## Verificação

Os resultados efectivamente medidos nesta revisão estão em `VERIFICACAO.md`. Os testes do site não representam uma repetição dos testes científicos da aplicação nem das verificações do relatório.

Para repetir a revisão manual: servir localmente, verificar a 360, 768 e 1440 px, navegar com Tab/Enter/Escape, abrir as entregas e repetir sem JavaScript. Para Lighthouse, usar Chrome DevTools → Lighthouse; procurar ≥95 em cada categoria e registar apenas valores medidos.

Nenhum commit, push ou publicação foi executado nesta tarefa. A pasta `.git` foi preservada.

## Harmonização visual com a aplicação — 10/11/2026

A aplicação foi aberta em `http://127.0.0.1:5173/` e comparada visualmente. Foram consultados, apenas em leitura, `frontend/src/style.css`, `frontend/src/multivariate.css` e `frontend/src/App.vue` na aplicação separada. As variáveis e os estilos calculados confirmaram:

| Função | Valor da aplicação usado no site |
|---|---|
| Destaque / foco | `#f96501` |
| Destaque forte / botão principal | `#b84b00` |
| Fundo de destaque | `#fff3e8` |
| Texto principal | `#171717` |
| Texto de corpo / secundário | `#525252` / `#737373` |
| Fundo / superfície | `#fafafa` / `#ffffff` |
| Borda / borda forte | `#e5e5e5` / `#d4d4d4` |
| Borda de destaque | `#f2c9aa` |

A pilha tipográfica é a mesma: `Inter, ui-sans-serif, system-ui, -apple-system, sans-serif`. Inter é utilizada apenas se estiver disponível localmente; nenhuma fonte é descarregada. Foram harmonizados títulos, botões (raio 5 px), painéis (9 px), badges, tabelas, foco e ilustração, incluindo favicon e imagens sociais. Os estados continuam identificados por texto; os planeados têm tons neutros e os concluídos usam o destaque suave, como os estados preparados da aplicação.

A estrutura académica e o conteúdo científico foram preservados. Nenhum código ou dado da aplicação foi alterado. Não foram acrescentadas bibliotecas nem publicado o site.

## Experiência de leitura e transparência — revisão de 10/11/2026

A página inicial explicita tema, origem dos dados, autor, instituição, actividade actual e próxima actividade. A navegação usa Início, Contexto, Problema, Solução, Etapas, Evolução e Materiais, preservando os IDs existentes para compatibilidade com ligações anteriores.

A secção «Como o projecto funciona» mantém as oito etapas, agora com resumo visível e detalhes nativos para entradas, operação, saídas e verificação. Ao editar, distinguir operações concluídas de critérios previstos e manter o estado textual de cada etapa. Os detalhes não executam processamento: descrevem o que a aplicação faz e o que está planeado.

Ligações permanentes incluem `#etapa-aquisicao`, `#etapa-auditoria`, `#etapa-integracao`, `#etapa-serie`, `#etapa-persistencia`, `#etapa-treino`, `#etapa-avaliacao`, `#etapa-relato`, `#marco-consolidacao`, `#entrega-2026-10-29`, `#entrega-2026-10-28` e `#criterios-exclusao`. Novas entregas devem receber IDs únicos e uma ligação no índice do diário. Acrescentar também as etapas relacionadas.

`assets/main.js` indica a secção actual com `aria-current="location"`, ajusta a margem das âncoras à altura real do cabeçalho e abre detalhes quando o visitante usa uma ligação directa. Sem JavaScript, o cabeçalho deixa de ser fixo para não esconder destinos; navegação e detalhes continuam nativos.

Os indicadores têm unidade, universo e interpretação. A fonte comum aparece junto dos três indicadores e a tabela tem descrição associada por `aria-describedby`. Ao adicionar resultados, indicar sempre fonte e suporte, separar preparação de previsão e não repartir exclusões por motivos sem contagens documentadas. As explicações incluem ausência versus zero, grade versus valores preenchidos e atributos derivados versus variáveis ambientais.

A imagem `assets/aplicacao-preparacao.webp` é uma captura real da aplicação aberta em 10/11/2026, recortada e redimensionada para 1200 × 500, sem simular funcionalidades. Mostra apenas a interface inicial, sem dados carregados ou resultados. Foi revista visualmente: a região publicada não contém caminhos pessoais ou dados de utilizadores. Está fora da área inicial, com dimensões, texto alternativo e carregamento diferido.

A identidade foi novamente conferida no navegador e no CSS da aplicação; os valores laranja/preto/cinza foram preservados. Não foram alterados código ou dados da aplicação. Não houve testes com utilizadores: a avaliação desta revisão é técnica e visual. Continuam pendentes o Word de consolidação para consulta/download e uma auditoria Lighthouse, não disponível nas ferramentas consultadas.

## Navegação lateral — 16/11/2026

No computador, as secções aparecem como opções na lateral esquerda; ao seleccionar uma, o conteúdo correspondente é apresentado à direita. No telemóvel, o botão Menu abre as mesmas opções. Autor/referências e projectos relacionados também têm destinos próprios.

O JavaScript usa o atributo `hidden` para alternar as nove secções, preservando as âncoras, ligações entre etapas e entregas e o histórico do navegador. Sem JavaScript, todas as secções permanecem visíveis. Ao imprimir, todas voltam a ser apresentadas. Para adicionar uma secção, criar um `section` directamente em `#principal`, com ID único, e a respectiva ligação no menu.

## Redesenho editorial e tecnológico — 16/11/2026

A identidade passou a um caderno de investigação: barra lateral escura numerada, conteúdo à direita, títulos editoriais em Georgia (fonte local), metadados em fonte monoespaçada do sistema e destaque laranja preservado. Os modos claro e escuro seguem a preferência do dispositivo. O CSS foi reorganizado num único ficheiro, sem carregar fontes, frameworks ou bibliotecas.

Referências de design consultadas, sem ranking ou alegação de vínculo institucional:

- Stanford HAI — https://hai.stanford.edu/research — página consultada por web e navegador, com captura visual inspeccionada.
- MIT Media Lab — https://www.media.mit.edu/research/ — conteúdo e organização de pesquisa consultados pela ferramenta web; o navegador excedeu o tempo de navegação.
- MIT Senseable City Lab — https://senseable.mit.edu/ — referência de investigação urbana consultada na pesquisa; a página não forneceu texto legível à ferramenta web e a captura no navegador excedeu o tempo de espera por fontes. Não se afirma inspecção visual completa ou reprodução das suas animações.

Estas referências orientaram a decisão de dar mais destaque à pergunta de investigação, aos capítulos e ao percurso dos dados. Não foram copiadas imagens, marcas, código ou conteúdo científico dessas instituições.

### Animações e interacções

- Entradas suaves e escalonadas dos elementos de cada capítulo, com Web Animations API.
- Revelação discreta das etapas ao entrarem no ecrã, sem ocultar o conteúdo base.
- Diagrama SVG original: fontes convergentes, órbitas e fluxo conceptual para os horizontes.
- Selector de 1/3/6 horas com texto explicativo acessível e `aria-pressed`. É uma exploração conceptual; não calcula previsões.
- Transições nos links, cartões, botões e detalhes expansíveis.
- Botão global de pausa na lateral e checkbox nativa para pausar o diagrama. Movimento reduzido desactiva animações e transições.
- Ligações de capítulo anterior/seguinte, identificação do capítulo actual e histórico preservado.

O texto científico e as contagens confirmadas foram mantidos. O título do SVG e a legenda explicitam os limites da ilustração. As animações não geram valores ou percentagens de progresso científico. Sem JavaScript, todas as secções e os detalhes continuam acessíveis; os controlos do explorador que dependem de JavaScript ficam ocultos. Não houve publicação.

## Navegação superior — 16/11/2026

A pedido do autor, a barra lateral e a apresentação como dashboard foram removidas. O menu fica no topo e as nove secções são novamente apresentadas numa página contínua. O menu compacto aplica-se até 1000 px; âncoras usam a altura real do cabeçalho. Mantêm-se as animações, o explorador conceptual e os modos claro/escuro. Esta organização substitui a navegação lateral descrita nas revisões anteriores.

## Barra de progresso de leitura

Indicador fixo de 3 px imediatamente abaixo do menu, posicionado pela altura real do cabeçalho (`--header-offset`), independente do layout e sem interceptar cliques, na cor `--accent`. Calcula a razão entre `scrollTop` e `scrollHeight - clientHeight`, limitada a 0–100%; oculta-se quando não há área para scroll. Não representa progresso científico do projecto.

O JavaScript agrupa actualizações em `requestAnimationFrame`, usa escuta de scroll passiva e recalcula em resize, carregamento de imagens, alterações de conteúdo e de dimensão. O `MutationObserver` ignora alterações da própria barra. Há uma transição de 100 ms, desactivada com movimento reduzido. Sem JavaScript ou na impressão, a barra permanece oculta. O elemento tem nome acessível e valor percentual, sem anúncios a cada scroll.

## Comparação de projectos em foco

Os cartões de projectos relacionados foram removidos. A secção tem um índice tipográfico com cinco botões e uma área única que compara o projecto seleccionado com PM2.5 em Luanda. Rato (hover), foco, clique e toque activam a selecção; setas percorrem as opções, Home/Escape regressam à referência e End selecciona o último projecto. Os botões usam `aria-pressed` e a selecção tem anúncio discreto acessível.

A fonte dos dados continua a ser a tabela integral no HTML, dentro de «Consultar comparação completa». O JavaScript deriva o comparador dessa tabela, sem duplicar os conteúdos científicos em estruturas de dados independentes. Sem JavaScript, a tabela integral aparece aberta. Preservaram-se os IDs antigos dos projectos nas linhas da tabela, as ligações ao portal e as ressalvas de autoria. Para editar uma comparação, actualizar a linha correspondente e, se necessário, os rótulos curtos no JavaScript.

## Mapa comparativo dos projectos

A secção apresenta agora uma matriz de leitura rápida: cinco projectos nas colunas e quatro dimensões nas linhas (dados, objectivo, ponto comum e diferença central). A selecção realça uma coluna sem esconder a visão de conjunto. Hover, foco, clique, toque e teclas de direcção funcionam; Home/Escape regressam ao meu projecto e End selecciona o último.

No telemóvel, apenas o mapa se desloca na horizontal, mantendo a coluna das dimensões fixa. Abaixo, o projecto em foco mostra o título completo, autoria e ressalvas, com ligação à fonte. A tabela integral continua numa área expansível e aparece aberta sem JavaScript. Os botões do mapa ficam desactivados sem JavaScript; os conteúdos estáticos continuam legíveis.

Para editar, actualizar as sínteses curtas no mapa e os textos detalhados na tabela integral. A autoria e os links do detalhe em foco são derivados desta última. O mapa é uma comparação metodológica; não representa relações geográficas, pontuações ou resultados experimentais.

## Etapas em cartões expansíveis

«Como o projecto funciona» usa oito cartões, em quatro colunas no computador, duas em larguras intermédias e uma no telemóvel. Número, título, resumo e estado permanecem visíveis. Seleccionar um cartão abre entradas, operação, saídas, verificação e fontes; seleccionar outro fecha o anterior. Os cartões usam `details/summary` nativos com o mesmo atributo `name`, mais compatibilidade JavaScript para exclusividade. Funcionam também sem JavaScript. Os IDs das etapas foram preservados e as ligações directas abrem o cartão correspondente.

## Detalhes das etapas em modal

Com JavaScript, seleccionar um cartão abre um `dialog` nativo com título, estado, resumo, entradas, operações, saídas, verificação e fontes. Os conteúdos são derivados do HTML do próprio cartão. Fecho pelo botão, Escape ou gesto fora da janela; Tab e Shift+Tab circulam no diálogo e o foco regressa ao cartão. Uma ligação para uma etapa abre a modal correspondente; ligações de suporte fecham a modal antes da navegação. Sem JavaScript, os detalhes nativos continuam expansíveis no cartão. Não há novas dependências.

## Percurso didáctico da evolução

«A evolução do projecto» começa por um percurso com seis apontadores desde a definição do problema até à actividade actual, mais um apontador separado para a próxima fase planeada. Cada fase explica o que foi feito e o seu significado. O estado actual tem `aria-current="step"`, rótulo «Estou aqui» e destaque visual; não há percentagens de progresso.

A ordem é metodológica e não pretende substituir uma cronologia documental completa. Apenas as entregas de 28 e 29/10/2026 recebem datas. A preparação e o marco de consolidação mantêm a indicação de data não documentada. Os registos completos existentes foram preservados abaixo, com ligações desde o percurso, e as etapas continuam a abrir as respectivas modais.

## Evolução em cartões e modal

O percurso de evolução apresenta sete cartões ordenados (seis marcos e próximo passo), em três colunas no computador, duas nas larguras intermédias e uma no telemóvel. Número, data ou indicação de ausência de data, título e resumo ficam visíveis. A actividade actual mantém «Estou aqui» e o próximo passo é identificado como planeado.

A selecção abre os detalhes na mesma modal nativa das etapas, preservando os controlos de foco e fecho. Os relatos completos abaixo do percurso permanecem disponíveis. Cada marco tem uma ligação directa `#evolucao-…`; sem JavaScript, os cartões continuam expansíveis por `details/summary`. Datas, estados e conteúdos científicos foram preservados.


## Single Page com sobreposição entre secções

Todo o conteúdo permanece numa única página contínua. Ao atravessar a fronteira de uma secção, um overlay translúcido aparece e desaparece em 480 ms, acompanhado de uma entrada vertical subtil do título. Não há rotações, simulação de páginas, captura de scroll ou carregamento fictício de conteúdo.

A camada fica abaixo do menu, não recebe cliques e desaparece ao terminar. Saltos de navegação e scroll nos dois sentidos usam a mesma transição. O último conteúdo termina normalmente no rodapé, sem repetição automática. Movimento reduzido, pausa global, conteúdo sem JavaScript e os detalhes em modal são preservados.

## Página educativa PM2.5 — 17/11/2026

`pm25.html` é uma página estática interna, aberta na mesma aba pelo botão **Conhecer melhor o PM2.5** no Contexto de `index.html`. O caminho de navegação e as ligações de regresso apontam para `index.html#contexto`; a proposta de solução aponta para `index.html#proposta`.

### Conteúdo e edição

O autor forneceu, após a clarificação inicial, o texto integral e as cinco referências. Os dez blocos de texto foram preservados, incluindo os parágrafos sobre Luanda, a tabela OMS, a data de consulta indicada e o DOI. Os parágrafos originais têm atributos `data-original` para facilitar a revisão; as explicações complementares foram acrescentadas separadamente. Não se transformou o conteúdo num resumo.

A estrutura tem apresentação, definição, origens, saúde, interpretação, relação com Luanda e referências. O índice é lateral e acompanha a leitura no computador; torna-se expansível no telemóvel. O conteúdo principal permanece visível sem JavaScript. Os dois percursos de formação usam texto e setas HTML, evitando um esquema dimensional sem escala. Não há semáforos, calculadoras ou previsões simuladas.

Editar o conteúdo em `pm25.html`. Manter as citações `[1]` a `[5]`, os IDs `ref-N` e as ligações de regresso correspondentes. As referências conservam títulos, instituições/autores, anos fornecidos, descrições e DOI. Não acrescentar `utm_source` aos links. Ao alterar as citações, actualizar também os backlinks.

### Ficheiros e reutilização

- `assets/style.css`: identidade partilhada e entrada curta no Contexto.
- `assets/education.css`: coluna de leitura com máximo de 72ch, índice, diagramas textuais, tabela e destaques.
- `assets/education.js`: índice responsivo, secção corrente, cabeçalho móvel e destinos de âncora acessíveis.
- `assets/reading-progress.js`: componente de leitura extraído de `assets/main.js` e carregado por ambas as páginas, sem duplicação de lógica.
- `assets/main.js`: mantém os comportamentos da página principal; a barra é agora inicializada pelo componente partilhado.

Pode abrir-se directamente `pm25.html` ou usar o servidor local já documentado. Não existe build nem nova dependência. Os caminhos relativos funcionam no servidor local e no GitHub Pages a partir da raiz.

### Preservação e verificação bibliográfica

A frase **“Fontes consultadas em 17 de novembro de 2026.”** é informação fornecida pelo autor e foi preservada como tal, com nota visível que distingue essa data da verificação desta implementação.

A verificação do agente, também em 17/11/2026, está discriminada em `VERIFICACAO.md`. A referência IARC foi preservada com **2016**, conforme o original; o catálogo consultado em `https://publications.iarc.who.int/538` apresenta **2015**. Esta divergência fica registada para revisão bibliográfica, sem alterar silenciosamente o texto fornecido. O DOI e o endereço NEJM foram preservados mesmo quando a ferramenta de consulta encontrou restrições; o manuscrito no PMC foi efectivamente aberto como acesso alternativo ao mesmo artigo.

Não houve commit, push ou publicação nesta tarefa.

## Vistas C4 e navegação arquitectural — 17/11/2026

A secção `#como-funciona`, intitulada **Como o projecto funciona**, fica imediatamente depois de `#inicio` e antes de `#contexto`. O menu inclui «Como funciona». O bloco metodológico anterior foi mantido em `#metodologia`, agora com o título **Etapas metodológicas**, evitando dois títulos iguais.

### Âmbito e entidades

A vista de contexto representa **uma única aplicação local de preparação**, o investigador **Jeorgel Chitende** e a **OpenWeather como origem externa dos ficheiros**. A fronteira tracejada envolve apenas a aplicação. As etapas de preparação são operações do mesmo sistema, não sistemas/contentores inventados. Não se desenham bases de dados, serviços cloud, sensores, perfis adicionais ou componentes de modelação.

O diagrama distingue a proveniência OpenWeather → investigador, a importação/configuração investigador → aplicação e o retorno de resultados aplicação → investigador. A ligação da origem não afirma uma chamada automática da aplicação à API. O site académico continua separado da aplicação de processamento.

A vista dinâmica adopta o estilo de sequência C4 ao nível de sistemas, com **oito interacções**:

1. Importar PM2.5 JSON/CSV.
2. Solicitar explicitamente diagnóstico e preparação.
3. Consultar a série de PM2.5 preparada e as verificações.
4. Importar e solicitar validação da meteorologia.
5. Configurar e solicitar integração e construção temporal.
6. Consultar atributos, alvos e elegibilidade com proveniência.
7. Solicitar exportações.
8. Receber CSV/JSON/PDF, conforme o estado dos artefactos.

É um cenário lógico bem-sucedido, não um registo de execução ou auditoria. Os bloqueios não são ignorados: fontes não aprovadas exigem resolução e nova validação. A modelação futura é uma nota separada, sem atribuir uma localização arquitectural não documentada.

### Documentos usados e rastreabilidade

Lidos em modo de consulta na aplicação separada, sem alterações:

| Informação representada | Base documental |
|---|---|
| Aplicação local, importação de ficheiros, diagnóstico e preparação PM2.5, pedidos explícitos | README da aplicação `previsao-pm25-luanda` |
| Snapshot, meteorologia validada, integração, atributos/alvos, artefactos verificados, CSV/JSON/PDF | `docs/implementacao_etapa3_incremento7.md`, de 28/10/2026 |
| Preparação histórica concluída e série consolidada | Estado e resultados do relatório de consolidação fornecidos pelo autor e já publicados no conteúdo do site; o Word continua ausente |
| Pessoa responsável e origem OpenWeather | Identificação e fonte principal fornecidas pelo autor, README da aplicação e conteúdo existente |
| Âmbito da notação | https://c4model.com/diagrams/system-context e https://c4model.com/diagrams/dynamic, consultados em 17/11/2026 |

O README da aplicação descreve o incremento de preparação PM2.5; o relatório de 28/10 documenta a engenharia multivariada posterior com fixtures. Não se confundem esses testes de engenharia com validação histórica. O estado científico actual continua a ser o marco de consolidação informado pelo autor.

### Destinos e manutenção

As entidades e relações ligam a explicações existentes ou complementos no próprio site:

- Fontes e operações: `#etapa-aquisicao`, `#etapa-auditoria`, `#etapa-integracao`, `#etapa-serie`.
- Sistema: `#sistema-preparacao`, dentro de Etapas metodológicas.
- Papel: `#papel-investigador`, no Autor.
- Exportações e materiais: `#materiais-preparacao`, antes da lista de materiais.
- Fases planeadas: `#etapa-persistencia`, `#etapa-treino`, `#etapa-avaliacao`.

Todos estes destinos explicitam **Finalidade, Entradas, Operações, Saídas, Verificações e Estado actual**. Nas etapas, os textos de entrada/operação/saída/verificação anteriores foram preservados e os campos de finalidade e estado acrescentados. Os links continuam a abrir as modais existentes; sem JavaScript, os detalhes nativos permanecem consultáveis.

As entidades são HTML semântico com links; os SVG desenham ícones e setas. A vista de contexto dispõe ainda de descrição textual equivalente. Na vista dinâmica, a própria lista numerada contém a equivalência textual, incluindo os intervenientes e a direcção de cada interacção. O contexto passa a disposição vertical no telemóvel; não são necessárias imagens, bibliotecas ou chamadas de rede para renderizar as vistas.

Ao acrescentar uma relação, confirmar primeiro o documento de suporte, o significado da seta e o destino. Manter IDs únicos também nos marcadores SVG; não atribuir um sistema independente a cada etapa metodológica.

### Pendências arquitecturais

- O percurso exacto de aquisição dos ficheiros fora da aplicação (manual, script, produto/encomenda e configuração) não está suficientemente documentado para um diagrama de runtime detalhado. A vista representa apenas a origem e a importação confirmadas.
- Não há base nesta revisão para desenhar integração directa aplicação ↔ API OpenWeather, autenticação, agendamentos ou outros serviços externos.
- A arquitectura de persistência preditiva, treino, validação e avaliação futura não está documentada; não foi inventado um módulo, contentor ou serviço para essas funções.
- O Word de consolidação não foi disponibilizado; conserva-se a atribuição aos dados informados pelo autor, sem declarar nova leitura do documento.
- As verificações do sistema são descritas a partir dos relatórios. Não foram reexecutadas suites, auditorias científicas ou medições operacionais da aplicação.

Nenhuma alteração foi feita à aplicação separada, nenhum ficheiro técnico foi publicado como download e não houve commit, push ou publicação.

### Etapas metodológicas em vista C4

A grelha de oito cartões foi substituída por uma vista dinâmica ao nível de sistema: o investigador e a aplicação são os únicos participantes. Quatro interacções numeradas ligam importação, diagnóstico, integração e consulta da série às explicações existentes. As setas identificam pedido e retorno; não representam oito sistemas nem uma execução capturada. A aquisição externa continua sem ligação directa inventada à API.

Persistência, treino, avaliação e relato mantêm-se numa sequência separada de ligações planeadas, sem atribuir-lhes arquitectura ainda não documentada. Os oito IDs e os seis campos de cada explicação foram preservados. O detalhe abre na modal existente; a alternativa textual usa `details` nativos, disponível sem JavaScript. Ao fechar a modal, o foco regressa à ligação de origem. O ajuste à navegação diferida impede que um callback de scroll retire esse foco.

### Revisão de estrutura e navegação

A ordem do menu acompanha as dez secções da página, incluindo “Como funciona” depois de “Resultados e materiais”. A numeração dos cabeçalhos foi alinhada com a do menu. O título “Resultados e materiais” identifica directamente o destino; a introdução de “Como funciona” distingue a arquitectura da aplicação do percurso metodológico.

Abrir uma explicação em modal conserva a posição de leitura da página. O histórico do navegador acompanha as âncoras e fecha a janela quando regressa a uma secção. O menu móvel admite deslocamento vertical em ecrãs baixos, mantendo os destinos acessíveis.

### Leitura visual da concentração

O painel de concentração apresenta área sob a curva diária, maior média diária assinalada, ausências em azul-cinzento e três indicadores relativos ao período seleccionado: média ponderada pelas horas observadas, máximo horário e cobertura. A média ponderada parte dos agregados diários exportados (arredondados a quatro casas), sendo apresentada com duas casas decimais. Não foram acrescentadas classes de risco ou limites sanitários ao gráfico.

Com JavaScript, o visitante pode tocar/clicar na curva ou percorrer um controlo nativo de intervalo com teclado para consultar cada dia e a sua cobertura. Dias sem observação mostram texto de ausência e nenhum ponto a zero. O SVG e a tabela continuam disponíveis sem JavaScript. Se o CSV derivado não carregar, indicadores relativos ao histórico completo são ocultados ao escolher um ano para evitar atribuição indevida ao período. As fontes e os números originais não foram alterados.
