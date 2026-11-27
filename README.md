# sable-loop

sable-loop is a Windows launcher for an unofficial fan distribution of **Star Wars: Galactic Racer**. It downloads the game, checks the files against their SHA-256 hashes, and installs them. No account or store client is required.

**[Download sable-loop-launcher.exe (latest release)](https://github.com/GhostDMA/sable-loop/releases/latest/download/sable-loop-launcher.exe)**

You'll need Windows 10 or 11 (64-bit), 16 GB of RAM, and about 45 GB free on the install drive. Check your GPU against the [game's Steam system requirements](https://store.steampowered.com/app/4078430/#appSysReq).

1. Run the launcher. Use the default folder (`C:\Games\sable-loop-game`) or select **Choose another folder**, then **Continue**.
2. Select **Download**. Leave the launcher open while it downloads, verifies, and installs the game.
3. Select **Play**. To point the launcher at a different install later, use **Settings → Change game folder**.

**Updates:** The launcher checks for updates automatically by default. Use **Settings → Check for updates now** for a manual check. Select **Update** for the game or **Update now** when offered a launcher update.

**Uninstall:** Close the game and uninstall it from Windows Settings → Apps. Saves are kept by default.

### Troubleshooting

- **SmartScreen warning:** The launcher is unsigned. Only if you trust the download from this repository, select **More info → Run anyway**.
- **Interrupted download:** Reopen the launcher and retry in the same game folder so it can reuse verified downloads.
- **Error message:** Select **View log**, or open `%LOCALAPPDATA%\sable-loop\launcher.log`. See the [install guide](docs/INSTALL.md) for hash errors.

### Publishing

- **Launcher (current: `v1.0.1`):** Set `APP_VERSION` in `src/launcher.py` and `src/Get-HeyListen.py` to the same version, higher than the last release. [Build the exe](AGENTS.md#build), run it with `--self-test` and `--help`, then run `python -X utf8 package-release.py`. Create a new matching `vX.Y.Z` release with `sable-loop-launcher.exe`, `sable-loop.zip` and `SHA256SUMS.txt` from `dist/`. Never clobber an exe on an existing release: installed launchers skip equal versions.
- **Game:** Payloads stay on `v1.0.0`. Run `python -X utf8 publish-game-revision.py "<packed folder>" <revision>`; the publisher uploads changed payloads and advances the channel last.

### Publishing files

- `package-release.py` — packages the launcher exe at the root of the zip and writes its checksum.
- [docs/GAME-UPDATES.md](docs/GAME-UPDATES.md) — how to pack and publish the next game revision.
