"""Vistas móveis das mesmas séries diárias. Sem reamostragem, suavização ou novos valores."""
from pathlib import Path
import csv,json,math,datetime as dt
from html import escape
out=Path('assets/data');rows=list(csv.DictReader((out/'serie-diaria.csv').open()));gaps=json.loads((out/'lacunas.json').read_text())
css='''<style>text{font:16px system-ui,sans-serif;fill:#525650}.grid{stroke:#dedfd6;stroke-dasharray:3 5}.curve{fill:none;stroke:#b84b00;stroke-width:1.25}.gap{fill:#596d7b}.back{fill:#dedfd6}.peak{fill:#b84b00}@media(prefers-color-scheme:dark){text{fill:#c0c5b9}.grid,.back{stroke:#354036;fill:none}.curve{stroke:#ffb17c}.gap{fill:#91b5c8}.peak{fill:#ffb17c}}</style>'''
def overview(name,selected,field='pm25_mean_ug_m3',unit='PM2.5 · µg/m³'):
 start=dt.datetime.fromisoformat(selected[0]['date_utc']).replace(tzinfo=dt.timezone.utc);end=dt.datetime.fromisoformat(selected[-1]['date_utc']).replace(tzinfo=dt.timezone.utc)+dt.timedelta(days=1)
 vals=[float(r[field]) for r in selected if r[field]];ceiling=max(50,math.ceil(max(vals)/50)*50) if field.startswith('pm25') else math.ceil(max(vals)/5)*5
 x=lambda t:44+(t-start).total_seconds()/(end-start).total_seconds()*420
 y=lambda v:32+(ceiling-v)/ceiling*175
 svg=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 300" role="img" aria-labelledby="t d"><title id="t">{escape(unit)} · vista móvel</title><desc id="d">Visão completa das médias diárias do mesmo ficheiro, sem interpolação. Faixa inferior: ausências de PM2.5.</desc>{css}<defs><linearGradient id="a" x2="0" y2="1"><stop stop-color="#f96501" stop-opacity=".3"/><stop offset="1" stop-color="#f96501" stop-opacity=".03"/></linearGradient></defs><text x="44" y="20">{escape(unit)}</text>']
 for v in [0,ceiling/2,ceiling]:
  yy=y(v);svg.append(f'<path class="grid" d="M44 {yy}H464"/><text x="36" y="{yy+5}" text-anchor="end">{v:g}</text>')
 segments=[];pts=[]
 for r in selected:
  if not r[field]:
   if pts:segments.append(pts);pts=[]
  else:pts.append((x(dt.datetime.fromisoformat(r['date_utc']).replace(tzinfo=dt.timezone.utc)+dt.timedelta(hours=12)),y(float(r[field]))))
 if pts:segments.append(pts)
 for pts in segments:
  path=' '.join(('M' if i==0 else 'L')+f'{a:.2f},{b:.2f}' for i,(a,b) in enumerate(pts))
  svg.append(f'<path d="{path}L{pts[-1][0]:.2f},207L{pts[0][0]:.2f},207Z" fill="url(#a)"/><path class="curve" d="{path}"/>')
 for i in range(3):
  t=start+(end-start)*i/2;label=t.strftime('%d/%m') if (end-start).days<70 else t.strftime('%m/%Y');align=['start','middle','end'][i];svg.append(f'<text x="{x(t)}" y="232" text-anchor="{align}">{label}</text>')
 svg.append('<rect class="back" x="44" y="249" width="420" height="10" rx="3"/>')
 for g in gaps:
  a=max(start,dt.datetime.fromisoformat(g['start_utc']));b=min(end,dt.datetime.fromisoformat(g['end_utc'])+dt.timedelta(hours=1))
  if b>a:svg.append(f'<rect class="gap" x="{x(a):.2f}" y="249" width="{x(b)-x(a):.2f}" height="10"/>')
 svg.append('<text x="44" y="286">Horas sem observação de PM2.5</text></svg>')
 (out/name).write_text(''.join(svg))
overview('pm25-todos-mobile.svg',rows)
for year in range(2020,2027):overview(f'pm25-{year}-mobile.svg',[r for r in rows if r['date_utc'].startswith(str(year))])
overview('temperatura-mobile.svg',rows,'temperature_mean_degC','Temperatura · °C')
# Mesma janela horária e mesmos três alvos, com rótulos adaptados ao ecrã.
pm=list(csv.DictReader((out/'exemplo-horario.csv').open()));origin=dt.datetime(2020,12,2,12,tzinfo=dt.timezone.utc);start=origin-dt.timedelta(hours=24);end=origin+dt.timedelta(hours=8);x=lambda t:44+(t-start).total_seconds()/(end-start).total_seconds()*420;y=lambda v:32+(100-v)/100*175
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 300" role="img" aria-labelledby="t d"><title id="t">Uma origem, três alvos históricos</title><desc id="d">Mesmos valores horários e alvos do gráfico ampliado. Os pontos depois da origem são observações históricas, não previsões.</desc>{css}<text x="44" y="20">PM2.5 · µg/m³ · 02/12/2020 UTC</text><rect x="{x(origin)}" y="32" width="{464-x(origin)}" height="175" fill="#ecc5a5" opacity=".25"/>']
for v in [0,50,100]:svg.append(f'<path class="grid" d="M44 {y(v)}H464"/><text x="36" y="{y(v)+5}" text-anchor="end">{v}</text>')
svg.append('<path class="curve" d="'+' '.join(('M' if i==0 else 'L')+f'{x(dt.datetime.fromisoformat(r["timestamp_utc"])):.2f},{y(float(r["pm2_5"])):.2f}' for i,r in enumerate(pm))+'"/>')
svg.append(f'<path d="M{x(origin)} 32V207" stroke="#676d61" stroke-dasharray="4 3"/><text x="44" y="235">Passado disponível</text><text x="464" y="235" text-anchor="end">t · 12h UTC</text>')
for i,h in enumerate([1,3,6]):
 t=origin+dt.timedelta(hours=h);r=next(r for r in pm if dt.datetime.fromisoformat(r['timestamp_utc'])==t);xx=x(t);yy=y(float(r['pm2_5']));svg.append(f'<circle class="peak" cx="{xx}" cy="{yy}" r="3.5"/><text x="{xx}" y="{60+i*25}" text-anchor="middle">+{h}h</text>')
svg.append('<text x="44" y="282">Alvos observados, não previsões.</text></svg>');(out/'horizontes-mobile.svg').write_text(''.join(svg))
