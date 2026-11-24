/* Índice de leitura: progressivo, sem esconder o conteúdo educativo. */
const educationHeader = document.querySelector('.header');
const educationMenu = document.querySelector('#menu');
const educationToggle = document.querySelector('.menu-toggle');
const toc = document.querySelector('.education-toc');
const tocMedia = matchMedia('(max-width: 900px)');
const tocLinks = [...document.querySelectorAll('.education-toc nav a')];
const educationSections = tocLinks.map(link => document.querySelector(link.hash));
function updateEducationOffset() {
  document.documentElement.style.setProperty('--header-offset', `${educationHeader.getBoundingClientRect().height}px`);
}
function closeEducationMenu() {
  educationMenu.classList.remove('is-open');
  educationToggle.setAttribute('aria-expanded', 'false');
  updateEducationOffset();
}
function updateTocMode() { toc.open = !tocMedia.matches; }
function focusEducationAnchor() {
  let target;
  try { target = document.getElementById(decodeURIComponent(location.hash.slice(1))); } catch { return; }
  if (!target) return;
  closeEducationMenu();
  if (tocMedia.matches && !toc.contains(target)) toc.open = false;
  requestAnimationFrame(() => {
    target.scrollIntoView({ block: 'start', behavior: 'instant' });
    if (!target.hasAttribute('tabindex')) target.setAttribute('tabindex', '-1');
    target.focus({ preventScroll: true });
  });
}
let tocFrame = false;
function updateTocSelection() {
  const threshold = educationHeader.getBoundingClientRect().height + 100;
  let current = educationSections[0];
  for (const section of educationSections) if (section.getBoundingClientRect().top <= threshold) current = section;
  for (const link of tocLinks) {
    if (link.hash === `#${current.id}`) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  }
  tocFrame = false;
}
document.documentElement.classList.add('js');
educationToggle.hidden = false;
educationToggle.addEventListener('click', () => {
  const open = educationToggle.getAttribute('aria-expanded') !== 'true';
  educationToggle.setAttribute('aria-expanded', String(open));
  educationMenu.classList.toggle('is-open', open);
  updateEducationOffset();
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && educationToggle.getAttribute('aria-expanded') === 'true') {
    closeEducationMenu();
    educationToggle.focus();
  }
});
window.addEventListener('hashchange', focusEducationAnchor);
document.addEventListener('click', event => {
  const link = event.target.closest('a[href^="#"]');
  if (link && link.hash === location.hash) focusEducationAnchor();
});
window.addEventListener('resize', updateEducationOffset);
window.addEventListener('scroll', () => {
  if (!tocFrame) { tocFrame = true; requestAnimationFrame(updateTocSelection); }
}, { passive: true });
matchMedia('(max-width: 1000px)').addEventListener('change', closeEducationMenu);
tocMedia.addEventListener('change', updateTocMode);
if ('ResizeObserver' in window) new ResizeObserver(updateEducationOffset).observe(educationHeader);
updateEducationOffset();
updateTocMode();
updateTocSelection();
if (location.hash) focusEducationAnchor();
