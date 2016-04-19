#Author: Hanwen Wang
#this file is to generlize the sourcing data method.
#here is the files that needed to be included
import computeMean
import deleteTemFile
# import downloadStateShape
# import downloadCoutyShape
# import downloadCLUShape
import downloadOneURL
import getAllURLS
import loadToDB
# import setOutputPath
import turnDbfToTxt
# import unZipStateShape
import unZipCLU
# import unzipCoutyShape
import deleteFile
import logging
import os
import getCLUList
import getTitle

#please set the workingDir
#here is the test direcotory
#
workingDir = 'C:\Users\hw544\AgDB\AgDBETL\eMODIS\RefactorProgram\\rerefactorCode\\finalrefactor\\file\\';

# #TODO: downloadStateShape
# downloadStateShape.main(workingDir)
#
# #TODO: downloadCoutyShape
# downloadCoutyShape.main(workingDir)

#TODO: downloadCLUShape
# downloadCLUShape.main(workingDir)

# #TODO: unZipStateShape
# unZipStateShape.main(workingDir)
#
# #TODO: unzipCoutyShape
# unzipCoutyShape.main(workingDir)

#TODO: unzipCLUShape
# CLUlist = unZipCLU.main(workingDir)
CLUlist = getCLUList.main(workingDir)
# #here is to set the environment
# logPosi = workingDir + "log.log"
# logging.basicConfig(filename= logPosi,level = logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# #frist set the working direcory to a specific direcoryS
# os.chdir(workingDir)
#
db="AgDB" #database name
targetTable = db +".dbo.TestTable" #this is load data table name
sqlServerInstance = "AG-AEM-BCRQYQ1\MSSQLAGDEV"
#
# workingdir = "sC:\Users\hw544\AgDB\AgDBETL\\eMODIS\\RefactorProgram\\rerefactorCode\\finalrefactor\\file\\"
# CLUlist = []
# clu = "ar001"
# CLUlist.append(clu)
# title = "US_eMTH_NDVI.2014.365-006.QKM.VI_NDVI.005.2014010002626"
#
# URLS =[]
# URL = "https://dds.cr.usgs.gov/emodis/CONUS/historical/TERRA/2014/comp_006/US_eMTH_NDVI.2014.365-006.QKM.COMPRES.005.2014010010308.zip"
# URLS.append(URL)

# #TODO: getAllURLS
URLS = getAllURLS.main()

#TODO: downloadeveryURL
for URL in URLS:
    #need to return one title
    downloadOneURL.main(workingDir,URL)
    # title = "US_eMTH_NDVI.2014.365-006.QKM.VI_NDVI.005.2014010002626"
    title = getTitle.main(workingDir)
    #TODO: computeMean
    computeMean.main(workingDir, title, CLUlist)

    #TODO: turnDbfToTxt
    turnDbfToTxt.main(workingDir,title, CLUlist)

    #TODO: loadToDB
    loadToDB.main(workingDir,db,targetTable,sqlServerInstance)
    # # #TODO: deleteTemFile
    deleteTemFile.main(workingDir)
#TODO: is to delete the downloaded file
deleteFile.main(workingDir)
