#this is to write all result dbf to a output file
#we need to get the essential information about what we need from the name of the file

#here are a lot of file here

#here we change the CLURestList to only list of ar003
import us
import logging
import os
import arcpy
import datetime
from dbfpy import dbf

# def main(workingDir, title, CLUResList, CountyResList, StateResList):
def main(workingDir, title, CLUResList):
    #TODO:get the essential information from title like year, month, you should change it accordingly
    outputfilePath = workingDir + "output.txt"
    #here we need to create the file

    if not os.path.exists(outputfilePath):
        with open(outputfilePath, 'w') as outputfileCreat:
            outputfileCreat.close()

    #TODO get the essential information from the title
    #get the essential information from title
    #this part is to get essential information from the title, you should change here
    List = title.split('.')
    Year = List[1]
    temday = List[2]
    temdayList = temday.split('-')
    DayofYearStart = temdayList[1]                                                   #DayofYearStart is the attribute of DayofYearStart
    print DayofYearStart
    DayofYearEnd = str(int(DayofYearStart) + 6)                                      #DayofYearEnd is the attribtue of DayofYearEnd
    DayofYearEnd = "000" + DayofYearEnd
    DayofYearEnd = DayofYearEnd[-3:]
    print DayofYearEnd
    day = datetime.date(int(Year),1,1) + datetime.timedelta(days = (int(DayofYearStart) - 1) )
    print day.month
    MonthNum = day.month                                                    #MonthNum is the attribute of number of month
    DayOfMonthStart = day.day
    print DayOfMonthStart
                                                          #AggLevel is the attribtue of aggregation level

    #TODO write all CLU dbf files to txt file, the outputpath is fixed, so we can read the file without parameter
    #TODO according to every specific level to get the infomation, we should change here


    outputResPath = workingDir + "outputRes//"

    for clu in CLUResList:
        #here is to get the outputpath accroding to clu
        CLUOutputResPath = outputResPath + "CLU//"

        AggLevel = "CLU"

        State = clu[0:2]
        print State
        StateLowerCase = State
        State = State.upper()
        StateFIPS = us.states.lookup(State).fips
        print StateFIPS
        CountyFIPS = clu[-3:]
        print CountyFIPS

        #here is to change AggLevel to number
        # 1 2 3 4 5 state county district township CLU
        AggLevel = getAggre(AggLevel)

        # shapeSpecPath = workingDir + "CLU//" + county + "//" + county + CluNum + "//" + "clu_public_a_"+ county + CluNum +".shp"
        #this is to read the area attribtutes in the shape file
        shapeSpecPath = workingDir + "\\CLU\\" + StateLowerCase + "\\" + StateLowerCase + CountyFIPS + "\\" + "clu_public_a_"+ StateLowerCase + CountyFIPS +".shp"
        returnField = 'CALCACRES'
        areavalueList = [r[0] for r in arcpy.da.SearchCursor(shapeSpecPath, returnField)]

        outputResPath = workingDir + "outputRes//"
        outputSpecPath = outputResPath + "CLU//" + StateLowerCase + "//" + StateLowerCase + CountyFIPS

        #here is to read the dbf file from here
        dbfpath = outputSpecPath + "\\ZonalStUS.dbf"                            #dbfpath is to set the result dbf file that needed to get the computation

        #here is some file that can not be read
        try:
            org_db = dbf.Dbf(dbfpath, new = False)

            fieldnames = org_db.fieldNames

            AttFID= 'FID_'
            AttMEAN  = 'MEAN'
            i = 0                                                               #this is to match the area for sepcific CLU
            with open(outputfilePath, 'a') as outputfile:
                for rec in org_db:
                    CLUID = rec[AttFID]
                    valueMEAN = rec[AttMEAN]
                    AREA = areavalueList[i]
                    i = i + 1
                    writeData(outputfile,Year, DayofYearStart, DayofYearEnd, MonthNum, DayOfMonthStart, AggLevel, StateFIPS, CountyFIPS, AREA, CLUID, valueMEAN)
                outputfile.flush()                                                  #here is to force to write the file, otherwise the buffer will become used up quickly
                outputfile.close()
        except Exception as e:
            logging.error("can not read" + dbfpath)


    # #TODO write all couty dbf files to txt file, the outputpath is fixed, so we can read the file without parameter
    outputfilePath = workingDir + "output.txt"

    if not os.path.exists(outputfilePath):
        with open(outputfilePath, 'w') as outputfileCreat:
            outputfileCreat.close()

    #TODO get the essential information from the title
    #get the essential information from title
    #this part is to get essential information from the title, you should change here
    #TODO write all CLU dbf files to txt file, the outputpath is fixed, so we can read the file without parameter
    #TODO according to every specific level to get the infomation, we should change here


    outputResPath = workingDir + "outputRes\\"
    CLUOutputResPath = outputResPath + "County\\"
    AggLevel = "county"
    AggLevel = getAggre(AggLevel)
    # shapeSpecPath = workingDir + "CLU//" + county + "//" + county + CluNum + "//" + "clu_public_a_"+ county + CluNum +".shp"
    #this is to read the area attribtutes in the shape file
    shapeSpecPath = workingDir + "\\County\\"  + "tl_2015_us_county.shp"

    outputResPath = workingDir + "outputRes"
    outputSpecPath = outputResPath + "\\County" + "\\ZonalStUS.dbf"

    dbfpath = outputSpecPath                                                    #dbfpath is to set the result dbf file that needed to get the computation

        #here is some file that can not be read
    try:
        org_db = dbf.Dbf(dbfpath, new = False)

        fieldnames = org_db.fieldNames
        #
        print fieldnames

        AttFID= 'GEOID'
        AttMEAN  = 'MEAN'
        AttAREA = 'AREA'
        i = 0
        CLUID="0"                                                                   #this is to match the area for sepcific CLU
        with open(outputfilePath, 'a') as outputfile:
            for rec in org_db:
                FID = rec[AttFID]
                StateFIPS = FID[0:2]
                CountyFIPS = FID[-3:]
                valueMEAN = rec[AttMEAN]
                AREA = rec[AttAREA]
                i = i + 1
                writeData(outputfile,Year, DayofYearStart, DayofYearEnd, MonthNum, DayOfMonthStart, AggLevel, StateFIPS, CountyFIPS, AREA, CLUID, valueMEAN)
            outputfile.flush()                                                      #here is to force to write the file, otherwise the buffer will become used up quickly
            outputfile.close()
    except Exception as e:
        logging.error("can not read" + dbfpath)

    # #TODO write all state dbf files to txt file, the outputpath is fixed, so we can read the file without parameter
    # #the result may just one line
    # for state in StateResList:


def writeData(fdout,Year, DayofYearStart, DayofYearEnd, MonthNum, DayOfMonthStart, AggLevel, StateFIPS, CountyFIPS, AREA, CLUID, Value):
    fdout.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (Year, DayofYearStart, DayofYearEnd, MonthNum, DayOfMonthStart, AggLevel, StateFIPS, CountyFIPS, AREA,CLUID, Value) )


def getAggre(AggLevel):
    if AggLevel == "state":
        AggLevel = 1
    elif AggLevel == "county":
        AggLevel = 2
    elif(AggLevel == "district"):
        AggLevel = 3
    elif AggLevel == "township":
        AggLevel = 4
    elif AggLevel == "CLU":
        AggLevel = 5
    return AggLevel
