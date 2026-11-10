/* Melhoria progressiva: o conteúdo e as âncoras funcionam sem JavaScript. */
document.documentElement.classList.add('js');
const toggle = document.querySelector('.menu-toggle');
const menu = document.querySelector('#menu');
toggle.hidden = false;
function closeMenu() {
  menu.classList.remove('is-open');
  toggle.setAttribute('aria-expanded', 'false');
}
toggle.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') !== 'true';
  toggle.setAttribute('aria-expanded', String(open));
  menu.classList.toggle('is-open', open);
});
menu.addEventListener('click', event => {
  if (event.target.closest('a')) closeMenu();
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
    closeMenu();
    toggle.focus();
  }
});
matchMedia('(min-width: 761px)').addEventListener('change', closeMenu);

/* Indicação de secção e abertura das entregas por ligação directa. */
const header = document.querySelector('.header');
const navLinks = [...menu.querySelectorAll('a[href^="#"]')];
const navSections = navLinks.map(link => document.querySelector(link.getAttribute('href')));
let framePending = false;
function updateNavigation() {
  const headerHeight = header.getBoundingClientRect().height;
  document.documentElement.style.setProperty('--header-offset', `${headerHeight}px`);
  let active = navSections[0];
  for (const section of navSections) {
    if (section.getBoundingClientRect().top <= headerHeight + 120) active = section;
  }
  for (const link of navLinks) {
    if (link.hash === `#${active.id}`) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  }
  framePending = false;
}
function scheduleNavigation() {
  if (!framePending) {
    framePending = true;
    requestAnimationFrame(updateNavigation);
  }
}
function revealAnchor() {
  let id;
  try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
  const target = document.getElementById(id);
  if (!target) return;
  if (target.tagName === 'DETAILS') target.open = true;
  let parent = target.parentElement;
  while (parent) {
    if (parent.tagName === 'DETAILS') parent.open = true;
    parent = parent.parentElement;
  }
  updateNavigation();
  requestAnimationFrame(() => {
    target.scrollIntoView({ block: 'start', behavior: 'instant' });
    scheduleNavigation();
  });
}
window.addEventListener('scroll', scheduleNavigation, { passive: true });
window.addEventListener('resize', scheduleNavigation);
window.addEventListener('hashchange', revealAnchor);
if ('ResizeObserver' in window) new ResizeObserver(scheduleNavigation).observe(header);
updateNavigation();
if (location.hash) revealAnchor();
