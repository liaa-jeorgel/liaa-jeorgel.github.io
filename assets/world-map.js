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
  const statisticsElement = figure.querySelector('#pm-luanda-statistics-data');
  const statistics = statisticsElement ? JSON.parse(statisticsElement.textContent) : null;
  let source = statistics ? 'openweather' : 'who';
  const period = figure.querySelector('#pm-map-year');
  const luandaData = figure.querySelector('#pm-luanda-data');
  const sourceNote = figure.querySelector('#pm-map-source-note');
  const formatter = new Intl.NumberFormat('pt-PT',{minimumFractionDigits:2,maximumFractionDigits:2});
  const integer = new Intl.NumberFormat('pt-PT');
  const displayDate = value => {
    const date = new Date(value);
    return new Intl.DateTimeFormat('pt-PT',{timeZone:'UTC',day:'2-digit',month:'2-digit',year:'numeric',hour:'2-digit',hour12:false}).format(date);
  };
  const sourceControls = figure.querySelector('.pm-map-source-controls');
  const yearControl = figure.querySelector('.pm-map-year-control');
  if (sourceControls) sourceControls.hidden = false;
  if (yearControl) yearControl.hidden = false;
  function updateStatistics() {
    if (!statistics || !period) return;
    const entry = statistics.periods[period.value];
    if (!entry) return;
    function value(id,number,unit) {
      const field = figure.querySelector(id);
      field.replaceChildren(document.createTextNode(formatter.format(number)+' '));
      const suffix = document.createElement('span');suffix.textContent=unit;field.append(suffix);
    }
    value('#pm-map-mean',entry.mean_ug_m3,'µg/m³');
    value('#pm-map-maximum',entry.max_ug_m3,'µg/m³');
    value('#pm-map-coverage',entry.coverage_percent,'%');
    const extent = period.value === 'todos' ? 'Média de todo o período, não uma média anual.' : entry.complete_calendar_year ? 'Ano civil completo na grade; cobertura das observações indicada.' : 'Ano parcial: a média não representa o ano inteiro.';
    figure.querySelector('#pm-map-period-note').textContent = `${displayDate(entry.start_utc)}–${displayDate(entry.end_utc)} UTC · ${integer.format(entry.observed_hours)} observações; ${integer.format(entry.missing_hours)} horas ausentes. ${extent}`;
  }
  function refreshLabels() {
    figure.dataset.source = source;
    if (sourceNote) sourceNote.textContent = source === 'openweather'
      ? 'OpenWeather · histórico fornecido para Luanda. Outras cidades: sem histórico desta fonte neste site.'
      : 'OMS V8.0 · valores comunicados em anos diferentes. Não são comparáveis directamente com o histórico OpenWeather de Luanda.';
    chips.forEach(chip => {
      const city = byId.get(chip.dataset.city);
      chip.querySelector('small').textContent = source === 'openweather'
        ? city.focus ? formatter.format(statistics.periods[period.value].mean_ug_m3)+' · OpenWeather' : 'Sem histórico OpenWeather'
        : city.focus ? 'Sem valor na OMS V8.0' : city.value+' · OMS';
    });
    nodes.forEach(node => {
      const city = byId.get(node.dataset.city);
      node.setAttribute('aria-label',source === 'openweather'
        ? city.focus ? `Luanda, Angola. OpenWeather: média do período ${formatter.format(statistics.periods[period.value].mean_ug_m3)} microgramas por metro cúbico.` : `${city.name}, ${city.country}. Sem histórico OpenWeather neste site.`
        : city.focus ? 'Luanda, Angola. Sem valor comunicado na OMS V8.0.' : `${city.name}, ${city.country}. OMS: média anual ${city.value} microgramas por metro cúbico em ${city.year}.`);
    });
  }

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
    if (luandaData) luandaData.hidden = !(source === 'openweather' && city.focus);
    if (source === 'openweather') {
      const entry = statistics.periods[period.value];
      meta.textContent = city.focus ? `OpenWeather · média do período: ${formatter.format(entry.mean_ug_m3)} µg/m³` : 'OpenWeather · sem histórico disponível neste site';
      note.textContent = city.focus
        ? 'Mesma série usada na preparação. Atribuição declarada pelo autor; origem física não autenticada, sem validação por sensores locais.'
        : 'O ponto é apenas uma referência geográfica. Para mostrar valores desta fonte aqui, é necessário obter e conferir o histórico correspondente; não se reutilizam números da OMS.';
    } else {
      meta.textContent = city.focus ? 'OMS V8.0 · sem valor comunicado para Luanda' : `OMS · ${city.year} · média anual ${city.value} µg/m³ · cobertura ${city.coverage}`;
      note.textContent = 'Valores comunicados à OMS; anos, métodos e cobertura diferem. Esta vista não mistura estatísticas OpenWeather nem constitui um ranking.';
    }

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
  figure.querySelectorAll('input[name="pm-map-source"]').forEach(input => input.addEventListener('change',() => {
    if (!input.checked) return;
    source = input.value;
    refreshLabels();
    const id = selected || 'luanda';selected = null;select(id);
  }));
  period?.addEventListener('change',() => {
    updateStatistics();refreshLabels();
    const id = selected || 'luanda';selected = null;select(id);
  });
  updateStatistics();refreshLabels();select('luanda');
})();
