#!/bin/bash

OUTPUT_PATH=$1

ROOT_DIR="$(dirname "${BASH_SOURCE[0]}")/../.."
FILE="$(basename "${BASH_SOURCE[0]}")"

if [ -z "$OUTPUT_PATH" ]; then
  echo "Usage $FILE <output_path>"
  exit 1
fi

repogen -v --update -p "$ROOT_DIR/configs/osx/packages" "$OUTPUT_PATH/osx"
repogen -v --update -p "$ROOT_DIR/configs/windows/packages" "$OUTPUT_PATH/windows"

sed -i s/\{AnyApplication\}/Screenshotgun/g "$OUTPUT_PATH/osx/Updates.xml"
sed -i s/\{AnyApplication\}/Screenshotgun/g "$OUTPUT_PATH/windows/Updates.xml"
