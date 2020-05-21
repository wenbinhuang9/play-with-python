from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import sys

def upload(filename):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)

    file1 = drive.CreateFile({'title': filename})
    path = "./" + filename
    file1.SetContentFile(path)
    file1.Upload() # Files.insert()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("please input the file name")
    else:
        upload(sys.argv[1])



