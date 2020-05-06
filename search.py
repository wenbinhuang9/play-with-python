
import os
import sys


def replace(output):
    output = output.strip()
    output = output.replace(' ', '\ ')
    output = output.replace('(', '\(')
    output = output.replace(')', '\)')
    return output

def main(argv):
    path = ["/Users/ben/Downloads", "/Users/ben/Documents/bookish/datastructure-and-algorithm"]

    if len(sys.argv) ==3:
        search_content = argv[2]
        dir = argv[1]
        search_dir = getalldirectories(dir)
        search_dir.append(dir)
        path = search_dir
    else:
        search_content = argv[1]

    for p in path:
        os.chdir(p)
        cmd = "ls -a|grep " + search_content
        stream = os.popen(cmd)
        filename = stream.read()
        if filename.strip() != "":
            filename = replace(filename)
            output = p + "/" + filename
            print(output)

def getalldirectories(dir):
    total_dir = [os.path.join(dir, d) for d in os.listdir(dir) if  os.path.isdir(os.path.join(dir,d))]

    for nextdir in total_dir:
        dir_list = getalldirectories(nextdir)
        total_dir.extend(dir_list)

    return total_dir

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("please input search content")
    else:
        main(sys.argv)
    

