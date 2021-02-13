#!/usr/bin/env python3
import argparse
import os
import pathlib

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Creates installer for Screenshotgun')
    parser.add_argument('-o', '--output', help='Output file', required=True)

    args = parser.parse_args()
    path = pathlib.Path(__file__).parent.absolute()

    os.system('binarycreator '
              '-n '
              '-v '
              '-c %s/configs/windows/config/config.xml '
              '-p %s/configs/windows/packages '
              '%s' % (path, path, args.output))
