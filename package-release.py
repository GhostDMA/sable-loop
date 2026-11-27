"""Package the built launcher for self-update without publishing anything."""
import argparse
import hashlib
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parent
EXE = 'sable-loop-launcher.exe'


def version(file):
    match = re.search(r'''^APP_VERSION = (["'])(\d+\.\d+\.\d+)\1\s*$''',
                      (ROOT / 'src' / file).read_text(encoding='utf-8'), re.MULTILINE)
    if not match:
        raise ValueError(f'Cannot read APP_VERSION in src/{file}')
    return match[2]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('exe', type=Path, nargs='?', default=ROOT / 'dist' / EXE)
    parser.add_argument('--out', type=Path, default=ROOT / 'dist')
    args = parser.parse_args()
    if not args.exe.is_file():
        parser.error(f'Launcher executable not found: {args.exe}')
    try:
        gui, cli = version('launcher.py'), version('Get-HeyListen.py')
    except ValueError as error:
        parser.error(str(error))
    if gui != cli:
        parser.error(f'APP_VERSION mismatch: launcher.py={gui}, Get-HeyListen.py={cli}')
    args.out.mkdir(parents=True, exist_ok=True)
    archive = args.out / 'sable-loop.zip'
    with zipfile.ZipFile(archive, 'w') as z:
        z.write(args.exe, EXE)
    with archive.open('rb') as f:
        digest = hashlib.file_digest(f, 'sha256').hexdigest()
    (args.out / 'SHA256SUMS.txt').write_bytes(f'{digest}  {archive.name}\r\n'.encode('ascii'))


if __name__ == '__main__':
    main()
