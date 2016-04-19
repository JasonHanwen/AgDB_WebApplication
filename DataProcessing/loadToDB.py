#this is to load the outputfile.txt to the database
import os
#parameter
def main(workingDir,db,targetTable,sqlServerInstance):

    #this is to set the output file name and path
    outPutFile = workingDir + "output.txt"
    # db="AgDB" #database name
    # targetTable = db +".dbo.TestTable" #this is load data table name
    # sqlServerInstance = "AG-AEM-BCRQYQ1\MSSQLAGDEV"
    os.system('bcp '+ targetTable + ' in ' + outPutFile + ' -c -T -b250000  -S' + sqlServerInstance)
