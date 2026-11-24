"""Estatísticas exactas de Luanda a partir do CSV preparado fornecido pelo autor."""
import argparse,csv,datetime as dt,hashlib,json,math
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--pm25',required=True,type=Path);p.add_argument('--output',type=Path,default=Path('assets/data/luanda-map-statistics.json'));args=p.parse_args()
raw=args.pm25.read_bytes();audit=json.loads(Path('assets/data/audit.json').read_text());sha=hashlib.sha256(raw).hexdigest();assert sha==audit['files']['pm25']['sha256'],'O CSV difere do insumo anteriormente conferido'
rows=list(csv.DictReader(raw.decode('utf-8-sig').splitlines()));periods={}
for key in ['todos']+sorted({r['timestamp_utc'][:4] for r in rows}):
 selected=[r for r in rows if key=='todos' or r['timestamp_utc'].startswith(key)];times=[dt.datetime.fromisoformat(r['timestamp_utc']) for r in selected];values=[]
 for r in selected:
  try:v=float(r['pm2_5'])
  except (ValueError,TypeError):continue
  if math.isfinite(v):values.append(v)
 assert len(times)==len(set(times));assert all(b-a==dt.timedelta(hours=1) for a,b in zip(times,times[1:]))
 year=int(key) if key!='todos' else None
 full_year=bool(year and min(times)==dt.datetime(year,1,1,tzinfo=dt.timezone.utc) and max(times)==dt.datetime(year,12,31,23,tzinfo=dt.timezone.utc))
 periods[key]={'start_utc':min(times).isoformat(),'end_utc':max(times).isoformat(),'grid_hours':len(selected),'observed_hours':len(values),'missing_hours':len(selected)-len(values),'coverage_percent':len(values)/len(selected)*100,'mean_ug_m3':sum(values)/len(values),'max_ug_m3':max(values),'min_ug_m3':min(values),'complete_calendar_year':full_year}
assert periods['todos']['observed_hours']==audit['observations'];assert math.isclose(periods['todos']['mean_ug_m3'],audit['mean'],abs_tol=1e-9)
result={'city':'Luanda','source':'OpenWeather Air Pollution API — atribuição declarada pelo autor','nature':'Histórico fornecido; origem física não autenticada; não representa medição local certificada nem resultados de treino','input_name':args.pm25.name,'input_sha256':sha,'verified_on':'2026-11-24','unit':'µg/m³','aggregation':'Média aritmética das concentrações horárias presentes. Ausências não entram como zero. Cobertura relativamente às horas da grade no período; anos parciais identificados.','periods':periods}
args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(periods,indent=2))
