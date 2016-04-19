#this is to compute the mean value from workingDir
import logging
import os
import arcpy
from arcpy import env
#so now  I just do the refactoring for the CLU level
#this step I just achieve a CLU shape file computation

# def main(workingDir, title, CLUshapeList, CountyShapeList, StateShapeList):
def main(workingDir, title, CLUshapeList):
    #set the result to the output result path
    #TODO:get the essential information from title like year, month, you should change it accordingly
    outputResPath = workingDir + "outputRes//"
    arcpy.CheckOutExtension("Spatial")
    arcpy.CheckOutExtension("GeoStats")
    os.chdir(workingDir)
    arcpy.env.overwriteOutput = True

    #Clu is the read path
    #clu is a list like ar003
    #TODO write all CLU dbf files to txt file, the outputpath is fixed, so we can read the file without parameter
    for clu in CLUshapeList:
        county = clu[0:2]
        CluNum = clu[-3:]
        outputSpecPath = outputResPath +  "CLU//" + county + "//" + county + CluNum + "//"
        shapeSpecPath = workingDir + "CLU//" + county + "//" + county + CluNum + "//" + "clu_public_a_"+ county + CluNum +".shp"
        #here is to get the last part of the read path and combien with outputResPath
        env.workspace = outputSpecPath
        try:                                                                #compute the mean value, given the specific raster file, and output is ZonnalStUS.dbfs
            print title
            Layer = arcpy.mapping.Layer(workingDir +"staging\\" + title)
            Raster = arcpy.Raster(workingDir +"staging\\" + title)
            arcpy.gp.ZonalStatisticsAsTable_sa(shapeSpecPath,"FID",workingDir +"\\staging\\" + title,outputSpecPath + "ZonalStUS.dbf","DATA","MEAN")
            print "Success" + clu
        except Exception as e:
            print "Fail" + clu
            logging.info("Fail compute" + clu)

    # #TODO write all couty dbf files to txt file, the outputpath is fixed, so we can read the file without parameter
    # for couty in CountyShapeList #there may jast one file here.
    outputSpecPath = outputResPath + "County//"
    shapeSpecPath = workingDir + "County//" + "tl_2015_us_county.shp"
    env.workspace = outputSpecPath
    #here I should Chanage

    try:                                                                #compute the mean value, given the specific raster file, and output is ZonnalStUS.dbfs
        # arcpy.gp.ZonalStatisticsAsTable_sa(specificUnZipShapePath,"FID",workingDir +"\\staging\\US_eMTH_NDVI.2014.365-006.QKM.VI_NDVI.005.2014010002626.tif","ZonalStUS.dbf","DATA","MEAN")
        print title
        Layer = arcpy.mapping.Layer(workingDir +"staging\\" + title)
        Raster = arcpy.Raster(workingDir +"staging\\" + title)
        arcpy.gp.ZonalStatisticsAsTable_sa(shapeSpecPath,"GEOID",workingDir +"\\staging\\" + title,outputSpecPath + "ZonalStUS.dbf","DATA","MEAN")
        print "Success + county"
    except Exception as e:
        print "Fail + couty"
        logging.info("Fail compute + couty")

    # #TODO write all state dbf files to txt file, the outputpath is fixed, so we can read the file without parameter
    # #the result may just one line
    # for state in StateShapeList:
    #     outputSpecPath = outputResPath + ...
    #     #here is to get the last part of the read path and combien with outputResPath
    #     arc.env = outputSpecPath
    #     #here I should Chanage
    #     try:                                                                #compute the mean value, given the specific raster file, and output is ZonnalStUS.dbfs
    #         # arcpy.gp.ZonalStatisticsAsTable_sa(specificUnZipShapePath,"FID",workingDir +"\\staging\\US_eMTH_NDVI.2014.365-006.QKM.VI_NDVI.005.2014010002626.tif","ZonalStUS.dbf","DATA","MEAN")
    #         arcpy.gp.ZonalStatisticsAsTable_sa(clu,"GEOID..",workingDir +"\\staging\\" + title +".tif","ZonalStUS.dbf","DATA","MEAN")
    #     except:
    #         print "Fail" + state
    #         logging.info("Fail compute" + state)

# it would be fine to return a list contain the CLUshapeList, CountyShapeList, StateShapeList
