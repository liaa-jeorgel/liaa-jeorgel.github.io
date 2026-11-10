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
- `assets/social.svg`: arte de partilha; algumas plataformas não aceitam SVG em Open Graph. Para compatibilidade ampla, exportar para PNG 1200 × 630 e actualizar `og:image` antes de divulgar.
- `materiais/`: destino dos relatórios e imagens reais; ficheiros ainda não fornecidos.
- `.nojekyll`: permite servir os ficheiros directamente pelo GitHub Pages.

O conteúdo, os links, as âncoras e os detalhes expansíveis funcionam sem JavaScript. Sem JavaScript, o menu permanece visível também no telemóvel.

## Fidelidade científica e informações pendentes

O único ficheiro encontrado no repositório antes desta implementação foi o README de apresentação. O pedido forneceu identificação, escopo, métodos, métricas e a informação de que a última actividade foi a construção da série temporal multivariada, antes do treino. Não foram encontrados relatórios, base de dados, código de processamento, imagens ou apresentações que comprovem a execução.

Por isso:

- Não se publica data de actualização do projecto nem etapa actual como factos confirmados.
- As oito etapas metodológicas aparecem como **Planeada**, enquanto estados documentais de execução não forem fornecidos. Isto representa o plano, sem afirmar que etapas anteriores não tenham sido executadas.
- O diário distingue a actividade relatada de uma entrega confirmada e não atribui uma data inventada.
- Não há resultados, percentagens de progresso, contagens de observações ou métricas fictícias.
- A imagem de Luanda e a curva são conceptuais, não derivadas de dados.

Para completar a informação, faltam:

1. Relatórios e datas reais das entregas, com actividades, decisões, dificuldades e próximos passos.
2. Evidências e estado de cada etapa: **Concluída**, **Em desenvolvimento** ou **Planeada**.
3. Período de aquisição, coordenadas do estudo, frequência, fuso horário, unidades e produtos meteorológicos utilizados.
4. Auditoria: lacunas, duplicados, cobertura e regras efectivas de integração e limpeza.
5. Definição final de atributos, alvos, janelas e partições cronológicas.
6. Resultados experimentais, quando existirem, incluindo protocolo e evidências reprodutíveis.
7. Relatórios, apresentações e capturas reais do protótipo, com descrições acessíveis.
8. Contactos e ligações pessoais, apenas se o autor quiser fornecê-los.
9. Referências científicas adicionais efectivamente utilizadas no trabalho.

As fontes públicas verificadas para o conteúdo introdutório são EPA (definição de partículas finas) e documentação oficial da OpenWeather (APIs de poluição e meteorologia). Estão ligadas no site. O site explicita a natureza estimada dos dados e a limitação da representatividade local.

## Editar conteúdos e acrescentar entregas

Editar os textos directamente no HTML. Alterar os estados de forma individual apenas com suporte documental; evitar substituições globais. A área `REGISTOS DE EVOLUÇÃO` em `index.html` contém o diário. Inserir cada entrega **antes das anteriores**, dentro de `.timeline`, usando o modelo abaixo. Substituir todos os campos e incluir apenas ficheiros existentes. Remover o registo informativo sem data quando houver uma entrega documentada que o substitua.

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

Verificações locais realizadas: sintaxe JavaScript; estrutura HTML, IDs únicos, correspondência de âncoras e existência de recursos locais; orçamento de transferência estática. Resultados medidos em `VERIFICACAO.md`.

Playwright, Puppeteer e Lighthouse não estavam disponíveis no ambiente. Não se atribuem pontuações Lighthouse nem se afirma validação visual em navegador. Antes da publicação, verificar em navegador a 360, 768 e 1440 px: ausência de scroll horizontal, menu móvel, navegação por teclado, foco, Escape, âncoras e abertura de cada entrega. Confirmar também o conteúdo com JavaScript desactivado e movimento reduzido.

Para medir Lighthouse, abrir o site num servidor local, usar Chrome DevTools → Lighthouse e executar auditorias mobile e desktop. Procurar ≥95 em desempenho, acessibilidade, boas práticas e SEO; registar apenas os valores obtidos. Links externos foram consultados para fundamentação; a disponibilidade futura depende dos respectivos fornecedores.
