# Screenshotgun installer

Qt Installer Framework files for Screenshotgun in this repo.

## Commands

These commands create or update repository inside `OUTPUT_PATH` directory. Also there is a command to build binary installer.

### Create repository

``` sh
make VERSION=<version> OUTPUT_PATH=<path> create_repo
```

### Update repository

``` sh
make VERSION=<version> OUTPUT_PATH=<path> update_repo
```

### Create installer
``` sh
make OUTPUT_FILE=<path> create_installer
```
