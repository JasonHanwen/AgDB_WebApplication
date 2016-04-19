The file that needed to have under workingDir:
1 CLUZip file with all downloaded CLU Zip files here, the subdirectory should be in county state level
2 CountyZip file with tl_2015_us_county.zip file here
3 then County file here with all unzip files here, for example  tl_2015_us_county.shp, so that the files can read the file here.
4 also I need to have 7z 
5 I need to have a bda_windows_1_2. I'm not sure whether or not I need to have it


Things need to change
1 the working dir, make sure working dir has the directories that I have mentioned above
2 the dbname and the table name abd database instance so that The connected to the write database

Things need to pay attention:
1 if you run the program first time, you need to run CLUlist = unZipCLU.main(workingDir), instead of CLUlist = getCLUList.main(workingDir)


The function that needs to change in order to generalize
1 unZipCLU                    This is to unzip all CLU files so make sure [The file I need to have(1)]
2 getAllURLS		      This is to download all URLS that need to be downloaded, to get the layers	
3 downloadOneURL	      This is to download on layer from specific URL
4 getTitle		      This is to get the title name to do computation for the next step
5 computeMean		      This is to do some computation that will be loaded to the database				
6 turnDbfToTxt		      This is to write the data in the dbf file to the txt file so that the data can be loaed to the database 
7 loadToDB		      This is to load the data in the dbf file to the database
8 deleteTemFile		      This is to delete the temperory file so that there will not be temperory files in the directories.
9 deleteFile		      This is to download all the files that in the direcotories, so that free the disk, and make sure the there is now files in the directory

The things You need to make some change in the program:
2 getAllURLS
3 downloadOneURL
4 getTitle
5 computeMean
6 turnDbfToTxt
7 loadToDB

Maybe you need to change some files in the directory


Author: Hanwen Wang
Last updated : 2015/11/15