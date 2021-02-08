#!/bin/bash

VERSION=$1

ROOT_DIR="$(dirname "${BASH_SOURCE[0]}")/.."
FILE="$(basename "${BASH_SOURCE[0]}")"

if [ -z "$VERSION" ]; then
  echo "Usage: $FILE <version>"
  exit 1
fi

DATE=$(date +'%Y-%m-%d')

# osx
sed -i "s#<Version>.*</Version>#<Version>$VERSION</Version>#g" "$ROOT_DIR/configs/osx/packages/screenshotgun/meta/package.xml"
sed -i "s#<ReleaseDate>.*</ReleaseDate>#<ReleaseDate>$DATE</ReleaseDate>#g" "$ROOT_DIR/configs/osx/packages/screenshotgun/meta/package.xml"

# windows
sed -i "s#<Version>.*</Version>#<Version>$VERSION</Version>#g" "$ROOT_DIR/configs/windows/packages/screenshotgun/meta/package.xml"
sed -i "s#<ReleaseDate>.*</ReleaseDate>#<ReleaseDate>$DATE</ReleaseDate>#g" "$ROOT_DIR/configs/windows/packages/screenshotgun/meta/package.xml"
