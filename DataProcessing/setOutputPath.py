#this is to set the output path for the computation result.
#this path should be quite the same as the CLU, County and State direcory

import os

def main(workingDir):
    #this is to downlaod all the CLU shape file in the server here

    outputResPath = workingDir + "outputRes//"
    #there should be CLU, county and state level output directory.
    if os.exist(outputResPath)
        os.mkdir(outputResPath)
    #then set the outputpath
    #it is better to set the result path at the sametime with unzip the shape file
    #TODO unzip all CLUfile to the specific directory

    #TODO delete the directory where the unzip CLU file is
