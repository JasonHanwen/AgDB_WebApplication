import logging
import os
import sys
import zipfile
import urllib2
import shutil
import popen2

#here is to set the working directory and URL that I need to go now let us just try one URL
def main(workingDir,URL):
    #TODO:here is the specific download method,you should change here, so that it can download spefific URL file to workingdir
    #this is to set the passwork and username
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, URL, "woodardjoshua@gmail.com", "USGSwoodard14")
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    opener.open(URL)
    urllib2.install_opener(opener)

    #here is to build a new staging directory that will store the downloaded file
    print "begin downloading FROM" + URL
    logging.info("begin downloading FROM" + URL)

    req =urllib2.urlopen(URL)

    # downLoadFileName = downLoadFileName[:-4]

    #here is to get the downloadfilepath,the default downloading path is workingdir/staging
    downLoadPath = workingDir + "staging//"
    if not os.path.exists(downLoadPath):
        os.makedirs(downLoadPath)

    #here is to get the name of downloaded layer
    logging.info("begin get the name of downloaded File" + URL)
    URLCompList = URL.split('/')
    downLoadFileName = URLCompList[-1]
    title = downLoadFileName[:-4]
    logging.info("finish get the name of downloaded File" + URL)

    #here is to get the download fileName
    logging.info("begin downloading" + title)
    with open(downLoadPath + downLoadFileName, 'wb') as fp:
        shutil.copyfileobj(req, fp)
    fp.close()
    print "finish downloading"
    logging.info("finish downloading" + title)


    #here is to unzip the downloaded layer
    #make sure there is 7z.exe in the workingDir
    logging.info("begin unzip" + URL)                                     #there is .zip for the
    outAndErrorStream, inStream = popen2.popen4(workingDir + '7z.exe e -o' + workingDir + 'staging\ ' + workingDir + "staging\\" + downLoadFileName + " -aoa")
    outAndErrorStream.close()
    inStream.close()
    logging.info("finish unzip" + URL)

    return title

if __name__ == "__main__":
    main()
