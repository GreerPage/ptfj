# store photo name under certain tag
import os 
import json

from .deal_with_json import readjson, writejson

class Tagging():
    """Handle tagging"""

    def __init__(self, file):
        self.path = file
        self.file = readjson(self.path)
        self.tags = self.file['tags']
    
    def create_tag(self, name):
        """Create a tag"""

        self.tags[name] = []

    def tag(self, t, f):
        """Tag a photo"""

        if not t in self.tags:
            self.create_tag(t)

        self.tags[t].append(f)
        writejson(self.path, self.file)
