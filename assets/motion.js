/* Camada partilhada de movimento: reveals discretos, estado de leitura e feedback.
   O conteúdo continua visível se este ficheiro não correr. */
(() => {
  const root = document.documentElement;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const canObserve = 'IntersectionObserver' in window;

  const selectors = [
    '.proposal-facts',
    '.proposal-flow > li',
    '.model-card',
    '.evaluation-head',
    '.metric-card',
    '.evaluation-table-wrap',
    '.data-panel',
    '.materials-grid > article, .materials-grid > div',
    '.delivery-row',
    '.result-notes > article, .result-notes > div',
    '.education-section > .eyebrow, .education-section > h2, .education-section > .education-lead',
    '.education-reading-note',
    '.education-concepts > div',
    '.education-units > div, .education-time-concepts > div',
    '.education-paths > section',
    '.education-study',
    '.education-guidelines',
    '.education-interpretation',
    '.education-horizons',
    '.education-warning',
    '.education-references > li'
  ];

  const targets = [];
  for (const selector of selectors) {
    for (const element of document.querySelectorAll(selector)) {
      if (targets.includes(element) || element.closest('.stage-modal, [hidden]')) continue;
      targets.push(element);
    }
  }

  for (const element of targets) element.classList.add('reveal');

  // Atrasos curtos apenas dentro de grupos irmãos; nunca acima de 180 ms.
  const groups = new Set(targets.map(element => element.parentElement));
  for (const group of groups) {
    [...group.children].filter(child => targets.includes(child)).slice(0, 4).forEach((child, index) => {
      child.style.setProperty('--reveal-delay', `${index * 60}ms`);
    });
  }

  const pending = new Set(targets);
  let observer = null;
  if (canObserve && pending.size) {
    observer = new IntersectionObserver((entries, currentObserver) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        reveal(entry.target);
        currentObserver.unobserve(entry.target);
      }
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.01 });
  }

  let scanFrame = false;
  function reveal(element) {
    if (!pending.delete(element)) return;
    element.classList.add('is-revealed');
    observer?.unobserve(element);
    if (!pending.size) window.removeEventListener('scroll', scheduleScan);
  }
  // Reserva para ambientes onde o IntersectionObserver não entrega callbacks.
  function scanViewport() {
    const limit = innerHeight * .92;
    for (const element of [...pending]) {
      const box = element.getBoundingClientRect();
      if (box.top < limit && box.bottom > 0) reveal(element);
    }
    scanFrame = false;
  }
  function scheduleScan() {
    if (scanFrame || !pending.size) return;
    scanFrame = true;
    requestAnimationFrame(scanViewport);
  }

  function revealAll() {
    root.classList.remove('motion-ready');
    observer?.disconnect();
    for (const element of targets) {
      pending.delete(element);
      element.classList.add('is-revealed');
    }
    window.removeEventListener('scroll', scheduleScan);
  }

  function applyMode() {
    if (reduced.matches || root.classList.contains('motion-paused') || !observer) {
      revealAll();
      return;
    }
    root.classList.add('motion-ready');
    for (const element of pending) observer.observe(element);
    window.addEventListener('scroll', scheduleScan, { passive: true });
    scanViewport();
  }

  applyMode();
  reduced.addEventListener('change', applyMode);

  // O botão de movimento do site também controla estes reveals.
  document.addEventListener('click', event => {
    if (!event.target.closest('.motion-toggle')) return;
    setTimeout(applyMode, 0);
  });

  /* Cabeçalho: elevação mínima depois de sair do topo, sem observar cada pixel. */
  const header = document.querySelector('.header');
  if (header) {
    let frame = false;
    function updateHeaderState() {
      const scrolling = document.scrollingElement || document.documentElement;
      root.classList.toggle('is-scrolled', scrolling.scrollTop > 8);
      frame = false;
    }
    window.addEventListener('scroll', () => {
      if (frame) return;
      frame = true;
      requestAnimationFrame(updateHeaderState);
    }, { passive: true });
    updateHeaderState();
  }
})();
