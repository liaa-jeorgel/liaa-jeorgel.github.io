/* Percurso progressivo: sem JS, as seis explicações permanecem na página. */
(() => {
  const section = document.querySelector('#evolucao');
  const route = section?.querySelector('.evolution-route');
  if (!route) return;
  const tabs = [...route.querySelectorAll('[data-evolution-step]')];
  const panels = [...section.querySelectorAll('.evolution-detail')];
  if (tabs.length !== panels.length || !tabs.length) return;
  const controls = section.querySelector('.evolution-controls');
  const previous = controls.querySelector('[data-evolution-direction="-1"]');
  const next = controls.querySelector('[data-evolution-direction="1"]');
  const compact = matchMedia('(max-width: 760px)');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  let selected = 2;
  let animation;
  const indexForHash = () => {
    let hash;
    try { hash = decodeURIComponent(location.hash.slice(1)); } catch { return -1; }
    return panels.findIndex(panel => panel.id === hash);
  };
  function select(index, {focusTab=false,focusPanel=false,updateUrl=false,animate=true}={}) {
    if (index < 0 || index >= panels.length) return;
    const changed = index !== selected;
    selected = index;
    tabs.forEach((tab, i) => {
      tab.setAttribute('aria-selected', String(i === index));
      tab.tabIndex = i === index ? 0 : -1;
      panels[i].hidden = i !== index;
    });
    previous.disabled = index === 0;
    next.disabled = index === panels.length-1;
    controls.querySelector('.evolution-position').textContent = `Etapa ${index+1} de ${panels.length}`;
    if (updateUrl) history.replaceState(null, '', '#'+panels[index].id);
    if (compact.matches) {
      const item = tabs[index].parentElement;
      route.scrollLeft += item.getBoundingClientRect().left-route.getBoundingClientRect().left-12;
    }
    if (focusTab) tabs[index].focus({preventScroll:true});
    if (focusPanel) {
      panels[index].focus({preventScroll:true});
      panels[index].scrollIntoView({block:'start',behavior:'instant'});
    }
    if (changed && animate && !reduced.matches && !document.documentElement.classList.contains('motion-paused')) {
      animation?.cancel();
      animation = panels[index].animate([{opacity:.5,transform:'translateY(6px)'},{opacity:1,transform:'translateY(0)'}],{duration:200,easing:'ease-out'});
    }
  }
  route.setAttribute('role','tablist');
  const orient = () => route.setAttribute('aria-orientation', compact.matches ? 'horizontal' : 'vertical');
  orient(); compact.addEventListener('change', orient);
  tabs.forEach((tab,index) => {
    tab.parentElement.setAttribute('role','presentation');
    tab.setAttribute('role','tab');
    tab.setAttribute('aria-controls',panels[index].id);
    panels[index].setAttribute('role','tabpanel');
    panels[index].setAttribute('aria-labelledby',tab.id);
    panels[index].tabIndex = 0;
    tab.addEventListener('keydown',event => {
      let target;
      if (event.key === 'ArrowRight' || event.key === 'ArrowDown') target = (index+1)%tabs.length;
      if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') target = (index-1+tabs.length)%tabs.length;
      if (event.key === 'Home') target = 0;
      if (event.key === 'End') target = tabs.length-1;
      if (target === undefined) return;
      event.preventDefault();select(target,{focusTab:true,updateUrl:true});
    });
  });
  section.querySelectorAll('a[href^="#evolucao-"]').forEach(link => link.addEventListener('click',event => {
    if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const index = panels.findIndex(panel => '#'+panel.id === link.getAttribute('href'));
    if (index < 0) return;
    event.preventDefault();
    select(index,{focusPanel:!route.contains(link),updateUrl:true});
  }));
  controls.querySelectorAll('button').forEach(button => button.addEventListener('click',() => {
    select(selected+Number(button.dataset.evolutionDirection),{focusPanel:true,updateUrl:true});
  }));
  const followHash = () => { const index = indexForHash(); if (index >= 0) select(index,{animate:false}); };
  window.addEventListener('hashchange',followHash);
  window.addEventListener('popstate',followHash);
  reduced.addEventListener('change', () => { if (reduced.matches) animation?.cancel(); });
  section.classList.add('evolution-ready');
  controls.hidden = false;
  const initial = indexForHash();
  select(initial >= 0 ? initial : 2,{animate:false});
})();
