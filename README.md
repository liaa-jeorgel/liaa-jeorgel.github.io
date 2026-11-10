# PM2.5 / Luanda

Site académico individual de **Jeorgel Chitende**, na disciplina Laboratório de Inteligência Artificial Aplicada, PPGES / Universidade Federal do Pampa — UNIPAMPA.

**Previsão de Curto Prazo de PM2.5 com IA em Contexto Urbano Angolano.**

Site estático, sem backend, frameworks, fontes externas, cookies, analytics ou dependências de execução. A aplicação de processamento de dados permanece separada deste repositório. Nenhuma publicação foi realizada nesta entrega.

## Execução local

Na raiz do repositório:

```sh
python3 -m http.server 8000
```

Abrir http://localhost:8000. Encerrar com Ctrl+C. Também é possível abrir `index.html` directamente, embora um servidor local reproduza melhor o ambiente de publicação.

## Organização

- `index.html`: conteúdo científico, navegação, metodologia e diário.
- `assets/style.css`: estilos responsivos e variáveis de cores, espaçamentos e tipografia em `:root`.
- `assets/main.js`: menu móvel com estado acessível, fecho por ligação e tecla Escape.
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
