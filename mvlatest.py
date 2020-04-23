import os

curpath = os.getcwd()
curpath = curpath.replace(' ', '\ ')
path = "/Users/ben/Downloads"
os.chdir(path)
stream  = os.popen('ls -Art|tail -n 1')

output = stream.read()
output = output.strip()
output = output.replace(' ', '\ ')
output = output.replace('(', '\(')
output = output.replace(')', '\)')

fromdir = path + "/" + output

mvcmd = "mv -f " + fromdir + " " + curpath
print(mvcmd)
os.popen(mvcmd)
