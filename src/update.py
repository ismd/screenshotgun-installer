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
        tag = release['tag_name']

        for asset in release["assets"]:
            fetcher.fetch(asset['name'], asset['browser_download_url'])

    if not fetcher.linux:
        raise FileNotFoundError("Can't fetch linux asset")
    if not fetcher.macos:
        raise FileNotFoundError("Can't fetch macOs asset")
    if not fetcher.windows:
        raise FileNotFoundError("Can't fetch windows asset")

    return fetcher

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

def update_repository():
    pass

def update_launchpad():
    pass

def update_aur():
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Downloads artifacts from GitHub releases and updates local repository, Launchpad and AUR')
    parser.add_argument('-u', '--url', help='GitHub release url', required=True)
    parser.add_argument('-v', '--version', help='Screenshotgun version', required=True)

    args = parser.parse_args()
    fetcher = fetch(args.url)
    unzip(linux=fetcher.linux, macos=fetcher.macos, windows=fetcher.windows)

    update_repository()
    update_launchpad()
    update_aur()
