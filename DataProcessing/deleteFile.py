#the thing I need to do here is to delete all the files in outputresult and delete all the downloaded file and also the get rid of the ouputefile
#here is to delte all the downloaded files
import os
import shutil

def main(workingDir):
    CLUdownloadZipPath = workingDir + "CLUZip//"
    CLUPath = workingDir + "CLU//"
    Couty

    CoutydownloadZipPath = workingDir + "CoutyZip//"
    CoutyPath = workingDir + "Couty//"

    StatedownloadZipPath = workingDir + "StateZip//"
    StatePath = workingDir + "State//"

    shutil.rmtree(CLUdownloadZipPath)
    shutil.rmtree(CLUPath)

    shutil.rmtree(CoutydownloadZipPath)
    shutil.rmtree(CoutyPath)

    shutil.rmtree(StatedownloadZipPath)
    shutil.rmtree(StatePath)

    outputPath = workingDir + "outputRes//"
    shutil.rmtree(outputPath)
#here is to delete the temperary file
