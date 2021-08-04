# run for initial setup
import os
import sys

from pathlib import Path
from .deal_with_json import writejson

class Initial():
    """perform actions necessary for setup"""

    def __init__(self):
        self.home = str(Path.home())
        self.p = self.home + 'Documents/.ptfj' if sys.platform == 'win32' else self.home + '/.ptfj'
        self.has_run = os.path.isdir(self.p)
        self.json = self.p + '/tags.json'

    def initial(self):
        """Creates ptfj directory"""

        os.mkdir(self.p)
        writejson(self.json, {"tags":{}})
        
