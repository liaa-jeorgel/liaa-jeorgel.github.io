/* Apenas troca de vistas SVG pré-calculadas. O gráfico principal e a tabela não dependem de JS. */
const seriesPeriod = document.querySelector('#series-period');
if (seriesPeriod) {
  document.querySelector('.data-controls').hidden = false;
  seriesPeriod.addEventListener('change', () => {
    const value = seriesPeriod.value;
    if (!['todos','2020','2021','2022','2023','2024','2025','2026'].includes(value)) return;
    const summary = document.querySelector('.concentration-summary');
    if (summary && !seriesPeriod.dataset.dailyReady) summary.hidden = value !== 'todos';
    const image = document.querySelector('#pm25-series-chart');
    const status = document.querySelector('#series-status');
    image.src = `assets/data/pm25-${value}.svg`;
    image.closest('picture')?.querySelector('source')?.setAttribute('srcset', `assets/data/pm25-${value}-mobile.svg`);
    image.alt = `Médias diárias de PM2.5 ${value === 'todos' ? 'em todo o histórico' : 'em '+value}, com faixa das horas ausentes. Valores em µg/m³.`;
    status.textContent = `${value === 'todos' ? 'Todo o histórico' : value} · médias diárias; faixa inferior: horas ausentes de PM2.5. Sem interpolação.`;
    if (!document.documentElement.classList.contains('motion-paused') && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
      image.getAnimations().forEach(animation => animation.cancel());
      image.animate([{opacity:.45},{opacity:1}],{duration:220,easing:'ease-out'});
      status.getAnimations().forEach(animation => animation.cancel());
      status.animate([{opacity:.5},{opacity:1}],{duration:180,easing:'ease-out'});
    }
  });
}
// O acesso flutuante não deve cobrir legendas ou controlos do leitor.
const projectVideo = document.querySelector('.video-panel');
const applicationAccess = document.querySelector('.application-float');
if (projectVideo && applicationAccess && 'IntersectionObserver' in window) {
  new IntersectionObserver(entries => {
    applicationAccess.hidden = entries[0].isIntersecting;
  }, {rootMargin:'40px 0px',threshold:0}).observe(projectVideo);
}

/* Leitura diária a partir dos mesmos derivados usados pelos SVG. */
if (seriesPeriod) {
  const panel = document.querySelector('.concentration-panel');
  const slider = document.querySelector('#concentration-day-slider');
  const image = document.querySelector('#pm25-series-chart');
  const cursor = panel.querySelector('.concentration-cursor');
  const number = new Intl.NumberFormat('pt-PT', {minimumFractionDigits:2,maximumFractionDigits:2});
  const date = value => new Intl.DateTimeFormat('pt-PT', {day:'2-digit',month:'short',year:'numeric',timeZone:'UTC'}).format(new Date(value+'T12:00:00Z'));
  let daily = [], selected = [];
  function showDay(index, announce = false) {
    const row = selected[index];
    if (!row) return;
    slider.value = String(index);
    const value = row.mean === null ? 'Sem observação' : `${number.format(row.mean)} µg/m³`;
    document.querySelector('#concentration-day').textContent = date(row.date);
    document.querySelector('#concentration-value').textContent = value;
    document.querySelector('#concentration-day-coverage').textContent = `${row.observed} de ${row.grid} horas observadas · ${row.missing} ausentes${row.observed < row.grid && row.observed > 0 ? ' · média de dia incompleto' : ''}`;
    slider.setAttribute('aria-valuetext', `${date(row.date)}: ${value}; ${row.observed} de ${row.grid} horas observadas`);
    const ceiling = Math.max(50, Math.ceil(Math.max(...selected.filter(r => r.mean !== null).map(r => r.mean))/50)*50);
    const overview = image.currentSrc.includes('-mobile.svg');
    const x = overview ? (44+(index+.5)/selected.length*420)/4.8 : (64+(index+.5)/selected.length*912)/10;
    cursor.hidden = false;
    cursor.style.left = `${x}%`;
    cursor.style.setProperty('--point-y', row.mean === null ? '100%' : `${(ceiling-row.mean)/ceiling*100}%`);
    cursor.classList.toggle('is-missing', row.mean === null);
    if (announce) document.querySelector('#concentration-day-announcement').textContent = `${date(row.date)}: ${value}.`;
    image.dispatchEvent(new CustomEvent('chart:reading',{detail:{date:row.date,value,coverage:`${row.observed} de ${row.grid} horas observadas · ${row.missing} ausentes`}}));
  }
  function updatePeriod() {
    selected = daily.filter(row => seriesPeriod.value === 'todos' || row.date.startsWith(seriesPeriod.value));
    if (!selected.length) return;
    const observed = selected.reduce((total,r) => total+r.observed,0);
    const grid = selected.reduce((total,r) => total+r.grid,0);
    const mean = selected.reduce((total,r) => total+(r.mean === null ? 0 : r.mean*r.observed),0)/observed;
    const maximum = Math.max(...selected.filter(r => r.max !== null).map(r => r.max));
    document.querySelector('#concentration-mean').replaceChildren(document.createTextNode(number.format(mean)+' '));
    const meanUnit = document.createElement('span'); meanUnit.textContent = 'µg/m³';
    document.querySelector('#concentration-mean').append(meanUnit);
    document.querySelector('#concentration-max').replaceChildren(document.createTextNode(number.format(maximum)+' '));
    document.querySelector('#concentration-max').append(meanUnit.cloneNode(true));
    document.querySelector('#concentration-coverage').replaceChildren(document.createTextNode(number.format(observed/grid*100)));
    const percent = document.createElement('span'); percent.textContent = '%';
    document.querySelector('#concentration-coverage').append(percent);
    slider.max = String(selected.length-1);
    // Começar pelo dia de maior média; não confundir com o máximo horário.
    const peak = selected.reduce((best,r,i) => r.mean !== null && (selected[best].mean === null || r.mean > selected[best].mean) ? i : best, 0);
    showDay(peak);
  }
  fetch('assets/data/serie-diaria.csv').then(response => {
    if (!response.ok) throw new Error('Série diária indisponível');
    return response.text();
  }).then(csv => {
    daily = csv.trim().split(/\r?\n/).slice(1).map(line => {
      const cells = line.split(',');
      return {date:cells[0],mean:cells[1] === '' ? null : Number(cells[1]),max:cells[3] === '' ? null : Number(cells[3]),observed:Number(cells[4]),grid:Number(cells[5]),missing:Number(cells[6]),temperature:cells[7] === '' ? null : Number(cells[7]),humidity:cells[8] === '' ? null : Number(cells[8]),wind:cells[9] === '' ? null : Number(cells[9])};
    });
    if (!daily.length || daily.some(r => !/^\d{4}-\d{2}-\d{2}$/.test(r.date) || (r.mean !== null && !Number.isFinite(r.mean)) || !Number.isFinite(r.grid))) throw new Error('Formato não reconhecido');
    seriesPeriod.dataset.dailyReady = 'true';
    panel.querySelector('.concentration-summary').hidden = false;
    updatePeriod();
    panel.querySelector('.concentration-inspector').hidden = false;
    seriesPeriod.addEventListener('change', updatePeriod);
    image.addEventListener('load', () => showDay(Number(slider.value)));
    slider.addEventListener('input', () => showDay(Number(slider.value)));
    slider.addEventListener('change', () => showDay(Number(slider.value), true));
    // Mesmo leitor para rato, toque e teclado. O hover é limitado a um frame.
    const canvas = image.closest('.concentration-canvas');
    const tip = document.createElement('div');tip.className='chart-tooltip';tip.hidden=true;tip.setAttribute('role','tooltip');tip.id='concentration-hover-value';
    for (const tag of ['span','strong','small']) tip.append(document.createElement(tag));
    canvas.append(tip);
    let reading = null, dismissed = false, hoverFrame = null, pendingPointer = null;
    function placeTip(clientX,clientY) {
      const bounds=canvas.getBoundingClientRect();
      tip.style.left=`${Math.max(8,Math.min(bounds.width-tip.offsetWidth-8,clientX-bounds.left+18))}px`;
      tip.style.top=`${Math.max(8,Math.min(bounds.height-tip.offsetHeight-8,clientY-bounds.top-tip.offsetHeight-15))}px`;
    }
    image.addEventListener('chart:reading',event => {
      reading=event.detail;
      tip.querySelector('span').textContent=date(reading.date)+' · média diária';
      tip.querySelector('strong').textContent=reading.value;
      tip.querySelector('small').textContent=reading.coverage;
    });
    function readPointer(event,announce=false) {
      const bounds=image.getBoundingClientRect(), overview=image.currentSrc.includes('-mobile.svg');
      const position=overview?((event.clientX-bounds.left)/bounds.width*480-44)/420:((event.clientX-bounds.left)/bounds.width*1000-64)/912;
      showDay(Math.max(0,Math.min(selected.length-1,Math.floor(position*selected.length))),announce);
      if (!dismissed && reading) {tip.hidden=false;placeTip(event.clientX,event.clientY);}
    }
    image.addEventListener('pointermove',event => {
      if (event.pointerType!=='mouse' || event.buttons) return;
      pendingPointer={clientX:event.clientX,clientY:event.clientY};
      if (hoverFrame===null) hoverFrame=requestAnimationFrame(() => {hoverFrame=null;if(pendingPointer)readPointer(pendingPointer);});
    });
    canvas.addEventListener('pointerleave',() => {tip.hidden=true;dismissed=false;pendingPointer=null;if(hoverFrame!==null)cancelAnimationFrame(hoverFrame);hoverFrame=null;});
    document.addEventListener('keydown',event => {if(event.key==='Escape'&&!tip.hidden){tip.hidden=true;dismissed=true;}});
    image.addEventListener('load',()=>{tip.hidden=true;});
    const hint=document.createElement('p');hint.className='chart-interaction-hint';hint.textContent='Passe o rato para ler os valores; toque no gráfico ou use o controlo de dias.';
    canvas.closest('.data-chart-scroll').before(hint);
    // Partilha os dados já carregados; não duplica a consulta do CSV.
    document.dispatchEvent(new CustomEvent('pm25:daily-ready',{detail:daily}));
    window.pm25DailyRows=daily;
    let pointerStart = null;
    image.addEventListener('pointerdown', event => { pointerStart = {x:event.clientX,y:event.clientY}; });
    image.addEventListener('pointerup', event => {
      if (event.button !== 0 || !pointerStart) return;
      const start = pointerStart; pointerStart = null;
      if (Math.hypot(event.clientX-start.x,event.clientY-start.y) > 10) return;
      dismissed=false;readPointer(event,true);
    });
    image.addEventListener('pointercancel', () => {pointerStart = null;});
  }).catch(() => {
    // SVG e tabela continuam acessíveis se a consulta falhar ou for bloqueada.
    panel.querySelector('.concentration-inspector').hidden = true;
    cursor.hidden = true;
  });
}

/* Visão completa no telemóvel; o SVG integral fica disponível por ampliação. */
for (const picture of document.querySelectorAll('[data-chart-picture]')) {
  const key = picture.dataset.chartPicture;
  const region = document.getElementById('chart-region-'+key);
  const button = document.querySelector('[data-chart-zoom="'+key+'"]');
  const source = picture.querySelector('source');
  if (!region || !button || !source) continue;
  button.hidden = false;
  button.addEventListener('click', () => {
    const expanded = button.getAttribute('aria-pressed') !== 'true';
    button.setAttribute('aria-pressed',String(expanded));
    button.textContent = expanded ? 'Voltar à visão completa' : 'Ampliar gráfico';
    region.classList.toggle('chart-zoomed',expanded);
    source.media = expanded ? 'not all' : '(max-width: 650px)';
    region.scrollLeft = 0;
  });
}

/* Separadores progressivos: a selecção troca o painel sem deslocar a página. */
(() => {
  const navigation = document.querySelector('.materials-navigation');
  if (!navigation) return;
  const tabs = [...navigation.querySelectorAll('a[href^="#"]')];
  const panels = tabs.map(tab => document.querySelector(tab.getAttribute('href')));
  if (panels.some(panel => !panel)) return;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  let selected = -1;
  let animation;
  function select(index, {focus=false,updateUrl=false,animate=true}={}) {
    if (index < 0 || index >= panels.length) return;
    const changed = selected !== index;
    selected = index;
    tabs.forEach((tab,i) => {
      tab.setAttribute('aria-selected',String(i === index));
      tab.tabIndex = i === index ? 0 : -1;
      panels[i].hidden = i !== index;
    });
    if (updateUrl) history.replaceState(null,'',tabs[index].getAttribute('href'));
    if (focus) tabs[index].focus({preventScroll:true});
    if (changed) {
      animation?.cancel();
      if (animate && !reduced.matches && !document.documentElement.classList.contains('motion-paused')) {
        animation = panels[index].animate([{opacity:.45,transform:'translateY(5px)'},{opacity:1,transform:'translateY(0)'}],{duration:200,easing:'ease-out'});
      }
    }
  }
  function indexForTarget(target) {
    return panels.findIndex(panel => panel === target || panel.contains(target));
  }
  function followHash() {
    let target;
    try { target = document.getElementById(decodeURIComponent(location.hash.slice(1))); } catch {return;}
    const index = indexForTarget(target);
    if (index >= 0) select(index,{animate:false});
  }
  navigation.setAttribute('role','tablist');
  navigation.setAttribute('aria-orientation','horizontal');
  tabs.forEach((tab,index) => {
    tab.id = `materials-tab-${index+1}`;
    tab.setAttribute('role','tab');
    tab.setAttribute('aria-controls',panels[index].id);
    tab.removeAttribute('aria-current');
    panels[index].setAttribute('role','tabpanel');
    panels[index].setAttribute('aria-labelledby',tab.id);
    panels[index].tabIndex = 0;
    tab.addEventListener('click',event => {
      if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      select(index,{updateUrl:true});
    });
    tab.addEventListener('keydown',event => {
      let next;
      if (event.key === 'ArrowRight' || event.key === 'ArrowDown') next = (index+1)%tabs.length;
      if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') next = (index-1+tabs.length)%tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length-1;
      if (next === undefined) return;
      event.preventDefault();
      select(next,{focus:true,updateUrl:true});
    });
  });
  document.addEventListener('materials:reveal',event => {
    const index = indexForTarget(event.detail?.target);
    if (index >= 0) select(index,{animate:false});
  });
  window.addEventListener('hashchange',followHash);
  window.addEventListener('popstate',followHash);
  reduced.addEventListener('change',() => {if (reduced.matches) animation?.cancel();});
  navigation.classList.add('materials-tabs-ready');
  select(0,{animate:false});
  followHash();
})();
