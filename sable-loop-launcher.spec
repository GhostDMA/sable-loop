from pathlib import Path
from PyInstaller.utils.hooks import collect_all

src = Path(SPECPATH) / 'src'
orig = Path(r'D:\heylisten-v043-stage\v181-final-caption-01\src')
dist = orig / 'dist-release'
import sysconfig
packages = Path(sysconfig.get_path('purelib'))
datas, binaries, hidden = collect_all('curl_cffi')
datas += [(str(src / 'Get-HeyListen.py'), '.'), (str(Path(SPECPATH) / 'assets/keyart-bg.png'), 'assets')]
binaries += [(str(dist / 'SDL2-2.30.10/SDL2-2.30.10/lib/x64/SDL2.dll'), '.'),
             (str(packages / 'sdl2dll/dll/SDL2_ttf.dll'), '.'),
             (str(packages / 'sdl2dll/dll/SDL2_image.dll'), '.')]
a = Analysis([str(src / 'Get-HeyListen.py')], pathex=list(map(str, [src, dist / 'flags', orig])),
             datas=datas, binaries=binaries, hiddenimports=hidden + ['launcher', 'install_scan_windows', 'game_channel', 'build_flags'])
exe = EXE(PYZ(a.pure), a.scripts, a.binaries, a.datas, [], name='sable-loop-launcher',
          console=False, icon=str(Path(SPECPATH) / 'assets/sable-loop.ico'))
