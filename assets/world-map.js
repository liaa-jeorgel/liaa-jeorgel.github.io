/* Mapa global da secção 02: melhoria progressiva, sem dados remotos.
   O SVG, os rótulos e a tabela em texto existem no HTML mesmo sem JavaScript. */
(() => {
  const root = document.documentElement;
  const figure = document.querySelector('.pm-map');
  if (!figure) return;

  const svg = figure.querySelector('.pm-map-svg');
  const zoom = figure.querySelector('.pm-map-zoom');
  const readout = figure.querySelector('#pm-map-readout');
  const nodes = [...figure.querySelectorAll('.pm-map-node')];
  const links = [...figure.querySelectorAll('.pm-map-link')];
  const chips = [...figure.querySelectorAll('.pm-map-chip')];
  const buttons = [...figure.querySelectorAll('[data-map-action]')];
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const still = () => reduced.matches || root.classList.contains('motion-paused');

  let cities = [];
  try {
    cities = JSON.parse(figure.querySelector('#pm-map-data').textContent);
  } catch { return; }
  const byId = new Map(cities.map(city => [city.id, city]));

  root.classList.add('worldmap-ready');

  const title = readout.querySelector('strong');
  const meta = readout.querySelector('span');
  const note = readout.querySelector('p');
  let selected = null;

  function select(id) {
    const city = byId.get(id);
    if (!city || selected === id) return;
    selected = id;
    for (const node of nodes) {
      const active = node.dataset.city === id;
      node.classList.toggle('is-selected', active);
      node.setAttribute('aria-pressed', String(active));
    }
    for (const link of links) {
      link.classList.toggle('is-linked', link.dataset.from === id || link.dataset.to === id);
    }
    svg.classList.add('has-selection');
    for (const chip of chips) chip.setAttribute('aria-pressed', String(chip.dataset.city === id));

    title.textContent = `${city.name}, ${city.country}`;
    meta.textContent = city.focus
      ? 'Foco do estudo · sem valor comunicado na base V8.0'
      : `${city.year} · média anual ${city.value} µg/m³ · cobertura ${city.coverage}`;
    note.textContent = city.focus
      ? 'A análise usa dados estimados da OpenWeather; a avaliação futura não equivale a validação por sensores locais.'
      : 'Valor comunicado à OMS. Anos, métodos e cobertura diferem: não é uma classificação nem uma comparação entre cidades.';

    if (!still()) {
      readout.getAnimations().forEach(animation => animation.cancel());
      readout.animate(
        [{ opacity: .45, transform: 'translateY(4px)' }, { opacity: 1, transform: 'none' }],
        { duration: 180, easing: 'ease-out' }
      );
    }
  }

  function setFocus(on) {
    // Mantém Luanda no centro ao ampliar o continente africano.
    zoom.style.transform = on ? 'translate(-681px,-450px) scale(2.2)' : '';
    svg.classList.toggle('is-focused', on);
    for (const button of buttons) {
      if (button.dataset.mapAction === 'focus') button.setAttribute('aria-pressed', String(on));
    }
    if (on) select('luanda');
  }

  for (const node of nodes) {
    const id = node.dataset.city;
    const city = byId.get(id);
    if (!city) continue;
    node.setAttribute('role', 'button');
    node.setAttribute('tabindex', '0');
    node.setAttribute('aria-pressed', 'false');
    node.setAttribute('aria-label', city.focus
      ? `${city.name}, ${city.country}. Foco do estudo.`
      : `${city.name}, ${city.country}. Média anual de ${city.value} microgramas por metro cúbico em ${city.year}.`);
    node.addEventListener('click', () => select(id));
    node.addEventListener('focus', () => select(id));
    node.addEventListener('keydown', event => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        select(id);
      }
    });
    node.addEventListener('pointerenter', event => {
      if (event.pointerType === 'mouse') select(id);
    });
  }

  for (const chip of chips) {
    chip.addEventListener('click', () => select(chip.dataset.city));
    chip.addEventListener('focus', () => select(chip.dataset.city));
  }

  for (const button of buttons) {
    if (button.dataset.mapAction === 'focus' || button.dataset.mapAction === 'reset') {
      button.addEventListener('click', () => setFocus(button.dataset.mapAction === 'focus'));
    }
    if (button.dataset.mapAction === 'links') {
      button.addEventListener('click', () => {
        const on = button.getAttribute('aria-pressed') !== 'true';
        button.setAttribute('aria-pressed', String(on));
        figure.classList.toggle('hide-links', !on);
      });
    }
  }

  for (const button of buttons) {
    if (button.dataset.mapAction === 'focus') button.setAttribute('aria-pressed', 'false');
  }
  select('luanda');
})();
