#!/usr/bin/env python3
import argparse
import os
import pathlib

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Creates installer for Screenshotgun')

    parser.add_argument('-o', '--output', help='Output file', required=True)
    parser.add_argument('-v', '--version', help='Screenshotgun version', required=True)

    parser.add_argument(
        '-t',
        '--type',
        help='Type of binary',
        required=True,
        choices=['macos', 'windows'],
    )

    args = parser.parse_args()
    root_path = pathlib.Path(__file__).parent.parent.absolute()

    os.system('binarycreator '
              '-n '
              '-v '
              '-c %s/config/%s/config/config.xml '
              '-p %s/config/%s/packages '
              '%s' % (root_path, args.type, root_path, args.type, args.output))
