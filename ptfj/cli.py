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
    file = i.json
    tagging = Tagging(file)

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
        return

    elif len(args) != 1:
        tag = args[1]      

        if args[0] == 'list':
            if tag not in tagging.tags: 
                print(f'Error: {tag}: tag not found')
                return
            print(listing(file, tag))
        
        else: 
            if not os.path.isfile(args[0]):
                print(f'Error: {args[0]}: file not found')
                return

            if len(args) == 3:
                if args[2] == 'remove':
                    print('e')
                    if tag not in tagging.tags: 
                        print(f'Error: {tag}: tag not found')
                        return
                    tagging.untag(tag, args[0])
                    
            tagging.tag(tag, args[0])




    
