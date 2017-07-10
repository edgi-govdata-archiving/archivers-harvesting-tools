#Michael Craig
#November 7, 2016
#Script downloads hourly CEMS data for given years and states from FTP site:
#ftp://ftp.epa.gov/dmdnload/emissions/hourly/monthly/

from ftplib import FTP
import os, time, zipfile

######### SET PARAMETERS #######################################################
#Set key parameters
def setInputParameters():
    downloadFiles = True #whether to download CEMS files
    states= ['wa','or','ca','nv','ak','hi','id','mt','wy','ut','az','co','nm','ne','sd','nd',
    'mn','ia','ks','ok','tx','la','ar','mo','ms','al','ga','fl','sc','nc','tn','ky','il','wi',
    'mi','in','oh','pa','wv','va','md','de','nj','ny','ma','nh','me','vt','ri','ct'] #enter all states
    years = [yr for yr in range(1995,2017)] #data goes from 1995 - 2016
    rootCEMSDir = 'C:\\Users\\mtcraig\\Desktop\\EPP Research\\Databases\\CEMSDataBackup' #base directory where files are downloaded to
    dirToDownloadTo = os.path.join(rootCEMSDir,'ZipFiles')
    dirToExtractTo = os.path.join(rootCEMSDir,'CSVFiles')
    return (states,years,dirToDownloadTo,dirToExtractTo,downloadFiles)

#Set generic non-user-defined inputs
def setOtherParameters():
    ftpSite = 'ftp.epa.gov'
    baseDir = '/dmdnload/emissions/hourly/monthly/'
    return (ftpSite,baseDir)
################################################################################

######### MASTER FUNCTION #######################################################
def masterFunction():
    (states,years,dirToDownloadTo,dirToExtractTo,downloadFiles) = setInputParameters()
    (ftpSite,baseDir) = setOtherParameters()
    if downloadFiles==True: downloadCEMSData(states,years,dirToDownloadTo,ftpSite,baseDir)
    # extractCSVFiles(dirToExtractTo,dirToDownloadTo,years)
################################################################################

######### DOWNLOAD CEMS ZIP FILES #######################################################
#Download .zip files
def downloadCEMSData(states,years,dirToDownloadTo,ftpSite,baseDir):
    epaFtp = connectToFTP(ftpSite,baseDir)
    months = getMonthStrs()
    parentDir = epaFtp.pwd()
    for year in years:
        epaFtp.cwd(str(year) + '/')
        dirToSaveYr = os.path.join(dirToDownloadTo,str(year))
        if not os.path.exists(dirToSaveYr):
            os.makedirs(dirToSaveYr)
        for state in states:
            for month in months:
                currFile = str(year) + state + month + '.zip'
                ftpInput = 'RETR ' + currFile
                filenameToSave = os.path.join(dirToSaveYr,currFile)
                try:
                    with open(filenameToSave, 'wb') as fobj: 
                        epaFtp.retrbinary(ftpInput, fobj.write) 
                    print('Downloaded ' + currFile)
                except:
                    print("Could not download:\t" + currFile)
                time.sleep(2) #pause 2 seconds
            print('Finished state ' + state)
        print('Finished year ' + str(year))
        epaFtp.cwd(parentDir)
    print('Finished downloads')
    epaFtp.quit()

#Connect to FTP
def connectToFTP(ftpSite,baseDir):
    epaFtp = FTP(ftpSite)
    epaFtp.login()
    epaFtp.cwd(baseDir)
    return epaFtp 

#Create list of month suffixes on CEMS data files w/ leading zeros
def getMonthStrs():
    monthStrs = []
    for num in range(1,13):
        if num<10: monthStrs.append('0' + str(num))
        else: monthStrs.append(str(num))
    return monthStrs
################################################################################

######### EXTRACT .ZIP DATA INTO .CSV FILES ####################################
#Extract CSV files from zip files
def extractCSVFiles(dirToExtractTo,dirToDownloadTo,years):
    for year in years:
        dirToExtractToYr = os.path.join(dirToExtractTo,str(year))
        dirWithZipFiles = os.path.join(dirToDownloadTo,str(year))
        if not os.path.exists(dirToExtractToYr):
            os.makedirs(dirToExtractToYr)
        cemsZipFiles = os.listdir(dirWithZipFiles)
        for cemsZipFile in cemsZipFiles:
            fileExtension = os.path.splitext(cemsZipFile)[1]
            if fileExtension == '.zip': #make sure .zip file, otherwise skip
                try: 
                    cemsZipFileObj = zipfile.ZipFile(os.path.join(dirWithZipFiles,cemsZipFile))
                    cemsZipFileObj.extractall(dirToExtractToYr)
                except:
                    print('Bad zip file:\t' + cemsZipFile)
        print('Extracted ' + str(year))

################################################################################

masterFunction()