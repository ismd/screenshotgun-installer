#!/usr/bin/env python3
import argparse
import json
import os
import pathlib
import shutil
import urllib.request
import zipfile

class Fetcher:
    linux = None
    macos = None
    windows = None

    def fetch(self, asset, url):
        filename = '/tmp/%s' % asset

        with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

        if asset == 'screenshotgun_linux.zip':
            self.linux = filename
        elif asset == 'screenshotgun_macos.zip':
            self.macos = filename
        elif asset == 'screenshotgun_windows.zip':
            self.windows = filename

def fetch(url):
    fetcher = Fetcher()

    with urllib.request.urlopen(url) as stream:
        release = json.loads(stream.read())

        if len(release['assets']) < 3:
            raise FileNotFoundError('Not enough assets: %d (3 required)' % len(release['assets']))

        tag = release['tag_name']
        for asset in release['assets']:
            fetcher.fetch(asset['name'], asset['browser_download_url'])

    if not fetcher.linux:
        raise FileNotFoundError("Can't fetch linux asset")
    if not fetcher.macos:
        raise FileNotFoundError("Can't fetch macOs asset")
    if not fetcher.windows:
        raise FileNotFoundError("Can't fetch windows asset")

    return fetcher, tag

def unzip(linux, macos, windows):
    for dir in ('/tmp/screenshotgun_linux', '/tmp/screenshotgun_macos', '/tmp/screenshotgun_windows'):
        try:
            shutil.rmtree(dir)
        except:
            pass

        os.mkdir(dir)

        if dir == '/tmp/screenshotgun_linux':
            filename = linux
        elif dir == '/tmp/screenshotgun_macos':
            filename = macos
        elif dir == '/tmp/screenshotgun_windows':
            filename = windows

        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall(dir)

def update_repository(version):
    os.system('make -f %s/Makefile VERSION=%s update-repo' % pathlib.Path(__file__).parent.absolute(), version)

def update_launchpad():
    pass

def update_aur():
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Downloads artifacts from GitHub releases and updates local repository, Launchpad and AUR')
    parser.add_argument('-u', '--url', help='GitHub release url', required=True)

    args = parser.parse_args()
    fetcher, tag = fetch(args.url)
    version = tag[1:]
    unzip(linux=fetcher.linux, macos=fetcher.macos, windows=fetcher.windows)

    update_repository(version)
    update_launchpad()
    update_aur()
