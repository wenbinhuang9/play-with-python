import  os


def replace(output):
    output = output.strip()
    output = output.replace(' ', '\ ')
    output = output.replace('(', '\(')
    output = output.replace(')', '\)')
    return output
path = "/Users/ben/Downloads"
os.chdir(path)

stream  = os.popen('ls -Art|tail -n 1')
output = stream.read()
print(output)
output = output.strip()
output = output.replace(' ', '\ ')
output = output.replace('(', '\(')
output = output.replace(')', '\)')

opencmd = "open " + output
os.popen(opencmd)


print("success")