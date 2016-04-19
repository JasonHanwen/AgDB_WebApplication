import os

def main(workingDir):
    layerDir = workingDir + "\\staging\\"
    LayerName = ""
    for files in os.walk(layerDir):
        filesList = files[2]
        # print filesList
        for onefile in filesList:
            temlist = onefile.split('.')
            # print temlist
            filetype = temlist[-1]
            # print filetype
    # # # US_eMTH_NDVI.2000.049-055.QKM.VI_NDVI.005.2009220231055.tif
            Datatype = temlist[-4]
            # print Datatype
            Datatype = Datatype[-4:]
            # print Datatype
            if(filetype == 'tif' and Datatype =='NDVI'):
                LayerName = onefile
    return LayerName
