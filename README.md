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
