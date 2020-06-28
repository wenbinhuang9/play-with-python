
import os
import sys


if len(sys.argv) < 2:
    print("please input file ")
    exit(0)

def openByFileName(filename):
    os.popen('open ' + filename + ' -a \'Foxit Reader\'')

def openBySearching(searchContent):
    stream = os.popen('s ' + searchContent)
    filename = stream.read()

    filename = filename.strip()
    print("the search file name is {0}".format(filename))
    openByFileName(filename)

if len(sys.argv) == 2:
    filename = sys.argv[1]
    openByFileName(filename)
    exit()
elif len(sys.argv) == 3:
    if sys.argv[1] != "-s":
        print("unsupported command")
    else:
        openBySearching(sys.argv[2])
    exit()
else:
    print("illegal command")
