/* Navegação progressiva: sem JavaScript, todas as secções continuam disponíveis. */
const toggle = document.querySelector('.menu-toggle');
const menu = document.querySelector('#menu');
const header = document.querySelector('.header');
const panels = [...document.querySelectorAll('#principal > section')];
const navLinks = [...menu.querySelectorAll('a[href^="#"]')];
const mobile = matchMedia('(max-width: 1000px)');
const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
const motionToggle = document.querySelector('.motion-toggle');
let motionPaused = false;
const revealed = new WeakSet();

function enterPanel(panel) {
  if (motionPaused || reducedMotion.matches) return;
  const candidates = panel.id === 'inicio'
    ? panel.querySelectorAll('.research-kicker, h1, .hero-copy, .current-stage, .actions, .hero-figure, .hero-foot')
    : panel.querySelectorAll('.section-heading, .question, .context-grid, .model-grid, .process-note, .journal-intro, .result-stats, .related-card, .author-grid');
  [...candidates].slice(0, 8).forEach((item, index) => {
    item.getAnimations().forEach(animation => animation.cancel());
    item.animate([{ opacity: .15, transform: 'translateY(16px)' }, { opacity: 1, transform: 'translateY(0)' }], {
      duration: 500, delay: index * 45, easing: 'cubic-bezier(.2,.7,.3,1)', fill: 'backwards'
    });
  });
}
function updateOffset() {
  const offset = header.getBoundingClientRect().height;
  document.documentElement.style.setProperty('--header-offset', `${offset}px`);
}
function closeMenu() {
  menu.classList.remove('is-open');
  toggle.setAttribute('aria-expanded', 'false');
  updateOffset();
}
function showDestination(hash, focus = false) {
  let id;
  try { id = decodeURIComponent(hash.replace(/^#/, '')); } catch { return; }
  const target = id ? document.getElementById(id) : panels[0];
  if (!target) return;
  const panel = target.closest('#principal > section');
  // O link de salto para o conteúdo não altera a secção seleccionada.
  if (!panel) return;
  if (target.matches('.process-list > li')) {
    const stageCard = target.querySelector('.stage-card');
    if (stageCard) {
      if (document.documentElement.classList.contains('stage-modals-ready')) openStageModal(stageCard);
      else stageCard.open = true;
    }
  }
  // As secções permanecem visíveis numa página contínua.
  for (const link of navLinks) {
    if (link.hash === `#${panel.id}`) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  }
  let parent = target;
  while (parent && parent !== panel) {
    if (parent.tagName === 'DETAILS') parent.open = true;
    parent = parent.parentElement;
  }
  closeMenu();
  enterPanel(panel);
  requestAnimationFrame(() => {
    target.scrollIntoView({ block: 'start', behavior: 'instant' });
    if (focus && !document.querySelector('.stage-modal[open]')) {
      const focusTarget = target.tagName === 'DETAILS' ? target.querySelector('summary') : target;
      if (!focusTarget.hasAttribute('tabindex')) focusTarget.setAttribute('tabindex', '-1');
      focusTarget.focus({ preventScroll: true });
    }
  });
}

motionToggle.hidden = false;
motionToggle.addEventListener('click', () => {
  motionPaused = !motionPaused;
  document.documentElement.classList.toggle('motion-paused', motionPaused);
  motionToggle.setAttribute('aria-pressed', String(motionPaused));
  motionToggle.innerHTML = motionPaused ? '<span aria-hidden="true">▷</span> Retomar movimento' : '<span aria-hidden="true">Ⅱ</span> Pausar movimento';
  document.getAnimations().filter(animation => !animation.effect?.target?.closest('.academic-scene')).forEach(animation => {
    if (motionPaused) animation.finish();
  });
});
for (const button of document.querySelectorAll('[data-select-horizon]')) {
  button.addEventListener('click', () => {
    const horizon = button.dataset.selectHorizon;
    for (const option of document.querySelectorAll('[data-select-horizon]')) option.setAttribute('aria-pressed', String(option === button));
    for (const item of document.querySelectorAll('[data-horizon]')) item.classList.toggle('is-selected', item.dataset.horizon === horizon);
    const period = horizon === '1' ? 'uma hora' : `${horizon} horas`;
    document.querySelector('#horizon-explanation').textContent = `Alvo: concentração de PM2.5 ${period} após a origem da previsão. Modelação ainda planeada.`;
  });
}
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) {
      if (!entry.isIntersecting || revealed.has(entry.target)) continue;
      revealed.add(entry.target);
      if (!motionPaused && !reducedMotion.matches) entry.target.animate([
        { opacity: .3, transform: 'translateY(12px)' }, { opacity: 1, transform: 'translateY(0)' }
      ], { duration: 450, easing: 'ease-out' });
    }
  }, { threshold: .12 });
  document.querySelectorAll('.process-list>li, .timeline details, .care-grid article').forEach(item => observer.observe(item));
}
reducedMotion.addEventListener('change', () => {
  if (reducedMotion.matches) document.getAnimations().forEach(animation => animation.cancel());
});
// O explorador é uma melhoria progressiva; não executa previsões.
document.documentElement.classList.add('horizon-ready');
toggle.hidden = false;
document.documentElement.classList.add('js');
toggle.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') !== 'true';
  toggle.setAttribute('aria-expanded', String(open));
  menu.classList.toggle('is-open', open);
  updateOffset();
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
    closeMenu();
    toggle.focus();
  }
});
document.addEventListener('click', event => {
  const link = event.target.closest('a[href^="#"]');
  if (!link || event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
  const hash = link.getAttribute('href');
  let target;
  try { target = document.getElementById(decodeURIComponent(hash.slice(1))); } catch { return; }
  if (!target?.closest('#principal > section')) return;
  event.preventDefault();
  if (location.hash !== hash) history.pushState(null, '', hash);
  showDestination(hash, true);
});
window.addEventListener('popstate', () => showDestination(location.hash));
window.addEventListener('hashchange', () => showDestination(location.hash));
window.addEventListener('resize', updateOffset);
mobile.addEventListener('change', closeMenu);
if ('ResizeObserver' in window) new ResizeObserver(updateOffset).observe(header);
// A secção corrente é identificada também durante a leitura por deslocamento.
let navigationFrame = false;
function updateCurrentSection() {
  const threshold = header.getBoundingClientRect().height + 120;
  let active = panels[0];
  for (const panel of panels) if (panel.getBoundingClientRect().top <= threshold) active = panel;
  for (const link of navLinks) {
    if (link.hash === `#${active.id}`) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  }
  navigationFrame = false;
}
window.addEventListener('scroll', () => {
  if (!navigationFrame) {
    navigationFrame = true;
    requestAnimationFrame(updateCurrentSection);
  }
}, { passive: true });
updateOffset();
updateCurrentSection();
enterPanel(panels[0]);
if (location.hash) showDestination(location.hash);


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

/* Mapa comparativo: seleccionar uma coluna sem esconder a visão de conjunto. */
const comparisonMap = document.querySelector('.comparison-map');
if (comparisonMap) {
  const sourceRows = [...document.querySelectorAll('.comparison-table tbody tr')];
  const mapButtons = [...comparisonMap.querySelectorAll('[data-map-project]')];
  const projectDetail = comparisonMap.querySelector('.map-project-detail');
  let mapSelection = -1;
  function selectMapProject(index) {
    if (mapSelection === index) return;
    mapSelection = index;
    const row = sourceRows[index];
    const link = row.querySelector('th a');
    comparisonMap.querySelectorAll('[data-project]').forEach(cell => {
      cell.classList.toggle('map-focused', Number(cell.dataset.project) === index);
    });
    mapButtons.forEach((button, buttonIndex) => button.setAttribute('aria-pressed', String(buttonIndex === index)));
    projectDetail.querySelector('#map-project-title').textContent = link.textContent;
    projectDetail.querySelector('.map-project-authors').textContent = row.querySelector('th>span').textContent;
    const source = projectDetail.querySelector('.map-project-source');
    source.href = link.getAttribute('href');
    source.firstChild.textContent = index === 0 ? 'Conhecer o meu projecto ' : 'Consultar no portal ';
    source.setAttribute('aria-label', `Consultar: ${link.textContent}`);
    comparisonMap.querySelector('.map-status').textContent = `Projecto em foco: ${link.textContent}.`;
    if (!motionPaused && !reducedMotion.matches) {
      projectDetail.getAnimations().forEach(animation => animation.cancel());
      projectDetail.animate([{opacity:.35,transform:'translateY(5px)'},{opacity:1,transform:'translateY(0)'}],{duration:200,easing:'ease-out'});
    }
  }
  mapButtons.forEach((button, index) => {
    button.disabled = false;
    button.addEventListener('focus', () => selectMapProject(index));
    button.addEventListener('pointerenter', event => {
      if (event.pointerType === 'mouse') selectMapProject(index);
    });
    button.addEventListener('click', () => selectMapProject(index));
    button.addEventListener('keydown', event => {
      let next;
      if (event.key === 'ArrowRight' || event.key === 'ArrowDown') next = (index + 1) % mapButtons.length;
      if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') next = (index - 1 + mapButtons.length) % mapButtons.length;
      if (event.key === 'Home' || event.key === 'Escape') next = 0;
      if (event.key === 'End') next = mapButtons.length - 1;
      if (next !== undefined) {event.preventDefault();mapButtons[next].focus();}
    });
  });
  selectMapProject(0);
  projectDetail.hidden = false;
  document.querySelector('.comparison-complete').open = false;
}

/* Detalhes em dialog nativo; sem JavaScript os cartões continuam expansíveis. */
const stageCards = [...document.querySelectorAll('.stage-card')];
const stageModal = document.querySelector('.stage-modal');
let stageTrigger = null;
let restoreStageFocus = true;
function openStageModal(card) {
  if (!stageModal || typeof stageModal.showModal !== 'function') {
    card.open = true;
    return;
  }
  stageTrigger = card.querySelector('summary');
  restoreStageFocus = true;
  stageModal.querySelector('.stage-modal-number').textContent = `ETAPA ${card.querySelector('.step').textContent}`;
  stageModal.querySelector('#stage-modal-title').textContent = card.querySelector('h3').textContent;
  stageModal.querySelector('.stage-modal-status').replaceChildren(card.querySelector('.status').cloneNode(true));
  stageModal.querySelector('.stage-modal-description').textContent = card.querySelector('summary>p').textContent;
  stageModal.querySelector('.stage-modal-content').replaceChildren(...[...card.querySelector('.stage-card-body').children].map(item => item.cloneNode(true)));
  card.open = false;
  if (!stageModal.open) stageModal.showModal();
  stageModal.scrollTop = 0;
}
if (stageModal && typeof stageModal.showModal === 'function') {
  document.documentElement.classList.add('stage-modals-ready');
  for (const card of stageCards) {
    card.querySelector('summary').addEventListener('click', event => {
      event.preventDefault();
      openStageModal(card);
    });
    card.open = false;
  }
  // Só fechar se o gesto começar e terminar fora do rectângulo da janela.
  let backdropStart = false;
  function outsideModal(event) {
    const bounds = stageModal.getBoundingClientRect();
    return event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom;
  }
  stageModal.addEventListener('pointerdown', event => { backdropStart = outsideModal(event); });
  stageModal.addEventListener('click', event => {
    if (event.target === stageModal && backdropStart && outsideModal(event)) stageModal.close();
    backdropStart = false;
  });
  stageModal.addEventListener('click', event => {
    if (event.target.closest('a[href]')) {
      restoreStageFocus = false;
      stageModal.close();
    }
  });
  stageModal.addEventListener('close', () => {
    if (restoreStageFocus && stageTrigger?.isConnected) stageTrigger.focus({preventScroll:true});
  });
  let initialStage;
  try { initialStage = document.getElementById(decodeURIComponent(location.hash.slice(1))); } catch {}
  if (initialStage?.matches('.process-list>li')) openStageModal(initialStage.querySelector('.stage-card'));
}
