#!/bin/bash

OUTPUT_FILE=$1

ROOT_DIR="$(dirname "${BASH_SOURCE[0]}")/.."
FILE="$(basename "${BASH_SOURCE[0]}")"

if [ -z "$OUTPUT_FILE" ]; then
  echo "Usage: $FILE <output_file>"
  exit 1
fi

binarycreator \
  -n \
  -v \
  -c "$ROOT_DIR/configs/windows/config/config.xml" \
  -p "$ROOT_DIR/configs/windows/packages" \
  "$OUTPUT_FILE"
