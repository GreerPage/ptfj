# read and write json

import json

def readjson(file):
    with open(file, 'r') as e:
        return json.load(e)


def writejson(file, data):
    with open(file, 'w') as e:
        json.dump(data, e)