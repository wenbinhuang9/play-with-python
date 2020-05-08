
## create a pipeline command, the first command  will be used as the second output!
## similar to the idea of linux. , this command is also very simple to implement


import os
import sys
def pipe(args):

   s = "".join(args[1:])

   splitcmd = s.split("|")

   if len(splitcmd) < 1:
      print("please input at least one command line")

      return

   output = ""
   for i, cmd in enumerate(splitcmd):
      if i == 0:
         stream = os.popen(cmd)
         output = stream.read()

      else:
         cmd = cmd + " " + output
         stream = os.popen(cmd)
         output = stream.read()

   return

if __name__ == "__main__":
   pipe(sys.argv)