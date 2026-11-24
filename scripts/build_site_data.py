import csv,datetime as dt,math,json,hashlib,collections
from pathlib import Path
import argparse
parser=argparse.ArgumentParser(description='Conferir os cinco CSV e gerar derivados públicos, sem modificar os originais.')
for key in ['pm25','h1','h3','h6','weather']:parser.add_argument('--'+key,required=True,type=Path)
parser.add_argument('--output',type=Path,default=Path('assets/data'))
args=parser.parse_args();files={k:getattr(args,k) for k in ['pm25','h1','h3','h6','weather']};args.output.mkdir(parents=True,exist_ok=True)
parse=dt.datetime.fromisoformat
pm=list(csv.DictReader(files['pm25'].open()));lookup={parse(r['timestamp_utc']):float(r['pm2_5']) if r['pm2_5'] and r['pm2_5'].lower() not in ['nan','na','null'] else None for r in pm};obs=[v for v in lookup.values() if v is not None];gaps=[]
for t,v in lookup.items():
 if v is None:
  if not gaps or t!=gaps[-1]['last']+dt.timedelta(hours=1):gaps.append({'first':t,'last':t,'hours':1})
  else:gaps[-1]['last']=t;gaps[-1]['hours']+=1
weather=list(csv.DictReader(files['weather'].open()));wl={};conflicts=0
for r in weather:
 t=dt.datetime.fromtimestamp(int(r['dt']),dt.timezone.utc);v=[float(r[k]) for k in ['temp','humidity','pressure','wind_speed','wind_deg']];v[0]-=273.15;v[-1]%=360
 if t in wl and wl[t]!=v:conflicts+=1
 wl[t]=v
stats={'period':[min(lookup).isoformat(),max(lookup).isoformat()],'grid':len(pm),'observations':len(obs),'missing':len(pm)-len(obs),'coverage':100*len(obs)/len(pm),'gap_episodes':len(gaps),'max_missing_hours':max(g['hours'] for g in gaps),'mean':sum(obs)/len(obs),'max':max(obs),'min':min(obs),'weather_rows':len(weather),'weather_unique':len(wl),'weather_duplicate_rows':len(weather)-len(wl),'weather_conflicting_selected':conflicts,'weather_overlap':sum(t in wl for t in lookup),'horizons':{},'files':{k:{'name':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for k,p in files.items()}}
for h in [1,3,6]:
 rows=list(csv.DictReader(files['h'+str(h)].open()));features=[k for k in rows[0] if k not in ['timestamp_utc','target_timestamp_utc','target_pm2_5','target_observado','target_extremo_iqr']];errors=collections.Counter();seen=set()
 for r in rows:
  t=parse(r['timestamp_utc']);target=parse(r['target_timestamp_utc'])
  if t in seen:errors['duplicate_origin']+=1
  seen.add(t)
  if target!=t+dt.timedelta(hours=h):errors['target_offset']+=1
  if lookup.get(target)!=float(r['target_pm2_5']):errors['target_value']+=1
  for f in features:
   if not math.isfinite(float(r[f])):errors['nonfinite_feature']+=1
   if f.startswith('pm25_lag_'):
    lag=int(f.split('_')[-1][:-1]);actual=lookup.get(t-dt.timedelta(hours=lag));expected=float(r[f]);
    if actual is None or not math.isclose(actual,expected,abs_tol=1e-8):errors['pm25_lag']+=1
   elif f.startswith('pm25_mean_'):
    n=int(f.split('_')[-1][:-1]);vs=[lookup.get(t-dt.timedelta(hours=j)) for j in range(1,n+1)]
    if None in vs or not math.isclose(sum(vs)/n,float(r[f]),abs_tol=1e-8):errors['pm25_mean']+=1
   elif f.startswith('meteo_'):
    rest=f[6:];var,op,n=rest.rsplit('_',2);n=int(n[:-1]);ix={'air_temperature':0,'relative_humidity':1,'sea_level_pressure':2,'wind_speed':3,'wind_direction':4}[var];ts=[t-dt.timedelta(hours=j) for j in ([n] if op=='lag' else range(1,n+1))];vs=[wl.get(ti,[None]*5)[ix] for ti in ts]
    if None in vs or not math.isclose(sum(vs)/len(vs),float(r[f]),abs_tol=1e-7):errors['weather_feature']+=1
 stats['horizons'][str(h)]={'rows':len(rows),'excluded_vs_grid':len(pm)-len(rows),'features':len(features),'errors':dict(errors)}
# Reconstituir elegibilidade de cada origem apenas com o histórico e o alvo exacto.
for h in [1,3,6]:
 actual={parse(r['timestamp_utc']) for r in csv.DictReader(files['h'+str(h)].open())}
 expected={t for t in lookup if lookup.get(t+dt.timedelta(hours=h)) is not None and all(lookup.get(t-dt.timedelta(hours=j)) is not None and t-dt.timedelta(hours=j) in wl for j in range(1,25))}
 stats['horizons'][str(h)]['eligible_origins_match']=actual==expected
 stats['horizons'][str(h)]['eligible_difference']=len(actual^expected)
assert len(pm)==len(lookup), 'Timestamps PM2.5 repetidos'
assert all(b-a==dt.timedelta(hours=1) for a,b in zip(lookup,list(lookup)[1:])), 'Grade não horária'
assert all((r['observado'].lower()=='true')==(lookup[parse(r['timestamp_utc'])] is not None) and (r['hora_ausente'].lower()=='true')==(lookup[parse(r['timestamp_utc'])] is None) for r in pm), 'Flags incoerentes'
assert not conflicts, 'Meteorologia conflituosa nas variáveis seleccionadas'
assert all(not h['errors'] and h['eligible_origins_match'] for h in stats['horizons'].values()), 'Divergência supervisionada'
stats['verified_on']='2026-11-24';stats['scope']='Verificações independentes dos CSV fornecidos pelo autor; não autenticam a origem física nem comprovam desempenho preditivo.'
(args.output/'audit.json').write_text(json.dumps(stats,indent=2,ensure_ascii=False))
# Uma linha por dia para o gráfico, com contagem para não confundir média parcial com dia completo.
daily=collections.defaultdict(list)
for t,v in lookup.items():daily[t.date()].append((t,v))
with (args.output/'serie-diaria.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['date_utc','pm25_mean_ug_m3','pm25_min_ug_m3','pm25_max_ug_m3','observed_hours','grid_hours','missing_hours','temperature_mean_degC','humidity_mean_pct','wind_speed_mean_m_s'])
 for day,items in daily.items():
  vs=[v for t,v in items if v is not None];met=[wl[t] for t,v in items if t in wl];mean=lambda seq: round(sum(seq)/len(seq),4) if seq else ''
  w.writerow([day.isoformat(),mean(vs),min(vs) if vs else '',max(vs) if vs else '',len(vs),len(items),len(items)-len(vs),mean([v[0] for v in met]),mean([v[1] for v in met]),mean([v[3] for v in met])])
monthly=collections.defaultdict(list)
for t,v in lookup.items():monthly[t.strftime('%Y-%m')].append((t,v))
with (args.output/'cobertura-mensal.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['month_utc','observed_hours','grid_hours','missing_hours','pm25_mean_ug_m3'])
 for month,items in monthly.items():
  vs=[v for t,v in items if v is not None];w.writerow([month,len(vs),len(items),len(items)-len(vs),round(sum(vs)/len(vs),4) if vs else ''])
(args.output/'lacunas.json').write_text(json.dumps([{'start_utc':g['first'].isoformat(),'end_utc':g['last'].isoformat(),'hours':g['hours']} for g in gaps],indent=2))
print(json.dumps({k:v for k,v in stats.items() if k!='files'},ensure_ascii=False,indent=2))

origin=dt.datetime(2020,12,2,12,tzinfo=dt.timezone.utc)
with (args.output/'exemplo-horario.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=pm[0].keys());w.writeheader();w.writerows(r for r in pm if origin-dt.timedelta(hours=24)<=parse(r['timestamp_utc'])<=origin+dt.timedelta(hours=8))
