import asyncio
import pathlib
import subprocess

def update(release_url):
    path = "%s/scripts/update.sh" % pathlib.Path(__file__).parent.parent.absolute()

    print("Running in background", path)
    subprocess.Popen(path)
