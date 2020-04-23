import  os

path = "/Users/ben/Downloads"
os.chdir(path)

stream  = os.popen('ls -Art|tail -n 1')
output = stream.read()
print(output)
