#the thing I need to do here is to delete all the files in outputresult and delete all the downloaded file and also the get rid of the ouputefile
#here is to delte all the downloaded files
import os
import shutil

def main(workingDir):

    downLoadPath = workingDir + "staging//"
    outputfilePath = workingDir + "output.txt"

    shutil.rmtree(downLoadPath)

    os.remove(outputfilePath)

#here is to delete the temperary file
