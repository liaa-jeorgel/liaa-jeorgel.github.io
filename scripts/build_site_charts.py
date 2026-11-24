"""SVG estáticos dos derivados conferidos. Sem bibliotecas de gráficos no navegador."""
import csv,datetime as dt,json,math,argparse
from pathlib import Path
from html import escape
out=Path('assets/data');rows=list(csv.DictReader((out/'serie-diaria.csv').open()));gaps=json.loads((out/'lacunas.json').read_text())
W,H,L,R,T,B=1000,380,64,24,36,74
style='<style>text{font-family:system-ui,sans-serif;fill:#525650;font-size:14px}.grid{stroke:#dedfd6;stroke-width:1}.curve{fill:none;stroke:#b84b00;stroke-width:1.6;stroke-linejoin:round} @media(prefers-color-scheme:dark){text{fill:#c0c5b9}.grid{stroke:#354036}.curve{stroke:#ffb17c}}</style>'
def chart(name,selected,field='pm25_mean_ug_m3',unit='PM2.5 · µg/m³',color='#b84b00'):
 start=dt.datetime.fromisoformat(selected[0]['date_utc']).replace(tzinfo=dt.timezone.utc);end=dt.datetime.fromisoformat(selected[-1]['date_utc']).replace(tzinfo=dt.timezone.utc)+dt.timedelta(days=1);span=(end-start).total_seconds();vs=[float(r[field]) for r in selected if r[field]];ymax=math.ceil(max(vs)/5)*5 if field!='pm25_mean_ug_m3' else math.ceil(max(vs)/50)*50;ymin=0
 x=lambda t:L+(t-start).total_seconds()/span*(W-L-R)
 y=lambda v:T+(ymax-v)/(ymax-ymin)*(H-T-B)
 svg=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc"><title id="title">{escape(unit)}: médias diárias de {start:%Y-%m-%d} a {end-dt.timedelta(days=1):%Y-%m-%d}</title><desc id="desc">Médias dos valores disponíveis em cada dia. Interrupções sem interpolação; faixa inferior marca horas ausentes de PM2.5. Dias parciais podem conter menos de 24 observações.</desc>{style}<text x="{L}" y="20">{escape(unit)}</text>']
 for i in range(5):
  v=ymax*i/4;yy=y(v);svg+=[f'<path class="grid" d="M{L} {yy:.1f}H{W-R}"/><text x="{L-10}" y="{yy+5:.1f}" text-anchor="end">{v:g}</text>']
 paths=[];current=[]
 for r in selected:
  if not r[field]:
   if current:paths.append(current);current=[]
  else:current.append((x(dt.datetime.fromisoformat(r['date_utc']).replace(tzinfo=dt.timezone.utc)+dt.timedelta(hours=12)),y(float(r[field]))))
 if current:paths.append(current)
 for points in paths:svg.append('<path class="curve" d="'+' '.join(('M' if i==0 else 'L')+f'{xx:.2f},{yy:.2f}' for i,(xx,yy) in enumerate(points))+'"/>')
 for i in range(7):
  t=start+(end-start)*i/6;xx=x(t);svg.append(f'<text x="{xx:.1f}" y="{H-B+25}" text-anchor="middle">{t:%m/%Y}</text>')
 svg.append(f'<rect x="{L}" y="{H-32}" width="{W-L-R}" height="10" rx="3" fill="#dedfd6"/>')
 for g in gaps:
  a=max(start,dt.datetime.fromisoformat(g['start_utc']));b=min(end,dt.datetime.fromisoformat(g['end_utc'])+dt.timedelta(hours=1))
  if b>a:svg.append(f'<rect x="{x(a):.2f}" y="{H-32}" width="{x(b)-x(a):.2f}" height="10" fill="#b84b00"/>')
 svg.append(f'<text x="{L}" y="{H-5}">Faixa de ausências de PM2.5 · UTC</text></svg>');(out/name).write_text(''.join(svg))
def concentration_chart(name, selected):
 # Mesmo agregado diário; apenas apresentação. Lacunas nunca são ligadas por uma curva.
 width,height,left,right,top,bottom=1000,440,64,24,60,90
 start=dt.datetime.fromisoformat(selected[0]['date_utc']).replace(tzinfo=dt.timezone.utc)
 end=dt.datetime.fromisoformat(selected[-1]['date_utc']).replace(tzinfo=dt.timezone.utc)+dt.timedelta(days=1)
 span=(end-start).total_seconds();values=[float(r['pm25_mean_ug_m3']) for r in selected if r['pm25_mean_ug_m3']]
 ceiling=max(50,math.ceil(max(values)/50)*50);base=height-bottom
 x=lambda t:left+(t-start).total_seconds()/span*(width-left-right)
 y=lambda v:top+(ceiling-v)/ceiling*(base-top)
 theme='<style>text{font-family:system-ui,sans-serif;fill:#525650;font-size:14px}.grid{stroke:#dedfd6;stroke-width:1;stroke-dasharray:3 6}.curve{fill:none;stroke:#b84b00;stroke-width:1.8;stroke-linejoin:round}.peak-text{fill:#b84b00;font-weight:600}.peak-bg{fill:#fffefa;stroke:#ecc5a5}.gap{fill:#596d7b}.back{fill:#f5f4ee}@media(prefers-color-scheme:dark){text{fill:#c0c5b9}.grid{stroke:#354036}.curve{stroke:#ffb17c}.peak-text{fill:#ffb17c}.peak-bg{fill:#161c18;stroke:#7c5230}.gap{fill:#91b5c8}.back{fill:#1d241f}}</style>'
 svg=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc"><title id="title">Concentração de PM2.5: {start:%Y-%m-%d} a {end-dt.timedelta(days=1):%Y-%m-%d}</title><desc id="desc">Médias diárias sem interpolação, área sombreada e maior média diária assinalada. Faixa azul-cinzenta: horas sem observação, não níveis de risco. Valores em microgramas por metro cúbico.</desc>{theme}<defs><linearGradient id="concentration-area" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f96501" stop-opacity=".4"/><stop offset="100%" stop-color="#f96501" stop-opacity=".045"/></linearGradient></defs><text x="{left}" y="26">PM2.5 · µg/m³</text><text x="976" y="26" text-anchor="end">MÉDIAS DIÁRIAS · UTC</text>']
 for i in range(5):
  v=ceiling*i/4;yy=y(v);svg.append(f'<path class="grid" d="M{left} {yy:.1f}H976"/><text x="54" y="{yy+5:.1f}" text-anchor="end">{v:g}</text>')
 segments=[];points=[]
 for r in selected:
  if not r['pm25_mean_ug_m3']:
   if points:segments.append(points);points=[]
  else:points.append((x(dt.datetime.fromisoformat(r['date_utc']).replace(tzinfo=dt.timezone.utc)+dt.timedelta(hours=12)),y(float(r['pm25_mean_ug_m3']))))
 if points:segments.append(points)
 for points in segments:
  path=' '.join(('M' if i==0 else 'L')+f'{xx:.2f},{yy:.2f}' for i,(xx,yy) in enumerate(points))
  svg.append(f'<path d="{path} L{points[-1][0]:.2f},{base} L{points[0][0]:.2f},{base} Z" fill="url(#concentration-area)"/>')
  if len(points)==1:svg.append(f'<circle cx="{points[0][0]:.2f}" cy="{points[0][1]:.2f}" r="2" fill="#b84b00"/>')
  else:svg.append(f'<path class="curve" d="{path}"/>')
 peak=max((r for r in selected if r['pm25_mean_ug_m3']),key=lambda r:float(r['pm25_mean_ug_m3']));peak_date=dt.datetime.fromisoformat(peak['date_utc']).replace(tzinfo=dt.timezone.utc);px=x(peak_date+dt.timedelta(hours=12));py=y(float(peak['pm25_mean_ug_m3']));bx=min(750,max(70,px+15));by=max(42,py-68)
 val=f"{float(peak['pm25_mean_ug_m3']):.2f}".replace('.',',')
 svg.append(f'<path d="M{px:.1f} {py:.1f}V{base}" stroke="#f96501" stroke-opacity=".25" stroke-dasharray="3 4"/><circle cx="{px:.1f}" cy="{py:.1f}" r="5" fill="#b84b00" stroke="#fffefa" stroke-width="2"/><rect class="peak-bg" x="{bx:.1f}" y="{by:.1f}" width="210" height="49" rx="8"/><text class="peak-text" x="{bx+12:.1f}" y="{by+20:.1f}">{val} µg/m³</text><text x="{bx+12:.1f}" y="{by+38:.1f}">Máx. diário · {peak_date:%d/%m/%Y}</text>')
 for i in range(7):
  t=start+(end-start)*i/6;tick=t.strftime('%d/%m') if span<86400*70 else t.strftime('%m/%Y');xx=x(t);anchor='start' if i==0 else 'end' if i==6 else 'middle';svg.append(f'<text x="{xx:.1f}" y="377" text-anchor="{anchor}">{tick}</text>')
 svg.append('<rect class="back" x="64" y="395" width="912" height="12" rx="4"/>')
 for g in gaps:
  a=max(start,dt.datetime.fromisoformat(g['start_utc']));b=min(end,dt.datetime.fromisoformat(g['end_utc'])+dt.timedelta(hours=1))
  if b>a:svg.append(f'<rect class="gap" x="{x(a):.2f}" y="395" width="{x(b)-x(a):.2f}" height="12"/>')
 svg.append('<text x="64" y="432">Horas sem observação de PM2.5 · sem preenchimento</text></svg>')
 (out/name).write_text(''.join(svg))
concentration_chart('pm25-todos.svg',rows)
for year in range(2020,2027):concentration_chart('pm25-'+str(year)+'.svg',[r for r in rows if r['date_utc'].startswith(str(year))])
for field,name,unit in [('temperature_mean_degC','temperatura.svg','Temperatura · °C'),('humidity_mean_pct','humidade.svg','Humidade relativa · %'),('wind_speed_mean_m_s','vento.svg','Velocidade do vento · m/s')]:chart(name,rows,field,unit)
# Janela real com a mesma origem dos primeiros exemplos supervisionados.
pmfile=out/'exemplo-horario.csv';pm=list(csv.DictReader(pmfile.open()));origin=dt.datetime(2020,12,2,12,tzinfo=dt.timezone.utc);start=origin-dt.timedelta(hours=24);end=origin+dt.timedelta(hours=8);selected=[r for r in pm if start<=dt.datetime.fromisoformat(r['timestamp_utc'])<=end];x=lambda t:L+(t-start).total_seconds()/(end-start).total_seconds()*(W-L-R);y=lambda v:280-v/100*220
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 380" role="img" aria-labelledby="title desc"><title id="title">Uma origem, três alvos históricos</title><desc id="desc">Origem 2 de dezembro de 2020 às 12 UTC. Os alvos são observações em t mais 1, 3 e 6 horas, não previsões produzidas por modelos.</desc>{style}<rect x="{x(origin):.1f}" y="35" width="{W-R-x(origin):.1f}" height="245" fill="#ecc5a5" opacity=".25"/><text x="64" y="22">PM2.5 · µg/m³ · valores horários</text>']
for v in [0,25,50,75,100]:svg.append(f'<path class="grid" d="M64 {y(v)}H976"/><text x="54" y="{y(v)+5}" text-anchor="end">{v}</text>')
svg.append('<path class="curve" d="'+' '.join(('M' if i==0 else 'L')+f'{x(dt.datetime.fromisoformat(r["timestamp_utc"])):.1f},{y(float(r["pm2_5"])):.1f}' for i,r in enumerate(selected))+'"/>')
svg.append(f'<path d="M{x(origin):.1f} 35V280" stroke="#525650" stroke-dasharray="5 4"/><text x="{x(origin)-10:.1f}" y="320" text-anchor="end">t · 02/12/2020 12h UTC</text><text x="64" y="350">Histórico estritamente anterior a t</text><text x="{x(origin)+12:.1f}" y="350">Alvos observados</text>')
for h in [1,3,6]:
 t=origin+dt.timedelta(hours=h);r=next(r for r in selected if dt.datetime.fromisoformat(r['timestamp_utc'])==t);xx=x(t);yy=y(float(r['pm2_5']));svg.append(f'<circle cx="{xx:.1f}" cy="{yy:.1f}" r="5" fill="#b84b00"/><path d="M{xx:.1f} {yy-8:.1f}V{50+h*18}" stroke="#b84b00" stroke-dasharray="3 3"/><text x="{xx:.1f}" y="{44+h*18}" text-anchor="middle">+{h} h</text>')
svg.append('</svg>');(out/'horizontes.svg').write_text(''.join(svg))
