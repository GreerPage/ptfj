# run for initial setup
import os
import sys

from pathlib import Path

def initial():
    # determine path for ptfj directory
    home = str(Path.home())
    p = home + 'Documents' if sys.platform == 'win32' else home

    os.mkdir(p)