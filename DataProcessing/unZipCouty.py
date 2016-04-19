#this is to unzip all Couty shape to the server:
import os
import popen2

def main(workingDir):
    #this is to downlaod all the Couty shape file in the server here

    downloadZipPath = workingDir + "CountyZip//"

    CoutyPath = workingDir + "County//"
    if not os.path.exists(CoutyPath):
        os.mkdir(CoutyPath)

    #this is to define the outputresultPath
    outputResPath = workingDir + "outputRes//"
    coutyOutputResPath = outputResPath + "County//"

    if not os.path.exists(outputResPath):
        os.mkdir(outputResPath)

    coutyOutputResPath = outputResPath + "County//"
    if not os.path.exists(coutyOutputResPath):
        os.mkdir(coutyOutputResPath)

    temPath = downloadZipPath + "t1_2015_us_county.zip"
    unzipCountyPath = CoutyPath

    #can not unzip the couty files
    outAndErrorStream, inStream = popen2.popen4(workingDir + '7z.exe e -o' + unzipCountyPath + ' ' + temPath +" -aoa")      #when you run program first, plsease do this to unzip the shape file
    outAndErrorStream.close()
    inStream.close()

    #so the shape file is here

    #TODO unzip all Coutyfile to the specific directory

    #TODO delete the directory where the unzip Couty file is

    #here is nice to return all CoutyShape file List

if __name__ == "__main__":
    main()
