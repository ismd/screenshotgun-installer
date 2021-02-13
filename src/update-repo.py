#!/usr/bin/env python3
import argparse
import os

from lib import update_packages

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Updates Screenshotgun repository')
    parser.add_argument('-c', '--config', help='Path to config directory', required=True)
    parser.add_argument('-o', '--output', help='Path to repository', required=True)
    parser.add_argument('-v', '--version', help='Screenshotgun version', required=True)

    args = parser.parse_args()
    config_path = update_packages(args.config, args.version)

    os.system('repogen -v --update -p "%s/macos/packages" "%s/macos"' % (config_path, args.path))
    os.system('repogen -v --update -p "%s/windows/packages" "%s/windows"' % (config_path, args.path))
