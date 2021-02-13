#!/usr/bin/env python3
import argparse
import os
import pathlib

from lib import update_packages

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Updates Screenshotgun repository')
    parser.add_argument('-c', '--config', help='Path to config directory', required=True)
    parser.add_argument('-o', '--output', help='Path to repository', required=True)
    parser.add_argument('-v', '--version', help='Screenshotgun version', required=True)

    args = parser.parse_args()
    update_packages(args.config, args.version)

    dir = pathlib.Path(__file__).absolute()
    os.system('repogen -v --update -p "%s/configs/macos/packages" "%s/macos"' % (dir, args.path))
    os.system('repogen -v --update -p "%s/configs/windows/packages" "%s/windows"' % (dir, args.path))
