#!/usr/bin/env python3
import argparse
import os

from lib import update_packages

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Creates repository for Screenshotgun')
    parser.add_argument('-c', '--config', help='Path to config directory', required=True)
    parser.add_argument('-o', '--output', help='Output path', required=True)
    parser.add_argument('-v', '--version', help='Screenshotgun version', required=True)

    args = parser.parse_args()
    config_path = update_packages(args.config, args.version)

    # macOs
    os.system('repogen -v -p "%s/macos/packages" "%s/macos"' % (config_path, args.output))
    os.system('sed -i s/\{AnyApplication\}/Screenshotgun/g "%s/macos/Updates.xml"' % (args.output))

    # Windows
    os.system('repogen -v -p "%s/windows/packages" "%s/windows"' % (config_path, args.output))
    os.system('sed -i s/\{AnyApplication\}/Screenshotgun/g "%s/windows/Updates.xml"' % (args.output))
