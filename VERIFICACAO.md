# Verificação local — 10 de Novembro de 2026

- `node --check assets/main.js`: passou.
- Parser HTML: 14 IDs únicos; 20 referências verificadas quanto a âncoras e existência de ficheiros locais. Sem links vazios.
- HTML + todos os assets: **29,270 bytes**, sem compressão. Este total inclui favicon e imagem social; está abaixo de 300 KB. Não é uma medição de rede em navegador.
- Sem dependências externas em tempo de execução.
- Inspecção de código: menu com `aria-expanded`, Escape e melhoria progressiva; link para saltar navegação; foco visível; movimento reduzido; âncoras com margem do cabeçalho; grelhas adaptativas e HTML semântico.
- Fontes de fundamentação consultadas: EPA e documentação oficial OpenWeather.

## Limites

Não foi executado Lighthouse, teste visual por navegador, leitor de ecrã ou medição automática de contraste. Playwright, Puppeteer e Lighthouse não estão disponíveis no ambiente. Os breakpoints foram inspeccionados no código, sem afirmar teste visual em dispositivos. É necessária a verificação manual descrita no README antes de publicar.
