/* Feedback informativo, sem bibliotecas: valores do CSV e controlos nativos. */
(() => {
  const number=new Intl.NumberFormat('pt-PT',{minimumFractionDigits:2,maximumFractionDigits:2});
  const date=value=>new Intl.DateTimeFormat('pt-PT',{timeZone:'UTC',day:'2-digit',month:'short',year:'numeric'}).format(new Date(value));
  const time=value=>new Intl.DateTimeFormat('pt-PT',{timeZone:'UTC',day:'2-digit',month:'short',year:'numeric',hour:'2-digit',minute:'2-digit'}).format(new Date(value));
  function chart(key,rows,describe,coordinates) {
    const picture=document.querySelector(`[data-chart-picture="${key}"]`);
    const region=document.querySelector('#chart-region-'+key);
    const image=picture?.querySelector('img');
    if(!region||!image||!rows.length||region.dataset.feedbackReady)return;
    region.dataset.feedbackReady='true';picture.classList.add('chart-feedback-stage');
    const tip=document.createElement('div');tip.className='chart-tooltip';tip.hidden=true;tip.setAttribute('role','tooltip');
    for(const tag of ['span','strong','small'])tip.append(document.createElement(tag));
    const line=document.createElement('span');line.className='chart-feedback-cursor';line.hidden=true;line.setAttribute('aria-hidden','true');line.append(document.createElement('i'));
    picture.append(tip,line);
    const controls=document.createElement('div');controls.className='chart-feedback-controls';
    const reading=document.createElement('p');reading.className='chart-feedback-reading';reading.append(document.createElement('span'),document.createElement('strong'),document.createElement('small'));
    const label=document.createElement('label');label.htmlFor='chart-reader-'+key;label.textContent=key==='temperatura'?'Percorrer os dias':'Percorrer as horas do exemplo';
    const slider=document.createElement('input');slider.id=label.htmlFor;slider.type='range';slider.min='0';slider.max=String(rows.length-1);slider.value='0';
    controls.append(reading,label,slider);region.after(controls);
    const hint=document.createElement('p');hint.className='chart-interaction-hint';hint.id='chart-hint-'+key;hint.textContent='Explore com o rato ou por toque. Com o gráfico focado, use as setas esquerda/direita, Home ou End.';region.before(hint);
    region.setAttribute('aria-describedby',[region.getAttribute('aria-describedby'),hint.id].filter(Boolean).join(' '));
    let index=0,dismissed=false,frame=null,pointer=null,start=null;
    function show(i){
      index=Math.max(0,Math.min(rows.length-1,i));slider.value=String(index);
      const info=describe(rows[index]);
      for(const container of [reading,tip]){
        container.querySelector('span').textContent=info.label;
        container.querySelector('strong').textContent=info.value;
        container.querySelector('small').textContent=info.note;
      }
      slider.setAttribute('aria-valuetext',`${info.label}: ${info.value}. ${info.note}`);
      const coord=coordinates(rows[index],index,image.currentSrc.includes('-mobile.svg'));
      line.hidden=false;line.style.left=`${coord.x*100}%`;line.style.top=`${coord.top*100}%`;line.style.height=`${coord.height*100}%`;
      line.classList.toggle('is-missing',coord.y===null);line.style.setProperty('--point-y',coord.y===null?'100%':`${coord.y*100}%`);
    }
    function position(event){
      const box=image.getBoundingClientRect(),mobile=image.currentSrc.includes('-mobile.svg');
      const startX=mobile?44/480:64/1000;
      const endX=mobile?464/480:976/1000;
      const relative=((event.clientX-box.left)/box.width-startX)/(endX-startX);
      const fraction=Math.max(0,Math.min(1,relative));
      show(key==='temperatura'?Math.min(rows.length-1,Math.floor(fraction*rows.length)):Math.round(fraction*(rows.length-1)));
      if(dismissed)return;
      tip.hidden=false;
      const parent=picture.getBoundingClientRect();
      tip.style.left=`${Math.max(8,Math.min(parent.width-tip.offsetWidth-8,event.clientX-parent.left+15))}px`;
      tip.style.top=`${Math.max(8,Math.min(parent.height-tip.offsetHeight-8,event.clientY-parent.top-tip.offsetHeight-15))}px`;
    }
    slider.addEventListener('input',()=>show(Number(slider.value)));
    region.addEventListener('keydown',event=>{
      if(event.target!==region)return;
      let next;if(event.key==='ArrowRight')next=index+1;if(event.key==='ArrowLeft')next=index-1;if(event.key==='Home')next=0;if(event.key==='End')next=rows.length-1;
      if(next!==undefined){event.preventDefault();show(next);}
    });
    image.addEventListener('pointermove',event=>{
      if(event.pointerType!=='mouse'||event.buttons)return;
      pointer={clientX:event.clientX,clientY:event.clientY};
      if(frame===null)frame=requestAnimationFrame(()=>{frame=null;if(pointer)position(pointer);});
    });
    image.addEventListener('pointerdown',e=>{start={x:e.clientX,y:e.clientY};});
    image.addEventListener('pointerup',e=>{if(!start||e.button!==0)return;const p=start;start=null;if(Math.hypot(e.clientX-p.x,e.clientY-p.y)>10)return;dismissed=false;position(e);});
    image.addEventListener('pointercancel',()=>{start=null;});
    picture.addEventListener('pointerleave',()=>{tip.hidden=true;dismissed=false;pointer=null;if(frame!==null)cancelAnimationFrame(frame);frame=null;});
    document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!tip.hidden){dismissed=true;tip.hidden=true;}});
    image.addEventListener('load',()=>{tip.hidden=true;show(index);});
    show(0);
  }
  function temperature(rows){
    const values=rows.filter(r=>r.temperature!==null).map(r=>r.temperature);if(!values.length)return;
    const max=Math.ceil(Math.max(...values)/5)*5;
    chart('temperatura',rows,row=>({label:date(row.date+'T12:00:00Z')+' · média diária',value:row.temperature===null?'Sem observação':number.format(row.temperature)+' °C',note:`Humidade: ${row.humidity===null?'—':number.format(row.humidity)+'%'} · vento: ${row.wind===null?'—':number.format(row.wind)+' m/s'}. Faixa inferior: ausências de PM2.5.`}),
      (row,i,mobile)=>({x:mobile?(44+(i+.5)/rows.length*420)/480:(64+(i+.5)/rows.length*912)/1000,top:mobile?32/300:36/380,height:mobile?175/300:270/380,y:row.temperature===null?null:(max-row.temperature)/max}));
  }
  document.addEventListener('pm25:daily-ready',event=>temperature(event.detail),{once:true});
  if(window.pm25DailyRows)temperature(window.pm25DailyRows);
  if(document.querySelector('[data-chart-picture="horizontes"]')){
    fetch('assets/data/exemplo-horario.csv').then(r=>{if(!r.ok)throw Error();return r.text();}).then(csv=>{
      const rows=csv.trim().split(/\r?\n/).slice(1).map(line=>{const r=line.split(',');return {timestamp:r[0].replace(' ','T'),value:r[1]===''?null:Number(r[1])};});
      if(rows.some(r=>!Number.isFinite(new Date(r.timestamp).getTime())||r.value!==null&&!Number.isFinite(r.value)))return;
      const origin=Date.parse('2020-12-02T12:00:00Z');
      chart('horizontes',rows,row=>{
        const h=(Date.parse(row.timestamp)-origin)/3600000;
        const label=h<0?`Histórico · t${h} h`:h===0?'Origem t':[1,3,6].includes(h)?`Alvo de ${h} h`:`Histórico futuro · t+${h} h`;
        return {label:time(row.timestamp)+' UTC · '+label,value:row.value===null?'Sem observação':number.format(row.value)+' µg/m³',note:h<0?'Observação anterior à origem; possível entrada histórica.':h===0?'Valor na origem; não entra nos atributos estritamente anteriores a t.':'Observação histórica futura, não previsão produzida por modelo.'};
      },(row,i,mobile)=>({x:mobile?(44+i/(rows.length-1)*420)/480:(64+i/(rows.length-1)*912)/1000,top:mobile?32/300:60/380,height:mobile?175/300:220/380,y:row.value===null?null:(100-row.value)/100}));
    }).catch(()=>{/* SVG e explicação estáticos permanecem disponíveis. */});
  }
})();
