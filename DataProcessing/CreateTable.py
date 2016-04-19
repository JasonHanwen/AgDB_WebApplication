import pyodbc

sqlServerInstance = "AG-AEM-BCRQYQ1\MSSQLAGDEV"
#sqlServerInstance = "AG-AEM-1M9RBY1" #this way when it is not a SQL Server named instance)
schema="dbo" #schema for processed data
dbname="AgDB" #database name
sqltablename = "TestTable"                                                       #this is to set the tableName

connectionStr = "DRIVER={SQL Server};SERVER="+sqlServerInstance+";DATABASE="+dbname+";Trusted_Connection=Yes"
con = pyodbc.connect(connectionStr)
cur = con.cursor()

workingDir="C:\\Users\\hw544\\AgDB\\AgDBETL\\eMODIS\\"
#first I need to try to create a table in database

try:
    f = open(workingDir+"RefactorProgram\\sqlqueries\\" + "CreateEmodisTABLE.txt", 'r')
    query = " ".join(f.readlines())
    query ="Create Table ["+dbname+"].["+ schema +"].["+sqltablename+"]"+query
    cursor = con.cursor()
    cursor.execute(query)
    cursor.commit()
    print "Created table for CLU data storage "
    f.close

except pyodbc.ProgrammingError:
    print "there is a error"
    string = "DROP TABLE [dbo].[TestTable]"
    cur.execute(string)
    con.commit()

    f = open(workingDir+"RefactorProgram\\sqlqueries\\" + "CreateEmodisTABLE.txt", 'r')
    query = " ".join(f.readlines())
    query ="Create Table ["+dbname+"].["+ schema +"].["+sqltablename+"]"+query
    cursor = con.cursor()
    cursor.execute(query)
    cursor.commit()
    print "Created table for CLU data storage "
    f.close

# try:
#           cursor = conn.cursor()
#           query ="Create Table ["+dbname+"].["+ schema +"].["+sqltablename+"] [symbol] varchar(6), [price] double)"
#           cursor.execute(query)
#           cursor.commit()
