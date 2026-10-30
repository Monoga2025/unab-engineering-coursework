"""Render the requested Blender clips sequentially, with logs and safe resume."""
from __future__ import annotations

import argparse
import datetime
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time

from verify_deliverables import CLIPS

ROOT = Path(__file__).resolve().parent
DEFAULT_BLENDER = Path(r"C:\Program Files\Blender Foundation\Blender 4.2\blender.exe")
STATUS = ROOT / 'verificacion' / 'render_status.json'


def timestamp():
    return datetime.datetime.now().astimezone().isoformat(timespec='seconds')


def write_status(data):
    temporary = STATUS.with_suffix('.tmp')
    temporary.write_text(json.dumps(data, indent=2), encoding='utf-8')
    temporary.replace(STATUS)


def valid_existing(path, duration):
    if not path.is_file() or not shutil.which('ffprobe'):
        return False
    result = subprocess.run([
        'ffprobe', '-v', 'error', '-select_streams', 'v:0',
        '-show_entries', 'stream=width,height,nb_frames,r_frame_rate,duration',
        '-of', 'json', str(path),
    ], capture_output=True, text=True)
    try:
        stream = json.loads(result.stdout)['streams'][0]
        return (stream['width'], stream['height'], stream['r_frame_rate'],
                int(stream['nb_frames'])) == (1920, 1080, '30/1', duration * 30)
    except (ValueError, KeyError, IndexError):
        return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--blender', type=Path, default=DEFAULT_BLENDER)
    parser.add_argument('--samples', type=int, default=32)
    parser.add_argument('--start', type=int, default=1)
    parser.add_argument('--end', type=int, default=10)
    parser.add_argument('--resume', action='store_true')
    parser.add_argument('--stills', action='store_true')
    args = parser.parse_args()
    if not args.blender.is_file():
        parser.error(f'Blender executable not found: {args.blender}')
    if not 1 <= args.start <= args.end <= 10:
        parser.error('Expected 1 <= start <= end <= 10')
    for folder in ('logs', 'renders', 'verificacion'):
        (ROOT / folder).mkdir(exist_ok=True)
    status = {'state': 'running', 'started_at': timestamp(), 'samples': args.samples,
              'resolution': '1920x1080', 'fps': 30, 'completed': [], 'skipped': []}
    write_status(status)
    base = [str(args.blender), '--background', '--factory-startup', '--python-exit-code', '1',
            '--python', str(ROOT / 'geneva_conveyor_generator.py'), '--',
            '--samples', str(args.samples), '--percentage', '100']
    jobs = [(index, name, seconds) for index, (name, seconds) in enumerate(CLIPS.items(), 1)
            if args.start <= index <= args.end]
    if args.stills:
        jobs.append((0, 'PNG_CAPTURES', 0))
    for number, name, seconds in jobs:
        if number and args.resume and valid_existing(ROOT / 'renders' / name, seconds):
            print(f'SKIP verified existing: {name}', flush=True)
            status['skipped'].append(name)
            write_status(status)
            continue
        status.update(current=name, current_started_at=timestamp())
        write_status(status)
        started = time.monotonic()
        command = base + (['--mode', 'clip', '--clip', str(number)] if number else ['--mode', 'stills'])
        log_path = ROOT / 'logs' / (Path(name).stem + '.log')
        print(f'RENDER {name}; log: {log_path.name}', flush=True)
        with log_path.open('w', encoding='utf-8') as log:
            result = subprocess.run(command, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT)
        elapsed = round(time.monotonic() - started, 2)
        if result.returncode or (number and not valid_existing(ROOT / 'renders' / name, seconds)):
            status.update(state='failed', failed=name, elapsed_seconds=elapsed,
                          exit_code=result.returncode, log=str(log_path.relative_to(ROOT)))
            write_status(status)
            raise RuntimeError(f'{name} failed; inspect {log_path}')
        status['completed'].append({'file': name, 'render_seconds': elapsed})
        write_status(status)
        print(f'COMPLETE {name}: {elapsed:.1f}s', flush=True)
    status.update(state='completed', finished_at=timestamp(), current=None)
    write_status(status)
    print('Requested render queue completed. Run verify_deliverables.py --decode.', flush=True)


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
