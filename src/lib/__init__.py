#!/usr/bin/env python3
import argparse
import os
import pathlib
import shutil

def update_packages(config_path, version):
    path = '/tmp/installer-config'
    os.system('rm -rf %s' % path)
    shutil.copytree(config_path, path)

    # macOs
    os.system('sed -i "s#<Version>.*</Version>#<Version>%s</Version>#g" "%s/macos/packages/screenshotgun/meta/package.xml"' % (version, path))
    os.system('sed -i "s#<ReleaseDate>.*</ReleaseDate>#<ReleaseDate>%s</ReleaseDate>#g" "%s/macos/packages/screenshotgun/meta/package.xml"' % (version, path))

    # Windows
    os.system('sed -i "s#<Version>.*</Version>#<Version>%s</Version>#g" "%s/windows/packages/screenshotgun/meta/package.xml"' % (version, path))
    os.system('sed -i "s#<ReleaseDate>.*</ReleaseDate>#<ReleaseDate>%s</ReleaseDate>#g" "%s/windows/packages/screenshotgun/meta/package.xml"' % (version, path))
