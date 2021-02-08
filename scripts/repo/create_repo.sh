#!/bin/bash

ROOT_DIR="$(dirname "${BASH_SOURCE[0]}")/../../"
mkdir -p "$ROOT_DIR/build"

repogen -v -p "$ROOT_DIR/configs/osx/packages" "$ROOT_DIR/build/osx"
repogen -v -p "$ROOT_DIR/configs/windows/packages" "$ROOT_DIR/build/windows"

sed -i s/\{AnyApplication\}/Screenshotgun/g "$ROOT_DIR/build/osx/Updates.xml"
sed -i s/\{AnyApplication\}/Screenshotgun/g "$ROOT_DIR/build/windows/Updates.xml"
