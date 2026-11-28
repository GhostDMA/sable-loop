from pathlib import Path
from runpy import run_path
from PyInstaller.utils.hooks import collect_all
from PyInstaller.utils.win32.versioninfo import (FixedFileInfo, StringFileInfo, StringStruct,
    StringTable, VarFileInfo, VarStruct, VSVersionInfo)

src = Path(SPECPATH) / 'src'
read_version = run_path(str(src.parent / 'package-release.py'))['version']
version = read_version('launcher.py')
if version != read_version('Get-HeyListen.py'):
    raise ValueError('APP_VERSION mismatch between GUI and CLI')
file_version = version + '.0'
parts = tuple(map(int, file_version.split('.')))
fields = {'FileDescription': 'Star Wars: Galactic Racer', 'ProductName': 'Star Wars: Galactic Racer',
          'FileVersion': file_version, 'ProductVersion': file_version, 'InternalName': 'sable-loop-launcher',
          'OriginalFilename': 'sable-loop-launcher.exe', 'CompanyName': '', 'LegalCopyright': ''}
resource = VSVersionInfo(ffi=FixedFileInfo(filevers=parts, prodvers=parts, fileType=1), kids=[
    StringFileInfo([StringTable('040904B0', [StringStruct(k, v) for k, v in fields.items()])]),
    VarFileInfo([VarStruct('Translation', [1033, 1200])])])
version_file = Path(workpath) / 'launcher-version.txt'
version_file.write_text(str(resource), encoding='utf-8')
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
          console=False, icon=str(Path(SPECPATH) / 'assets/sable-loop.ico'), version=str(version_file))
