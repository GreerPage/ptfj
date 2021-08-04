# command line interface
import os
import sys

from .tag import Tagging
from .listing import listing
from .initial import Initial

def initial():

    global i
    i = Initial()

    if not i.has_run:
        i.initial()


def error():
	print('Usage: ptfj [ FILE_PATH ] [ TAG ]')
	print('Try \'ptfj --help\' for more information.')

def cli():
    """handles command line input"""

    initial()
    tagging = Tagging(i.json)

    args = sys.argv
    args.pop(0)

    if args == []:
        error()
    
    elif args == ['--help']:
        print('Usage: ptfj [ FILE_PATH ] [ TAG ]')
        print('Example: ptfj jackson.jpeg sillygeese')
        print()
        print('Listing: ptfj list [ TAG ]')
        print('Example: ptfj list sillygeese')  


    
