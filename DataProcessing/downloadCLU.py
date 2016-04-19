#this is to download all CLU shape to the server:
import requests
from lxml import html


def main(workingDir):
    #this is to downlaod all the CLU shape file in the server here

    #TODO get the specific URL here to download CLU file here
    URL = "  "

    #I can download from dropBox directely
    downloadPath = workingDir + "CLUZip//"
    #TODO write the specific code here to download the CLU Shape file
    URL = 'https://www.dropbox.com/sh/870e07iehzo68le/AACrEmc54raFXFoLs3Wlk7YKa?dl=0'

    r = requests.get(URL)
    tree = html.fromstring(r.text)

    print tree
    print r.text

    #here is the download file, even with the click, we can not downlaod files from the website, so How can we do it
    # aList = tree.xpath('//a/text()')                                            #alist is the tree structure which contains all years

if __name__ == "__main__":
    main("1")
