/* Componente partilhado pelas páginas do site. */
(() => {
/* Progresso de leitura: no máximo uma medição por frame, sem alterar o layout. */
const readingProgress = document.querySelector('.reading-progress');
const readingFill = readingProgress.querySelector('.reading-progress-fill');
let readingFrame = false;
let readingPercent = -1;
function updateReadingProgress() {
  const scrolling = document.scrollingElement || document.documentElement;
  const available = scrolling.scrollHeight - scrolling.clientHeight;
  const ratio = available > 0 ? Math.min(1, Math.max(0, scrolling.scrollTop / available)) : 0;
  readingProgress.hidden = available <= 0;
  readingFill.style.transform = `scaleX(${ratio})`;
  const percent = Math.round(ratio * 100);
  if (percent !== readingPercent) {
    readingProgress.setAttribute('aria-valuenow', String(percent));
    readingPercent = percent;
  }
  readingFrame = false;
}
function scheduleReadingProgress() {
  if (readingFrame) return;
  readingFrame = true;
  requestAnimationFrame(updateReadingProgress);
}
window.addEventListener('scroll', scheduleReadingProgress, { passive: true });
window.addEventListener('resize', scheduleReadingProgress);
window.addEventListener('pageshow', scheduleReadingProgress);
window.visualViewport?.addEventListener('resize', scheduleReadingProgress);
// Imagens diferidas, detalhes e alterações de conteúdo podem mudar a área de leitura.
document.addEventListener('load', scheduleReadingProgress, true);
if ('ResizeObserver' in window) {
  const readingResizeObserver = new ResizeObserver(scheduleReadingProgress);
  readingResizeObserver.observe(document.body);
  readingResizeObserver.observe(document.documentElement);
}
if ('MutationObserver' in window) {
  new MutationObserver(records => {
    if (records.some(record => !readingProgress.contains(record.target))) scheduleReadingProgress();
  }).observe(document.body, {
    subtree: true, childList: true, characterData: true,
    attributes: true, attributeFilter: ['open', 'hidden', 'class', 'style', 'src', 'width', 'height']
  });
}
updateReadingProgress();
})();
