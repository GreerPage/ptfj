# run for initial setup
import os
import sys

from pathlib import Path

class Initial():
    """perform actions necessary for setup"""

    def __init__(self):
        self.home = str(Path.home())
        self.p = self.home + 'Documents' if sys.platform == 'win32' else self.home


    def initial(self):
        """Creates ptfj directory"""

        os.mkdir(self.p)

    def has_run(self):
        """Determine if setup has completed"""

        return os.path.isdir(self.p)