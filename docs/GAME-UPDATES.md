# Publish a game mod

From the repo root, add the mod to the complete unpacked game tree, then pack it into a separate folder. For example, with revision 3 live:

```powershell
python -X utf8 src\pack-game.py --source ..\staging\install-tree --out ..\staging\release-assets-r4
python -X utf8 publish-game-revision.py ..\staging\release-assets-r4 4
```

Use the next `game-channel/channel.json` revision. You need GitHub CLI (`gh`) signed into an account with write access. The publisher retains unchanged payload names, uploads changed payloads to `v1.0.0`, checks every referenced payload's server-side size and SHA-256, then uploads and checks the manifest before advancing the channel. Do not remove old release assets: other revisions still reference them. After an interrupted run, retry the same unchanged pack; matching immutable uploads are reused, conflicting uploads are never overwritten.

Installed launchers check the channel when opened. From the ready main screen a changed manifest starts a game update automatically; **Update** is also available manually. Fresh installations use the same manifest.
