# Install Star Wars: Galactic Racer on Windows

sable-loop is an unofficial fan distribution. You don't need an account or a store client.

1. **Check your PC.** Use Windows 10 or 11 (64-bit) with 16 GB RAM. Allow about 45 GB of free space on the drive where you want the game. Compare your GPU with the [game's Steam requirements](https://store.steampowered.com/app/4078430/#appSysReq).
2. **Get the launcher.** Download [sable-loop-launcher.exe from the latest release](https://github.com/GhostDMA/sable-loop/releases/latest/download/sable-loop-launcher.exe) and open it. Windows SmartScreen may warn that the executable is unsigned. Only choose **More info → Run anyway** if you trust this repository and downloaded the file from its release.
3. **Pick a game folder.** Choose **Use default folder** for `C:\Games\sable-loop-game` or **Choose another folder** for a different drive or location. Check the path shown, then select **Continue**. You can point the launcher at another install later under **Settings → Change game folder**.
4. **Select Download.** Wait for the download, verification, and installation to finish. If interrupted, reopen the launcher, keep the same install folder, and retry. Leave the downloaded files in place so verified data can be reused.
5. **Select Play** once installation finishes.

## Verify a download or recover from a hash error

Verification is automatic. The release manifest lists the expected SHA-256 hash for each game download. To check a bundle yourself, open PowerShell in the folder containing it and run `Get-FileHash -Algorithm SHA256` followed by its quoted filename. Compare the full hash to the manifest entry for that exact file and release. A match means the bytes agree with the manifest; it does not authenticate an unsigned launcher.

If the launcher reports a hash mismatch, don't run or unpack the failed file. Select **Retry** in the same install folder. If the same file fails again, stop and report the filename and error from **View log**. You can also open `%LOCALAPPDATA%\sable-loop\launcher.log` in File Explorer.

## Update or uninstall

- **Update:** Automatic update checks are on by default. To check manually, open **Settings → Check for updates now**. Use **Update** for game files or **Update now** when prompted for a launcher update.
- **Uninstall:** Close the game. Open **Settings → Apps → Installed apps** (Windows 11) or **Apps & features** (Windows 10), find the game, and select **Uninstall**. The normal uninstall keeps your saves.
