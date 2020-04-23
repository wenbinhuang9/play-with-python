
import  sys
import  re

py_bin_file = "~/bin"
import os
def main(argv):
    if len(argv) < 2:
        print("input a python script ")
        return

    scriptname = argv[1]

    fd = open("./" + scriptname)

    pcmd = "#!/usr/local/bin/python3.7\n"

    lines = fd.readlines()

    mat_obj = re.match("(.*)\.py", scriptname)

    executable_name = mat_obj.group(1)

    fd = open(executable_name, "w+")
    fd.write(pcmd)
    fd.writelines(lines)

    source_file = "./" + executable_name
    to_dir = py_bin_file
    mvcmd =" ".join(["mv", source_file, to_dir])
    os.popen(mvcmd)

    print(mvcmd)

    os.popen("chmod +x " + py_bin_file + "/" +  executable_name)

    print("success")



if __name__ == "__main__":
    main(sys.argv)


