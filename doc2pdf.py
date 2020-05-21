##this can be only to used in Mac platform
#- the textutil and cupsfilter command is supported by mac os
import os
import sys

def doc2pdf(filename):

    name = filename.split(".")
    name = name[0]
    htmlfile = "./" + name + ".html"
    pdffile = "./" + name + ".pdf"
    cmd = "textutil -convert html -output " + htmlfile + " " + filename

    stream = os.popen(cmd)
    print(stream.read())
    cmd = "cupsfilter" + " " + htmlfile +  " > " + pdffile
    stream = os.popen(cmd)
    print(stream.read())

    if os.path.exists("./" + htmlfile):
        stream = os.popen("rm " + "./" + htmlfile)
        print(stream.read())


if __name__=="__main__":
    if len(sys.argv) != 2:
        print("doc to pdf, usage, please input file name ")
    else:
        doc2pdf(sys.argv[1])




