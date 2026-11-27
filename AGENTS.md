# sable-loop

Launcher that downloads, verifies and installs STAR WARS Galactic Racer, and keeps
it updated. Public hosting is this repo's GitHub release.

## Layout

- `src/Get-HeyListen.py`: command-line entry point. Downloads, verifies, installs, updates.
- `src/launcher.py`: the window the user sees.
- `src/game_channel.py`: reads `channel.json` on the `game-channel` branch and checks
  the manifest it points to against its SHA-256.
- `src/install_scan_windows.py`: fast file verifier.
- `src/pack-game.py`: packs an installed game folder into payloads of at most 1.5 GiB
  plus `game-manifest.json`.
- `assets/`: icon and background. `sable-loop-launcher.spec`: PyInstaller build.
- `package-release.py`: packages the launcher zip and checksum.
- `publish-game-revision.py`: publishes game updates; see `docs/GAME-UPDATES.md`.
- `docs/INSTALL.md`: install guide.

## Build

```
python -m PyInstaller --distpath dist --workpath "$env:TEMP\opencode\sable-loop-build" sable-loop-launcher.spec
```

The result is one file, `dist\sable-loop-launcher.exe`.

## Test

```
dist\sable-loop-launcher.exe --self-test
dist\sable-loop-launcher.exe --help
dist\sable-loop-launcher.exe --cli --install-game "<folder>" --no-launch --no-self-update --no-pause --plain
```

The last line does a real download of about 42 GB and needs about 49 GB free.
When testing by hand, set `LOCALAPPDATA` to a scratch folder so the real settings
are left alone.

## Publishing

- Launcher (current: `v1.0.1`): set `APP_VERSION` in both `src/launcher.py` and
  `src/Get-HeyListen.py` higher than the last release. Build, run `--self-test`
  and `--help`, then run `python -X utf8 package-release.py`. Create a new matching
  `vX.Y.Z` release with `sable-loop-launcher.exe`, `sable-loop.zip` and `SHA256SUMS.txt`
  from `dist/`. Never clobber an existing launcher: the updater skips equal versions.
- Game payloads stay on `v1.0.0`. Run `python -X utf8 publish-game-revision.py "<packed folder>" <revision>`;
  it advances `game-channel` last. See [GAME-UPDATES.md](docs/GAME-UPDATES.md).

## Conventions

- The code is ported from another launcher. Internal names keep the old spelling
  (`.heylisten-get`, `.heylisten-parts`, `Get-HeyListen.py`). Change them only on purpose.
- Text the user sees names the game. The repo and launcher keep the name `sable-loop`.
- No new dependencies. PowerShell 5.1 has no `&&`. Run Python with `-X utf8`.
