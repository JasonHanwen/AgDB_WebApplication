#this python is to get all URLs we need to download the layer

#now this file can get all URL list, so this is specific to every task
import urllib2
import shutil
import os
import popen2
import requests
from lxml import html

def main():
    url = 'https://dds.cr.usgs.gov/emodis/CONUS/historical/TERRA/'
    r = requests.get(url, auth=('woodardjoshua@gmail.com', 'USGSwoodard14'))
    tree = html.fromstring(r.text)
    aList = tree.xpath('//a/text()')                                            #alist is the tree structure which contains all years

    URLList = []

    for year in aList:
    # print year
        year = year.strip()
#        print year
        subURL = url + year
#        print subURL
        subRequest = requests.get(subURL, auth=('woodardjoshua@gmail.com', 'USGSwoodard14'))
        #   print subRequest.text
        subtree = html.fromstring(subRequest.text)
        subaList = subtree.xpath('//a/text()')
        #print subaList
        for day in subaList:
            #this is to get rid of the first and end whitespace
            day = day.strip()
            if(day[-2] != 'y'):                                                 #I'm not sure wheather nor not we need the 14-day shape, just get the data on 7-day basis
                downloadURL = subURL + day
                #print downloadURL
                URLList.append(downloadURL)
    #print URLList
    #this is to return the list from one file

    URLZiplist = []                                                             #URLZiplist is the specific download URL list. all linkas are stored in URL form
    for url in URLList:
        r = requests.get(url, auth=('woodardjoshua@gmail.com', 'USGSwoodard14'))
        tree = html.fromstring(r.text)
        aList = tree.xpath('//a/text()')                                        #for every link, get the fifth link which is in this format US_eMTH_NDVI.2015.293-299.QKM.COMPRES.005.2015303011712.zip\
        #download the 5th URLfor example: US_eMTH_NDVI.2015.293-299.QKM.COMPRES.005.2015303011712.zip\
        try:
            tem = aList[4].strip()
            specificUrl = url + tem
            URLZiplist.append(specificUrl)
        except Exception:
            print "there is no such file"
    print URLZiplist
    return URLZiplist
if __name__ == "__main__":
    main()
