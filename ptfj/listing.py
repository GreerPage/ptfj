# list photos under tag

from .deal_with_json import readjson

def listing(file, tag):
    """List photos under specified tag"""

    return '\n'.join(readjson(file)['tags'][tag])
