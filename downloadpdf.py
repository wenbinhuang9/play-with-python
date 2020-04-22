from urllib.request import urlretrieve
import  sys

## download pdf from the url
def download_file(download_url):
    urlretrieve(download_url, "./some_file.pdf")
def main(argv):
    if len(argv) <=1:
        print ("invalid input|argument is too less")
    url = argv[1]
    download_file(url)

    print( "success")

if __name__ == "__main__":
     main(sys.argv)
