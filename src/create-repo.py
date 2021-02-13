#!/usr/bin/env python3
import argparse
import os
import pathlib

from lib import update_packages

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Creates repository for Screenshotgun')
    parser.add_argument('-c', '--config', help='Path to config directory', required=True)
    parser.add_argument('-o', '--output', help='Output path', required=True)
    parser.add_argument('-v', '--version', help='Screenshotgun version', required=True)

    args = parser.parse_args()
    update_packages(args.config, args.version)

    path = pathlib.Path(__file__).parent.absolute()

    # macOs
    os.system('repogen -v -p "%s/configs/macos/packages" "%s/macos"' % (path, args.output))
    os.system('sed -i s/\{AnyApplication\}/Screenshotgun/g "%s/macos/Updates.xml"' % (path, args.output))

    # Windows
    os.system('repogen -v -p "%s/configs/windows/packages" "%s/windows"' % (path, args.output))
    os.system('sed -i s/\{AnyApplication\}/Screenshotgun/g "%s/windows/Updates.xml"' % (path, args.output))
