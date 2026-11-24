"""Vídeo explicativo com animações dos derivados locais e narração sintética.

Requer Pillow e imageio-ffmpeg; executar make_narration.py antes.
Nenhuma animação simula uma execução ou produz previsões.
"""
import csv,datetime as dt,json,math,re,subprocess,textwrap
from pathlib import Path
from functools import lru_cache
from PIL import Image,ImageDraw,ImageFont
import imageio_ffmpeg
ROOT=Path.cwd();WORK=Path('/tmp/pm25-video');OUT=ROOT/'assets/video';OUT.mkdir(exist_ok=True)
meta=json.loads((WORK/'scenes.json').read_text());scenes=meta['scenes'];FF=imageio_ffmpeg.get_ffmpeg_exe()
W,H,FPS=1280,720,24
BG='#131c18';PANEL='#202d25';LINE='#3d5146';INK='#eef3eb';MUTED='#b1c2b7';ORANGE='#ffab67';BLUE='#9cc5d6'
@lru_cache(None)
def font(n,b=False):return ImageFont.truetype('/System/Library/Fonts/Supplemental/'+('Arial Bold.ttf' if b else 'Arial.ttf'),n)
def txt(d,x,y,s,n=26,color=INK,b=False):d.text((x,y),s,font=font(n,b),fill=color)
def card(d,box,accent=False):d.rounded_rectangle(box,radius=18,fill=PANEL,outline=ORANGE if accent else LINE,width=2)
def clamp(x):return min(1,max(0,x))
def step(p,a,b):return clamp((p-a)/(b-a))
def dot(d,x,y,r=6,color=ORANGE):d.ellipse((x-r,y-r,x+r,y+r),fill=color)
def arrow(d,x1,y1,x2,y2,color=ORANGE):
 d.line((x1,y1,x2,y2),fill=color,width=3);angle=math.atan2(y2-y1,x2-x1);d.polygon([(x2,y2),(x2-12*math.cos(angle-.45),y2-12*math.sin(angle-.45)),(x2-12*math.cos(angle+.45),y2-12*math.sin(angle+.45))],fill=color)
def draw_path(d,pts,color=ORANGE,width=3):
 if len(pts)>1:d.line(pts,fill=color,width=width)
 elif pts:dot(d,*pts[0],r=2,color=color)
daily=list(csv.DictReader((ROOT/'assets/data/serie-diaria.csv').open()));hourly=list(csv.DictReader((ROOT/'assets/data/exemplo-horario.csv').open()));gaps=json.loads((ROOT/'assets/data/lacunas.json').read_text());audit=json.loads((ROOT/'assets/data/audit.json').read_text())
origin=dt.datetime(2020,12,2,12,tzinfo=dt.timezone.utc);obs={dt.datetime.fromisoformat(r['timestamp_utc']):float(r['pm2_5']) for r in hourly};largest=max(gaps,key=lambda g:g['hours'])

def frame(scene,index,p):
 im=Image.new('RGB',(W,H),BG);d=ImageDraw.Draw(im)
 d.rectangle((0,0,W,5),fill=ORANGE);txt(d,55,29,'PM2.5 / LUANDA',20,ORANGE,True);txt(d,854,31,'JEORGEL CHITENDE · UNIPAMPA',16,MUTED)
 txt(d,55,77,scene['kicker'],17,ORANGE,True);title_size=42
 while d.textlength(scene['title'],font=font(title_size,True))>1170:title_size-=1
 txt(d,55,113,scene['title'],title_size,INK,True)
 k=scene['kind']
 if k=='city':
  for j,(x,h,w) in enumerate([(75,100,85),(175,160,90),(280,125,80),(375,210,80),(470,145,85),(570,110,80)]):
   d.rectangle((x,465-h,x+w,465),fill=PANEL,outline=LINE,width=2)
   for xx in range(x+15,x+w-10,23):
    for yy in range(465-h+20,445,28):d.rectangle((xx,yy,xx+6,yy+8),fill='#60786b')
  for j in range(18):
   x=90+(j*83+math.sin(p*8+j)*12)%560;y=216+(j*47)%130+math.cos(p*9+j)*7;dot(d,x,y,2+j%3)
  d.line((55,470,670,470),fill=LINE,width=3)
  x=70+(p*450)%520;d.rounded_rectangle((x,475,x+53,492),radius=5,fill='#405b4d');dot(d,x+10,495,4,MUTED);dot(d,x+43,495,4,MUTED)
  card(d,(730,212,1220,502));txt(d,760,240,'PARTÍCULAS FINAS',22,MUTED,True);txt(d,760,285,'≤ 2,5 µm',64,ORANGE,True);txt(d,760,390,'1 h · 3 h · 6 h',38,INK,True);txt(d,55,529,'Luanda esquemática · fontes dos episódios não identificadas',21,MUTED)
 elif k=='world':
  cx,cy,rx,ry=620,355,300,150;d.ellipse((cx-rx,cy-ry,cx+rx,cy+ry),outline=LINE,width=2)
  for f in [.4,.75]:d.ellipse((cx-rx*f,cy-ry,cx+rx*f,cy+ry),outline=LINE,width=1)
  for yy in [cy-60,cy,cy+60]:d.line((cx-rx+40,yy,cx+rx-40,yy),fill=LINE,width=1)
  pts=[(390,310),(585,270),(650,397),(810,300),(840,445)]
  for i in range(4):
   a,b=pts[i],pts[i+1];t=step(p,.04+i*.08,.35+i*.08);d.line((a[0],a[1],a[0]+(b[0]-a[0])*t,a[1]+(b[1]-a[1])*t),fill=ORANGE,width=2)
  for a in pts:dot(d,*a,6)
  d.ellipse((633,380,667,414),outline=ORANGE,width=2);txt(d,677,386,'Luanda',24,ORANGE,True)
  txt(d,55,525,'Pontos e ligações esquemáticos · sem valor para Luanda na OMS V8.0',21,MUTED)
 elif k=='sources':
  for x,title,items in [(55,'PM2.5',['Concentração','µg/m³']),(755,'METEOROLOGIA',['Temperatura · humidade · pressão','Velocidade e direcção do vento'])]:
   card(d,(x,218,x+470,463));txt(d,x+25,244,title,33,ORANGE,True)
   for j,line in enumerate(items):txt(d,x+25,320+j*48,line,22)
  arrow(d,545,345,735,345,BLUE);cx=545+190*((p*2)%1);dot(d,cx,345,7,BLUE);txt(d,555,285,'UTC',32,BLUE,True)
  txt(d,55,515,'Mesma hora ≠ causa comprovada',30,INK,True)
 elif k=='series':
  x0,x1,y0,y1=85,1195,230,473;hi=200
  for v in [0,50,100,150,200]:yy=y1-v/hi*(y1-y0);d.line((x0,yy,x1,yy),fill=LINE);txt(d,33,yy-10,str(v),17,MUTED)
  txt(d,85,197,'Médias diárias · µg/m³',19,MUTED)
  n=max(1,int(len(daily)*step(p,.04,.68)));pts=[]
  for j,r in enumerate(daily[:n]):
   if not r['pm25_mean_ug_m3']:draw_path(d,pts);pts=[]
   else:pts.append((x0+j/(len(daily)-1)*(x1-x0),y1-float(r['pm25_mean_ug_m3'])/hi*(y1-y0)))
  draw_path(d,pts);txt(d,85,482,'12/2020',18,MUTED);txt(d,1100,482,'09/2026',18,MUTED)
  txt(d,85,523,'49.896 observações',30,ORANGE,True);txt(d,675,523,'98,02% cobertura',30,ORANGE,True)
 elif k=='gaps':
  d.line((80,324,1200,324),fill=LINE,width=3)
  # O número de blocos é simbólico; as datas e a duração vêm da lacuna real.
  for j in range(12):
   xx=95+j*96;missing=2<=j<=9;visible=j<=int(step(p,.03,.5)*12)
   if visible:
    d.rounded_rectangle((xx,287,xx+57,361),radius=8,fill=BG if missing else PANEL,outline=BLUE if missing else ORANGE,width=2)
    txt(d,xx+10,306,'—' if missing else '●',27,BLUE if missing else ORANGE)
  txt(d,90,215,'Observado',21,ORANGE,True);txt(d,470,215,'Sem observação',23,BLUE,True);txt(d,1050,215,'Observado',21,ORANGE,True)
  txt(d,105,400,'120 horas ausentes',42,BLUE,True);txt(d,710,413,'121 h entre registos',29,INK,True)
  start=dt.datetime.fromisoformat(largest['start_utc']);end=dt.datetime.fromisoformat(largest['end_utc']);txt(d,90,492,f'Lacuna real: {start:%d/%m/%Y %Hh}–{end:%d/%m/%Y %Hh} UTC',23,MUTED)
  txt(d,90,535,'Blocos ilustrativos, sem escala horária · ausência ≠ zero',21,MUTED)
 elif k=='pipeline':
  steps=['Conferir','Alinhar','Preservar','Exportar'];labels=['Datas e unidades','Grade horária','Valores e lacunas','Ficheiros verificáveis'];active=min(3,int(p*4))
  for j,(name,label) in enumerate(zip(steps,labels)):
   x=55+j*304;card(d,(x,255,x+265,455),j==active);txt(d,x+20,282,f'0{j+1}',20,ORANGE,True);txt(d,x+20,327,name,31,INK,True);txt(d,x+20,388,label,18,MUTED)
   if j<3:arrow(d,x+272,355,x+294,355,ORANGE if j<active else LINE)
  txt(d,55,512,'Animação do método · não é execução da aplicação',26,MUTED)
 elif k=='features':
  card(d,(55,214,1225,504));txt(d,78,225,'PM2.5 · µg/m³',17,MUTED);ty=311;d.line((110,ty,1160,ty),fill=LINE,width=3)
  for j,h in enumerate([24,6,3,1]):
   x=140+j*225;active=j<=int(step(p,.02,.55)*4);dot(d,x,ty,8,ORANGE if active else LINE);txt(d,x-22,260,f't−{h} h',23,ORANGE if active else MUTED,True)
   value=f'{obs[origin-dt.timedelta(hours=h)]:.2f}'.replace('.',',');txt(d,x-24,345,value,30,INK,True)
  d.line((1100,242,1100,415),fill=BLUE,width=3);txt(d,1090,266,'t',30,BLUE,True)
  if p>.45:
   dot(d,702,ty,8);txt(d,678,260,'t−2 h',23,ORANGE,True);txt(d,678,345,f'{obs[origin-dt.timedelta(hours=2)]:.2f}'.replace('.',','),30,INK,True)
   d.line((568,408,845,408),fill=ORANGE,width=3)
   mean=sum(obs[origin-dt.timedelta(hours=j)] for j in [1,2,3])/3
   txt(d,500,435,('Média(t−3, t−2, t−1) = '+f'{mean:.2f}'+' µg/m³').replace('.',','),22,ORANGE)
  txt(d,78,486,'Posições esquemáticas; não representam escala temporal.',17,MUTED)
  txt(d,55,532,'Disponibilidade de 1 h: hipótese retrospectiva, não latência medida',21,MUTED)
 elif k=='horizons':
  start=origin-dt.timedelta(hours=24);end=origin+dt.timedelta(hours=8);x=lambda t:80+(t-start).total_seconds()/(end-start).total_seconds()*1120;y=lambda v:465-v/100*245;xo=x(origin)
  d.rectangle((xo,212,1200,465),fill='#392a1d')
  for v in [0,50,100]:yy=y(v);d.line((80,yy,1200,yy),fill=LINE);txt(d,30,yy-10,str(v),17,MUTED)
  past=[(x(t),y(v)) for t,v in obs.items() if t<=origin];draw_path(d,past);d.line((xo,210,xo,475),fill=BLUE,width=2);txt(d,xo-20,484,'t · 12h',20,BLUE,True)
  if p>.2:draw_path(d,[(x(t),y(v)) for t,v in obs.items() if t>=origin],color='#c9a280',width=2)
  for j,h in enumerate([1,3,6]):
   if p<.25+j*.17:continue
   t=origin+dt.timedelta(hours=h);xx=x(t);yy=y(obs[t]);dot(d,xx,yy,7);txt(d,xx-22,230+j*34,f'+{h}h',22,ORANGE,True)
  txt(d,80,530,'02/12/2020 · alvos observados, não previsões',24,INK,True)
 elif k=='samples':
  for j,(h,n) in enumerate([(1,'49.124'),(3,'49.068'),(6,'48.984')]):
   x=55+j*405;card(d,(x,223,x+365,476),j==min(2,int(p*3)));txt(d,x+24,246,f'{h} HORA'+('S' if h>1 else ''),23,ORANGE,True);txt(d,x+24,302,n,57,INK,True);txt(d,x+24,384,'amostras mantidas',23,MUTED);txt(d,x+24,431,'39 atributos',24,ORANGE)
  txt(d,55,524,'Histórico completo + alvo disponível · contagens não se somam',23,MUTED)
 elif k=='future':
  names=['Persistência','Random Forest','LSTM'];labels=['Referência simples','Árvores de decisão','Rede para sequências']
  for j,(name,label) in enumerate(zip(names,labels)):
   x=55+j*405;card(d,(x,224,x+365,407));txt(d,x+24,255,name,29,INK,True);txt(d,x+24,318,label,22,MUTED);txt(d,x+24,363,'POR EXECUTAR',17,ORANGE,True)
  txt(d,65,448,'Mesmo período de teste · ordem cronológica',29,BLUE,True);txt(d,65,511,'Ainda sem resultados preditivos.',35,ORANGE,True)
 # Área inferior livre para as legendas; sem texto de gráfico sob a fala.
 d.line((55,568,1225,568),fill=LINE,width=1);txt(d,55,690,'Animação explicativa · dados dos CSV · narração sintética',15,MUTED)
 txt(d,1125,690,f'{index+1:02} / {len(scenes):02}',15,MUTED);d.rectangle((0,716,int(W*p),719),fill=ORANGE)
 return im

def stamp(t):return f'{int(t//3600):02}:{int(t%3600//60):02}:{t%60:06.3f}'
def render():
 chapters=[];vtt=['WEBVTT\n'];offset=0;clips=[]
 for i,s in enumerate(scenes):
  duration=s['duration'];count=math.ceil(duration*FPS);clip=WORK/f'animated-{i}.mp4'
  cmd=[FF,'-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','pipe:0','-i',s['audio'],'-t',f'{duration:.6f}','-vf',f'fade=t=in:st=0:d=0.25,fade=t=out:st={duration-.2:.3f}:d=0.2','-c:v','libx264','-preset','fast','-crf','24','-pix_fmt','yuv420p','-c:a','aac','-b:a','96k','-ar','48000','-movflags','+faststart',str(clip)]
  proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
  for n in range(count):proc.stdin.write(frame(s,i,n/max(1,count-1)).tobytes())
  proc.stdin.close();assert proc.wait()==0;clips.append(clip)
  if i==0:frame(s,i,.42).save(OUT/'capa.jpg',quality=90)
  for line,timing in zip(s['lines'],s['timings']):
   # Cues até 10 palavras, ancorados na frase sintetizada. Sem sobreposição.
   words=line.split();chunks=[words[j:j+10] for j in range(0,len(words),10)];begin=offset+timing['start']+timing['voiced_start'];length=timing['voiced_duration'];used=0
   for chunk in chunks:
    a=begin+length*used/len(words);used+=len(chunk);b=begin+length*used/len(words)
    vtt.append(f'{stamp(a)} --> {stamp(b)} line:84% position:50% align:center\n'+textwrap.fill(' '.join(chunk),48)+'\n')
  chapters.append({'scene':i+1,'start':round(offset,3),'duration':round(duration,3),'title':s['title'],'kind':s['kind']});offset+=duration
  print(f'Cena {i+1}/{len(scenes)} · {duration:.1f}s',flush=True)
 (WORK/'animated-clips.txt').write_text(''.join(f"file '{p}'\n" for p in clips))
 video=WORK/'pm25-luanda-final.mp4';subprocess.run([FF,'-y','-v','error','-f','concat','-safe','0','-i',str(WORK/'animated-clips.txt'),'-c','copy','-movflags','+faststart','-metadata','title=PM2.5 em Luanda — explicação visual',str(video)],check=True);video.replace(OUT/'pm25-luanda.mp4')
 (OUT/'pm25-luanda.vtt').write_text('\n'.join(vtt));(OUT/'transcricao.txt').write_text('PM2.5 em Luanda — explicação visual\nNarração sintética portuguesa; não imita o autor.\n\n'+'\n\n'.join(s['title']+'\n'+' '.join(s['lines']) for s in scenes)+'\n')
 cvtt=['WEBVTT\n']
 for i,c in enumerate(chapters):cvtt.append(f"{stamp(c['start'])} --> {stamp(chapters[i+1]['start'] if i+1<len(chapters) else offset)}\n{c['title']}\n")
 (OUT/'capitulos.vtt').write_text('\n'.join(cvtt))
 (OUT/'producao.json').write_text(json.dumps({'duration_seconds':round(offset,3),'voice':meta['voice'],'speech_rate_wpm':meta['rate'],'resolution':'1280x720','frame_rate':FPS,'captions':{'language':'pt','cues':sum('-->' in cue for cue in vtt),'alignment':'proporcional dentro da fala detectada de cada frase; revisão palavra-a-palavra pendente'},'scenes':chapters,'data':'assets/data/audit.json','nature':'Animação do método e dos CSV; não é gravação da aplicação, filmagem local ou resultado preditivo.'},ensure_ascii=False,indent=2));print('TOTAL',round(offset,3),flush=True)

if __name__ == "__main__":
 render()
