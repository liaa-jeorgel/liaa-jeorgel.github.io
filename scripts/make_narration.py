"""Gera a narração e os tempos reais de cada frase.

A síntese é local (macOS `say`). Os tempos servem para alinhar as legendas com a
fala efectiva, ignorando os silêncios no início e no fim de cada frase.
"""
import json, re, shutil, subprocess, wave
from pathlib import Path

import imageio_ffmpeg

ROOT = Path.cwd()
WORK = Path('/tmp/pm25-video')
ROTEIRO = ROOT / 'assets/video/roteiro.json'
RATE = 156          # ligeiramente mais lento que a versão anterior
GAP = 0.28          # pausa curta entre frases da mesma cena
TAIL = 0.70         # respiro no fim de cada cena
SAMPLE_RATE = 22050

if WORK.exists():
    shutil.rmtree(WORK)
WORK.mkdir(parents=True)
ff = imageio_ffmpeg.get_ffmpeg_exe()
scenes = json.loads(ROTEIRO.read_text(encoding='utf-8'))


def duration_of(path):
    with wave.open(str(path), 'rb') as wav:
        return wav.getnframes() / wav.getframerate()


def silence(path, seconds):
    subprocess.run([
        ff, '-y', '-v', 'error', '-f', 'lavfi',
        '-i', f'anullsrc=r={SAMPLE_RATE}:cl=mono',
        '-t', f'{seconds:.3f}', '-c:a', 'pcm_s16le', str(path)
    ], check=True)


def voiced_span(path):
    """Devolve (início, duração) da parte não silenciosa do ficheiro."""
    full = duration_of(path)
    proc = subprocess.run([
        ff, '-hide_banner', '-nostats', '-i', str(path),
        '-af', 'silencedetect=noise=-45dB:d=0.18', '-f', 'null', '-'
    ], text=True, capture_output=True)
    intervals = []
    starts = re.findall(r'silence_start: ([\d.]+)', proc.stderr)
    ends = re.findall(r'silence_end: ([\d.]+)', proc.stderr)
    for start, end in zip(starts, ends):
        intervals.append((float(start), float(end)))
    if not intervals:
        return 0.0, full
    first, last = intervals[0], intervals[-1]
    voice_start = first[1] if first[0] <= 0.08 else 0.0
    voice_end = last[0] if last[1] >= full - 0.08 else full
    return voice_start, max(0.4, voice_end - voice_start)


def make_voice(scene_index, line_index, text):
    aiff = WORK / f'voice-{scene_index}-{line_index}.aiff'
    wav = WORK / f'voice-{scene_index}-{line_index}.wav'
    subprocess.run(['say', '-v', 'Joana', '-r', str(RATE), '-o', str(aiff), text], check=True)
    subprocess.run([
        ff, '-y', '-v', 'error', '-i', str(aiff),
        '-ar', str(SAMPLE_RATE), '-ac', '1', '-c:a', 'pcm_s16le', str(wav)
    ], check=True)
    aiff.unlink()
    return wav


gap_wav = WORK / 'gap.wav'
tail_wav = WORK / 'tail.wav'
silence(gap_wav, GAP)
silence(tail_wav, TAIL)

for i, scene in enumerate(scenes):
    timings = []
    cursor = 0.0
    concat = []
    for j, line in enumerate(scene['lines']):
        voice = make_voice(i, j, line)
        length = duration_of(voice)
        start, voiced = voiced_span(voice)
        timings.append({
            'start': round(cursor, 6),
            'duration': round(length, 6),
            'voiced_start': round(start, 6),
            'voiced_duration': round(voiced, 6),
            'words': len(line.split())
        })
        concat.append(voice)
        cursor += length
        if j < len(scene['lines']) - 1:
            concat.append(gap_wav)
            cursor += GAP
    concat.append(tail_wav)
    cursor += TAIL

    list_file = WORK / f'audio-{i}.txt'
    list_file.write_text(''.join(f"file '{p}'\n" for p in concat), encoding='utf-8')
    audio = WORK / f'scene-{i}.wav'
    subprocess.run([
        ff, '-y', '-v', 'error', '-f', 'concat', '-safe', '0',
        '-i', str(list_file), '-c:a', 'pcm_s16le', str(audio)
    ], check=True)

    scene['audio'] = str(audio)
    scene['duration'] = round(cursor, 6)
    scene['timings'] = timings

meta = {
    'rate': RATE,
    'gap': GAP,
    'tail': TAIL,
    'voice': 'Joana — macOS, síntese de voz',
    'scenes': scenes
}
(WORK / 'scenes.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
print('Narração:', round(sum(s['duration'] for s in scenes), 2), 'segundos', flush=True)
