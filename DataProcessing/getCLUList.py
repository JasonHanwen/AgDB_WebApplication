#this is to unzip all CLU shape to the server:
import os
import popen2

def main(workingDir):
    #this is to unzip all the CLU shape file in the server here

    downloadZipPath = workingDir + "CLUZip//"

    #all unzip shape file is in workingDir//CLU
    CLUPath = workingDir + "CLU//"
    if not os.path.exists(CLUPath):
        os.mkdir(CLUPath)

    #all computation of CLU shape file is in outputRes//CLU//
    outputResPath = workingDir + "outputRes//"
    if not os.path.exists(outputResPath):
        os.mkdir(outputResPath)

    #here is to set CLUOutputResPath
    CLUOutputResPath = outputResPath + "CLU//"
    if not os.path.exists(CLUOutputResPath):
        os.mkdir(CLUOutputResPath)


    #this function is  just to return all the subfilesName ofCLU files, with .zip, CLU format is under working directory
    HashCLUResult = {}
    CLUDirs = []
    #this list is to return the file that the computation mean needs
    CLUList = []

    #this is to walk all CLU files
    for dirs in os.walk(downloadZipPath):
        CLUDirs.append(dirs)

    print CLUDirs
    del CLUDirs[0]
    countyResult = []
    countyName = []
    for CLUdir in CLUDirs:
        if CLUdir[2]:
            tem = CLUdir[0].split("\\")
            TemcountyName = tem[-2]                                             #here is to set state level name
            TemcountyName = TemcountyName[-2:]
            countyName.append(TemcountyName)
            HashCLUResult[TemcountyName] = CLUdir[2]                            #this is to set county level name

    print HashCLUResult

    outputPathList =[]                                                          #this is to store all list of outputPath
    errorFile=[]                                                                #this is to store all errir files

    for key in HashCLUResult:
        print key
        print HashCLUResult[key]
        if key == "clu":
            continue
                                                                   #I'm not sure why there would be this problem, the key will show CLU
        suboutputPath = CLUOutputResPath + key;                                 #this is the state level output direcotry
        if not os.path.exists(suboutputPath):
            os.makedirs(suboutputPath)

        subUnzipPath = CLUPath + key;
        if not os.path.exists(subUnzipPath):
            os.makedirs(subUnzipPath)

        subCLUList = HashCLUResult[key]                                         #this is the county in the key state for example: clu_public_a_me001.zip belongs to me

        for clu in subCLUList:
            tempstr = clu.split("_")[-1]                                        #this is to getthe specific county name for example for clu_public_a_me001.zip, get me001
            cluouput = tempstr[:-4]
            print cluouput                                                      #this is to get all countyName
            CLUList.append(cluouput)

            specificOutPath = suboutputPath
            specificOutPath = specificOutPath + "\\" + cluouput +"\\"
            if not os.path.exists(specificOutPath):
                os.makedirs(specificOutPath)
            # print specificOutPath                                               #this is the county level output direcory

            specificUnzipPath = subUnzipPath
            specificUnzipPath = subUnzipPath + "\\" + cluouput +"\\"
            if not os.path.exists(specificUnzipPath):
                os.makedirs(specificUnzipPath)

            outputPathList.append(specificOutPath)
            print os.getcwd()



            subReadPath = downloadZipPath + key + "\\" + "clu\\"                       #this is to get state level read path
            temPath = subReadPath + "clu_public_a_" +  cluouput + ".zip"        #temPath is the county level read path, the file is in zip file before, need to be unziped


            unZipShapePath = specificUnzipPath                                  #unZipShapePath is to set the unzip file, which is the output path for unzip command

            #this is to unzip all CLUpath
            #this is to unzip all shape files
            # outAndErrorStream, inStream = popen2.popen4(workingDir + '7z.exe e -o' + unZipShapePath + '\ ' + temPath +" -aoa")      #when you run program first, plsease do this to unzip the shape file
            # outAndErrorStream.close()
            # inStream.close()
    return CLUList
    #TODO delete the directory where the unzip CLU file is
