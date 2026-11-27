"""Publish a pack-game.py output to the immutable payload release, pointer last."""
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

REPO = 'GhostDMA/sable-loop'
TAG = 'v1.0.0'
API = f'repos/{REPO}'
CHANNEL = f'{API}/contents/channel.json'


def gh(*args):
    return subprocess.check_output(['gh', *args])


def metadata():
    release = json.loads(gh('api', f'{API}/releases/tags/{TAG}'))
    pages = json.loads(gh('api', '--paginate', '--slurp',
                          f'{API}/releases/{release["id"]}/assets?per_page=100'))
    return {a['name']: a for page in pages for a in page}


def verify(remote, name, size, digest):
    a = remote.get(name, {})
    if (a.get('state'), a.get('size'), a.get('digest')) != ('uploaded', size, 'sha256:' + digest):
        raise ValueError(f'Missing or mismatched release asset: {name}')


def encoded(obj):
    return (json.dumps(obj, ensure_ascii=False, separators=(',', ':')) + '\n').encode()


def upload(path):
    gh('release', 'upload', TAG, '--repo', REPO, str(path))  # Never clobber.


def publish(pack, revision):
    entry = json.loads(gh('api', CHANNEL + '?ref=game-channel'))
    old = json.loads(base64.b64decode(entry['content']))
    if old['version'] != 1 or revision != old['revision'] + 1:
        raise ValueError(f'Expected revision {old["revision"] + 1}')
    previous = gh('release', 'download', TAG, '--repo', REPO, '-p', old['manifest'], '-O', '-')
    if hashlib.sha256(previous).hexdigest() != old['sha256']:
        raise ValueError('Previous manifest does not match channel')
    baseline = {re.sub(r'^r\d+-', '', a['asset']): a for a in json.loads(previous)['assets']}
    manifest = json.loads((pack / 'game-manifest.json').read_bytes())
    manifest['revision'] = revision
    remote = metadata()
    rename = {}
    pending = []
    for asset in manifest['assets']:
        name = asset['asset']
        if name in rename or not re.fullmatch(r'whole-(?:bundle-\d+\.tar|chunk-\d+\.bin)', name):
            raise ValueError(f'Invalid packed asset: {name}')
        prior = baseline.get(name, {})
        if prior.get('sha256') == asset['sha256']:
            target = prior['asset']
        else:
            target = f'r{revision}-{name}'
            if target not in remote:
                pending.append((pack / name, target))
        if target in remote or target == prior.get('asset'):
            verify(remote, target, asset['size'], asset['sha256'])
        rename[name] = asset['asset'] = target
    for file in manifest['files']:
        for segment in file['segments']:
            segment['asset'] = rename[segment['asset']]
    name = f'game-manifest-{revision}.json'
    data = encoded(manifest)
    digest = hashlib.sha256(data).hexdigest()
    (pack / name).write_bytes(data)
    with tempfile.TemporaryDirectory(dir=pack) as tmp:
        for source, target in pending:
            path = Path(tmp) / target
            try:
                os.link(source, path)
            except OSError:
                shutil.copyfile(source, path)
            upload(path)
            print(f'Uploaded {target}: {path.stat().st_size} bytes', flush=True)
    remote = metadata()
    for a in manifest['assets']:
        verify(remote, a['asset'], a['size'], a['sha256'])
    print(f'All {len(manifest["assets"])} release payloads verified', flush=True)
    if name not in remote:
        upload(pack / name)
        remote = metadata()
    verify(remote, name, len(data), digest)
    pointer = encoded(dict(version=1, revision=revision, manifest=name, sha256=digest))
    # GitHub rejects stale content SHA: concurrent publishers cannot replace a newer pointer.
    gh('api', '-X', 'PUT', CHANNEL, '-f', 'branch=game-channel', '-f', 'sha=' + entry['sha'],
       '-f', f'message=Publish game revision {revision}', '-f',
       'content=' + base64.b64encode(pointer).decode())
    print(pointer.decode().strip())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('packed_folder', type=Path)
    parser.add_argument('revision', type=int)
    args = parser.parse_args()
    publish(args.packed_folder, args.revision)
