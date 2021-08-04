# store photo name under certain tag
import os 
import json

from .deal_with_json import readjson, writejson

class Tagging():
    """Handle tagging"""

    def __init__(self, file):
        self.file = file
    
    def create_tag(self, name):
        """Create a tag"""

        tags = readjson(self.file)['tags']
        
        tags[name] = []