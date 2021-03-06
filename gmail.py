## todo the ability to store the email and  retreive, enabling intelligence.

import yagmail
import  os
import sys
frommail = ""
password = ""
yag = yagmail.SMTP(frommail, password)

tomailstorefile = "~/bin/tomailer.txt"


def loadtomail():
    with open(tomailstorefile, "w+") as fd:
        lines = fd.readlines()

    mailset = set(lines)

    return mailset

def writetomail(tomail):
    mailset = loadtomail()

    if tomail not in mailset:
        with open(tomailstorefile, "w+") as fd:
            fd.writelines([tomail])


def match(tomail):
    mailset = loadtomail()

    for mail in mailset:
        if tomail in mail:
            return mail
    return None

def sendMail(mail, title, content, attachment):
    contents = [content]
    yag.send(mail, title, contents, attachments = attachment)


def main(argv):
    filname = argv[1]
    mail = argv[2]

    dir = os.getcwd()

    filepath = dir + "/" + filname

    sendMail(mail, filname, "", filepath)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("please input filename and email")

    main(sys.argv)
    mail = sys.argv[2]
    print("mail to {0} success".format(mail))
