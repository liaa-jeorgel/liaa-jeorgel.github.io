"""Renderiza o vídeo educativo a partir do roteiro e da narração locais.

Sem dados remotos: o gráfico e o exemplo horário vêm dos derivados em
`assets/data/`. As transições são curtas e o movimento é muito ligeiro.
"""
import csv, datetime as dt, json, math, re, subprocess, textwrap
from pathlib import Path

import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

ROOT = Path.cwd()
WORK = Path('/tmp/pm25-video')
OUT = ROOT / 'assets/video'
ff = imageio_ffmpeg.get_ffmpeg_exe()
meta = json.loads((WORK / 'scenes.json').read_text(encoding='utf-8'))
scenes = meta['scenes']
W, H, FPS = 1280, 720, 24
XFADE = 0.65
FONT_DIR = Path('/System/Library/Fonts/Supplemental/')

INK = '#eef1e7'
MUTED = '#b4bfae'
ORANGE = '#ff934b'
BG = '#171d19'
PANEL = '#202a22'
PANEL_2 = '#2a352c'
LINE = '#3b473c'

daily = list(csv.DictReader(open(ROOT / 'assets/data/serie-diaria.csv', encoding='utf-8')))
hourly = list(csv.DictReader(open(ROOT / 'assets/data/exemplo-horario.csv', encoding='utf-8')))


def font(size, bold=False, serif=False):
    if serif:
        name = 'Georgia Bold.ttf' if bold else 'Georgia.ttf'
    else:
        name = 'Arial Bold.ttf' if bold else 'Arial.ttf'
    return ImageFont.truetype(str(FONT_DIR / name), size)


def tw(d, text, f):
    box = d.textbbox((0, 0), text, font=f)
    return box[2] - box[0]


def text(d, xy, value, size=24, fill=INK, bold=False, serif=False):
    d.text(xy, value, font=font(size, bold, serif), fill=fill)


def wrap(d, value, f, max_width):
    words = value.split()
    lines, current = [], ''
    for word in words:
        candidate = f'{current} {word}'.strip()
        if current and tw(d, candidate, f) > max_width:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def base(d, scene, index, total):
    d.rectangle((0, 0, W, H), fill=BG)
    for x in range(0, W, 80):
        d.line((x, 0, x, H), fill='#1c251e', width=1)
    for y in range(0, H, 80):
        d.line((0, y, W, y), fill='#1c251e', width=1)
    d.rectangle((0, 0, W, 6), fill=ORANGE)
    text(d, (64, 32), 'PM2.5 / LUANDA', 20, ORANGE, True)
    text(d, (930, 34), 'JEORGEL CHITENDE · UNIPAMPA', 16, MUTED)
    text(d, (64, 76), scene['kicker'], 17, ORANGE, True)
    title_font = font(46, True, True)
    title_lines = wrap(d, scene['title'], title_font, 1120)
    for n, line in enumerate(title_lines):
        text(d, (64, 106 + n * 54), line, 46, INK, True, True)
    top = 106 + len(title_lines) * 54 + 26
    d.line((64, 676, 1216, 676), fill=LINE, width=1)
    text(d, (64, 688), 'Narração sintética · dados conferidos em 24/11/2026', 16, MUTED)
    number = f'{index + 1} / {total}'
    text(d, (1190 - tw(d, number, font(16)), 688), number, 16, MUTED)
    return top


def card(d, box, fill=PANEL, outline=LINE, radius=16):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=2)


def draw_city(d, top):
    palette = ['#253129', '#2c3a2e']
    skyline = [(100, 100, 95), (215, 160, 80), (320, 125, 100), (445, 210, 85),
               (550, 155, 90), (670, 110, 105), (805, 180, 85), (910, 135, 100), (1040, 85, 100)]
    for n, (x, h, w) in enumerate(skyline):
        d.rounded_rectangle((x, 545 - h, x + w, 545), radius=3,
                            fill=palette[n % 2], outline='#60705e', width=2)
        for xx in range(x + 15, x + w - 10, 22):
            for yy in range(545 - h + 20, 525, 28):
                d.rectangle((xx, yy, xx + 6, yy + 9), fill='#60705e')
    for n in range(26):
        x = 90 + (n * 103) % 1100
        y = top + 30 + (n * 47) % 150
        r = 2 + n % 4
        d.ellipse((x - r, y - r, x + r, y + r), fill=ORANGE)
    d.line((64, 546, 1216, 546), fill=ORANGE, width=3)
    text(d, (70, 574), '1 h  ·  3 h  ·  6 h', 42, ORANGE, True)
    text(d, (70, 632), 'Ilustração esquemática · sem atribuir causas aos dados', 18, MUTED)


def quad_points(a, b, bend=50, steps=36):
    x1, y1 = a
    x2, y2 = b
    dx, dy = x2 - x1, y2 - y1
    dist = max(1, math.hypot(dx, dy))
    cx = (x1 + x2) / 2 - dy / dist * bend
    cy = (y1 + y2) / 2 + dx / dist * bend
    out = []
    for n in range(steps + 1):
        t = n / steps
        x = (1 - t) ** 2 * x1 + 2 * (1 - t) * t * cx + t ** 2 * x2
        y = (1 - t) ** 2 * y1 + 2 * (1 - t) * t * cy + t ** 2 * y2
        out.append((round(x), round(y)))
    return out


def draw_world(d, top):
    cx, cy, rx, ry = 640, 425, 335, 205
    d.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill='#1b251e', outline=LINE, width=2)
    for factor in (0.38, 0.72):
        d.ellipse((cx - rx * factor, cy - ry, cx + rx * factor, cy + ry), outline=LINE, width=1)
    for offset in (-0.55, -0.2, 0.2, 0.55):
        y = cy + offset * ry
        half = rx * math.sqrt(max(0.05, 1 - offset ** 2))
        d.line((cx - half, y, cx + half, y), fill=LINE, width=1)
    points = {
        'América': (0.29, 0.40),
        'Europa': (0.50, 0.31),
        'África': (0.53, 0.55),
        'Ásia': (0.73, 0.38),
        'Oceânia': (0.86, 0.72),
    }
    absolute = {k: (cx + (u - 0.5) * 2 * rx, cy + (v - 0.5) * 2 * ry) for k, (u, v) in points.items()}
    for a, b in [('América', 'Europa'), ('América', 'África'), ('Europa', 'Ásia'),
                 ('África', 'Ásia'), ('Ásia', 'Oceânia')]:
        d.line(quad_points(absolute[a], absolute[b]), fill=ORANGE, width=2)
    for name, (x, y) in absolute.items():
        r = 5 if name != 'África' else 8
        d.ellipse((x - r, y - r, x + r, y + r), fill=ORANGE if name == 'África' else MUTED)
    lx, ly = absolute['África']
    d.ellipse((lx - 15, ly - 15, lx + 15, ly + 15), outline=ORANGE, width=3)
    text(d, (lx + 20, ly - 12), 'Luanda', 20, ORANGE, True)
    text(d, (70, top + 20), 'OMS V8.0 · sem registos para Angola', 22, INK, True)
    text(d, (70, top + 62), 'Pontos esquemáticos · sem ranking nem comparação entre países', 19, MUTED)


def draw_sources(d, top):
    panels = [
        (70, 'PM 2,5', ['Concentração horária', 'Unidade: µg/m³', 'Lacunas preservadas']),
        (670, 'METEOROLOGIA', ['Temperatura · humidade · pressão', 'Velocidade e direcção do vento', 'Alinhamento horário em UTC']),
    ]
    for x, heading, items in panels:
        card(d, (x, top + 10, x + 535, 560))
        text(d, (x + 28, top + 38), heading, 32, ORANGE, True)
        d.line((x + 28, top + 88, x + 507, top + 88), fill=LINE, width=1)
        for n, item in enumerate(items):
            text(d, (x + 28, top + 112 + n * 58), item, 24, INK)
    text(d, (70, 600), 'Origem declarada: OpenWeather · conferência dos CSV fornecidos', 21, MUTED)


def chart_base(d, top, hi, x0=90, x1=1190, y0=None, y1=548):
    y0 = top + 30 if y0 is None else y0
    for n in range(5):
        y = y1 - n * (y1 - y0) / 4
        d.line((x0, y, x1, y), fill=LINE, width=1)
        label = str(round(hi * n / 4))
        text(d, (x0 - 52, y - 10), label, 15, MUTED)
    text(d, (x0, y0 - 34), 'PM2.5 · µg/m³', 17, MUTED)
    return x0, x1, y0, y1


def draw_series(d, top):
    values = []
    for row in daily:
        raw = row['pm25_mean_ug_m3']
        values.append(float(raw) if raw else None)
    hi = math.ceil(max(v for v in values if v is not None) / 50) * 50
    x0, x1, y0, y1 = chart_base(d, top, hi)
    step = (x1 - x0) / max(1, len(values) - 1)
    points = []
    for n, value in enumerate(values):
        x = x0 + n * step
        if value is None:
            if len(points) > 1:
                d.line(points, fill=ORANGE, width=3)
            points = []
        else:
            points.append((round(x), round(y1 - value / hi * (y1 - y0))))
    if len(points) > 1:
        d.line(points, fill=ORANGE, width=3)
    text(d, (90, 566), '12/2020', 18, MUTED)
    text(d, (1080, 566), '09/2026', 18, MUTED)
    card(d, (70, 596, 560, 654), fill=PANEL_2)
    text(d, (92, 610), '98,02% de cobertura', 28, ORANGE, True)
    text(d, (610, 608), 'Médias diárias · sem suavização nem interpolação', 21, MUTED)


def draw_gaps(d, top):
    text(d, (80, top + 12), '120 h', 92, ORANGE, True)
    text(d, (80, top + 120), 'maior ausência', 28, INK)
    x0, x1, y = 620, 1180, top + 80
    d.line((x0, y, x1, y), fill=LINE, width=5)
    d.line((x0 + 170, y, x1 - 130, y), fill=ORANGE, width=7)
    for x in (x0 + 170, x1 - 130):
        d.ellipse((x - 9, y - 9, x + 9, y + 9), fill=ORANGE)
    text(d, (660, top + 18), 'SEM OBSERVAÇÃO', 24, ORANGE, True)
    text(d, (680, top + 122), '121 h entre observações', 22, MUTED)
    card(d, (70, 540, 1210, 640), fill=PANEL_2)
    text(d, (96, 560), '1.008 horas ausentes · 30 episódios', 32, INK, True)
    text(d, (96, 606), 'A ausência não é zero: nenhuma concentração foi inventada.', 20, MUTED)


def draw_pipeline(d, top):
    names = ['IMPORTAR', 'DIAGNOSTICAR', 'ALINHAR', 'CONSTRUIR']
    subs = ['Duas fontes', 'Qualidade e cobertura', 'Grade horária UTC', '39 atributos']
    card(d, (65, top, 1215, 560))
    text(d, (85, top + 16), 'UMA APLICAÇÃO DE PREPARAÇÃO', 17, MUTED, True)
    for n, name in enumerate(names):
        x = 90 + n * 280
        card(d, (x, top + 74, x + 245, top + 220), fill=PANEL_2)
        text(d, (x + 16, top + 94), f'0{n + 1}', 16, ORANGE, True)
        text(d, (x + 16, top + 122), name, 22, INK, True)
        text(d, (x + 16, top + 172), subs[n], 18, MUTED)
        if n < 3:
            text(d, (x + 252, top + 142), '→', 26, ORANGE, True)
    text(d, (75, 600), 'Entradas · operações · saídas · verificações. Sem treino ou avaliação.', 22, MUTED)


def draw_horizons(d, top):
    origin = dt.datetime(2020, 12, 2, 12, tzinfo=dt.timezone.utc)
    start = origin - dt.timedelta(hours=24)
    end = origin + dt.timedelta(hours=8)
    rows = [r for r in hourly if start <= dt.datetime.fromisoformat(r['timestamp_utc']) <= end]
    x = lambda t: 90 + (t - start).total_seconds() / (end - start).total_seconds() * 1100
    y = lambda v: 520 - v / 100 * 250
    d.rectangle((round(x(origin)), top + 20, 1190, 520), fill='#38281b')
    points = [(round(x(dt.datetime.fromisoformat(r['timestamp_utc']))), round(y(float(r['pm2_5'])))) for r in rows]
    d.line(points, fill=ORANGE, width=3)
    d.line((round(x(origin)), top + 20, round(x(origin)), 532), fill=INK, width=2)
    text(d, (round(x(origin)) + 10, top + 26), 'origem', 18, INK, True)
    for h in (1, 3, 6):
        t = origin + dt.timedelta(hours=h)
        row = next(r for r in rows if dt.datetime.fromisoformat(r['timestamp_utc']) == t)
        px, py = round(x(t)), round(y(float(row['pm2_5'])))
        d.ellipse((px - 7, py - 7, px + 7, py + 7), fill=ORANGE)
        text(d, (px - 22, top + 70 + h * 14), f'+{h} h', 21, ORANGE, True)
    text(d, (90, 548), 'Histórico anterior a t', 24, INK)
    text(d, (850, 548), 'Alvos observados', 23, ORANGE, True)
    text(d, (90, 600), 'Origem real: 02/12/2020 · 12h UTC · não são previsões', 21, MUTED)


def draw_samples(d, top):
    for n, (h, count) in enumerate(((1, '49.124'), (3, '49.068'), (6, '48.984'))):
        x = 70 + n * 405
        card(d, (x, top + 20, x + 370, 540))
        text(d, (x + 25, top + 48), f'{h} HORA' + ('S' if h > 1 else ''), 23, ORANGE, True)
        text(d, (x + 25, top + 110), count, 58, INK, True, True)
        text(d, (x + 25, top + 210), 'amostras mantidas', 22, MUTED)
    text(d, (80, 590), 'Conjuntos independentes · não somar as contagens', 24, MUTED, True)


def draw_future(d, top):
    items = [
        '1. Executar a persistência',
        '2. Treinar e validar Random Forest e LSTM',
        '3. Comparar MAE e RMSE por horizonte',
    ]
    for n, item in enumerate(items):
        text(d, (80, top + 16 + n * 76), item, 31, INK, True)
    card(d, (70, 530, 1210, 640), fill='#38281b', outline=ORANGE)
    text(d, (95, 554), 'Ainda não existem resultados preditivos.', 34, ORANGE, True)
    text(d, (95, 604), 'A comparação futura deve respeitar a ordem temporal.', 20, MUTED)


RENDERERS = {
    'city': draw_city,
    'world': draw_world,
    'sources': draw_sources,
    'series': draw_series,
    'gaps': draw_gaps,
    'pipeline': draw_pipeline,
    'horizons': draw_horizons,
    'samples': draw_samples,
    'future': draw_future,
}

for i, scene in enumerate(scenes):
    img = Image.new('RGB', (W, H), BG)
    draw = ImageDraw.Draw(img)
    top = base(draw, scene, i, len(scenes))
    RENDERERS[scene['kind']](draw, top)
    img.save(WORK / f'scene-{i}.png')
    if i == 0:
        img.save(OUT / 'capa.jpg', quality=90, subsampling=0)

# Vídeo: um único filtro com zoom muito ligeiro e crossfades curtos.
cmd = [ff, '-y', '-v', 'error']
for i, scene in enumerate(scenes):
    cmd += ['-loop', '1', '-framerate', str(FPS), '-t', f"{scene['duration']:.3f}",
            '-i', str(WORK / f'scene-{i}.png')]
    cmd += ['-i', scene['audio']]

filters = []
for i, scene in enumerate(scenes):
    duration = f"{scene['duration']:.3f}"
    zoom = (f"scale=1280:720,trim=duration={duration},"
            "setpts=PTS-STARTPTS,fps=24,format=yuv420p")
    if i == 0:
        zoom += ',fade=t=in:st=0:d=0.4'
    if i == len(scenes) - 1:
        zoom += f',fade=t=out:st={scene["duration"] - 0.4:.3f}:d=0.4'
    filters.append(f'[{2 * i}:v]{zoom}[v{i}]')
    audio = f'[{2 * i + 1}:a]aresample=48000,asetpts=PTS-STARTPTS'
    if i == 0:
        audio += ',afade=t=in:st=0:d=0.25'
    if i == len(scenes) - 1:
        audio += f',afade=t=out:st={scene["duration"] - 0.35:.3f}:d=0.35'
    filters.append(f'{audio}[a{i}]')

current_v, current_a = 'v0', 'a0'
elapsed = scenes[0]['duration']
for i in range(1, len(scenes)):
    offset = elapsed - XFADE
    filters.append(f'[{current_v}][v{i}]xfade=transition=fade:duration={XFADE:.2f}:'
                   f'offset={offset:.3f}[vx{i}]')
    filters.append(f'[{current_a}][a{i}]acrossfade=d={XFADE:.2f}:c1=tri:c2=tri[ax{i}]')
    current_v, current_a = f'vx{i}', f'ax{i}'
    elapsed += scenes[i]['duration'] - XFADE

cmd += [
    '-filter_complex', ';'.join(filters),
    '-map', f'[{current_v}]', '-map', f'[{current_a}]',
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '26', '-tune', 'stillimage',
    '-profile:v', 'high', '-level:v', '4.0', '-g', '48', '-keyint_min', '24',
    '-sc_threshold', '0', '-pix_fmt', 'yuv420p',
    '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709',
    '-c:a', 'aac', '-b:a', '80k', '-ar', '48000',
    '-movflags', '+faststart',
    '-metadata', 'title=PM2.5 em Luanda — vídeo educativo',
    '-metadata', 'author=Jeorgel Chitende',
    str(OUT / 'pm25-luanda.mp4'),
]
subprocess.run(cmd, check=True)


def stamp(value):
    value = max(0.0, value)
    return f'{int(value // 3600):02}:{int(value % 3600 // 60):02}:{value % 60:06.3f}'


def caption_chunks(value, max_words=12, max_chars=52):
    parts = re.split(r'(?<=[;:])\s+', value)
    chunks = []
    for part in parts:
        words = part.split()
        while len(words) > max_words:
            chunk, used = [], 0
            for word in words:
                candidate = ' '.join(chunk + [word])
                if chunk and (len(chunk) >= max_words or len(candidate) > max_chars):
                    break
                chunk.append(word)
                used += 1
            chunks.append(' '.join(chunk))
            words = words[used:]
        if words:
            chunks.append(' '.join(words))
    merged = []
    for chunk in chunks:
        if merged and len(merged[-1]) + len(chunk) + 1 <= 40:
            merged[-1] += ' ' + chunk
        else:
            merged.append(chunk)
    return merged


vtt = ['WEBVTT\n']
scene_starts = []
cursor = 0.0
for i, scene in enumerate(scenes):
    scene_starts.append(cursor)
    cursor += scene['duration'] - (XFADE if i else 0)

for i, scene in enumerate(scenes):
    for line, timing in zip(scene['lines'], scene['timings']):
        chunks = caption_chunks(line)
        total_words = sum(len(chunk.split()) for chunk in chunks)
        voiced_begin = scene_starts[i] + timing['start'] + timing['voiced_start']
        voiced_length = timing['voiced_duration']
        used = 0
        for chunk in chunks:
            count = len(chunk.split())
            start = voiced_begin + voiced_length * used / total_words
            end = voiced_begin + voiced_length * (used + count) / total_words
            end = max(start + 0.9, end)
            vtt.append(f'{stamp(start)} --> {stamp(end)}\n'
                       + textwrap.fill(chunk, 52) + '\n')
            used += count

(OUT / 'pm25-luanda.vtt').write_text('\n'.join(vtt), encoding='utf-8')
(OUT / 'transcricao.txt').write_text(
    'PM2.5 em Luanda — vídeo educativo\n'
    'Narração sintética portuguesa; não imita o autor.\n\n'
    + '\n\n'.join(s['title'] + '\n' + ' '.join(s['lines']) for s in scenes) + '\n',
    encoding='utf-8')
production = {
    'duration_seconds': round(elapsed, 3),
    'voice': meta['voice'],
    'speech_rate_wpm': meta['rate'],
    'pause_between_lines_seconds': meta['gap'],
    'crossfade_seconds': XFADE,
    'resolution': '1280x720',
    'frame_rate': FPS,
    'captions': {
        'language': 'pt',
        'cues': sum(1 for line in vtt if '-->' in line),
        'alignment': 'repartidas proporcionalmente dentro da fala detetada em cada frase'
    },
    'scenes': [
        {'scene': i + 1, 'start': round(scene_starts[i], 3),
         'duration': round(scene['duration'], 3), 'title': scene['title']}
        for i, scene in enumerate(scenes)
    ],
    'data': 'assets/data/audit.json',
    'nature': 'Apresentação dos dados fornecidos; não é gravação de execução nem previsão.'
}
(OUT / 'producao.json').write_text(json.dumps(production, ensure_ascii=False, indent=2), encoding='utf-8')
print('Vídeo:', round(elapsed, 2), 'segundos', flush=True)
