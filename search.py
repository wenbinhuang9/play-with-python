
import os
import sys

path = ["/Users/ben/Downloads"]

def main(argv):
    search_content = argv[1]
    for p in path:
        os.chdir(p)
        cmd = "ls -a|grep " + search_content
        stream = os.popen(cmd)
        print(stream.read())


if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("please input search content")
    else:
        main(sys.argv)


