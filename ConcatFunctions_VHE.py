# ========== Concat Functions ======================= 
import pandas as pd
import re
import os

from IPython.display import display
from ipywidgets import widgets

import time

def NameIsValid(filename): #checks if user defined out file name is valid: returns boolean
    patterns=re.compile("[:/\\\<>?*\\|\"]")
    if patterns.search(filename):
        return False
    else:
        return True    


# I've hardcoded the parameters here because this function is only used once, and it always uses the same parameters
def UserInfoFile(user, date, name, notes):

    f = open('Session_Information.txt', 'w')
    f.write('User Name: ' + user + '\n')
    f.write('Session Date (YYYY/MM/DD): ' + str(date.year) + '/' + str(date.month) + '/' + str(date.day) + '\n')
    f.write('Project Name: ' + name + '\n')
    f.write('Project Notes: ' + notes + '\n')
    f.close()

    return


def ConcatIfMatch(user, date, notes, projectname, inputfile, outputfilepath, outputfiletype):
                                #concats and outputs file type with predetermined file name if name is appropriate: returns output file
                                #converts input filetype to dataframe: returns dataframe array of input data
                                #checks for matching headers: returns boolean
                                #widget to prompt out file name: returns user defined out file name. If none, returns auto generated file name
    global FinalFileName
    
    #b=[]
    matchTF = []
    b_col = []
    
    minCONCAT = 0
    if outputfiletype == '.csv':
        maxCONCAT = len(inputfile.files)
    elif outputfiletype == '.xlsx':
        maxCONCAT = 37
        
    global progressbarCONCAT
    
    progressbarCONCAT = widgets.FloatProgress(min = minCONCAT, max=maxCONCAT, 
                                        description = 'Concatenating files',
                                        style = {'description_width':'initial'}
                                        )
    display(progressbarCONCAT)
    stepup = 0
    progressbarCONCAT.value = 0
        
    global inputfile_df
    inputfile_df = pd.read_csv(inputfile.files[0], sep=',')  # loads data from csv to dataframe
                       # note: I removed the append feature so you can only upload 1 file at a time
   
    # I commented this out simply because it ran an IndexError but I realize this workflow doesn't really need
    # the failsafe given the application will likely not be for multiple file upload applications
        #b_col.append(b[n].columns) #creates an array of column names of b : b_col 
        #matchTF.append(pd.Index.equals(b_col[0], b_col[n])) #compares if ALL column names match
        
        #variable for loading bar
    if outputfiletype == '.csv':
        stepup += 1
        progressbarCONCAT.value += 1

    elif outputfiletype == '.xlsx':
        for n in range (minCONCAT, maxCONCAT):
            stepup += 1
            progressbarCONCAT.value += 1
            time.sleep(1)

    FinalFileName = projectname + '_output_file' + outputfiletype 
    
    if NameIsValid(FinalFileName) is True:
        # given the single file upload nature, this line has also been commented out
        #fout6 = pd.concat(b)

        #write into seperate function later
        selDirectory = outputfilepath
        newFolderInDir = projectname
        newDirectory = selDirectory + '//' + newFolderInDir
        os.mkdir(newDirectory)
        os.chdir(newDirectory)

        #calling shortened function for session information function, to create .txt file w user info
        UserInfoFile(user, date, projectname, notes)

        if outputfiletype == '.xlsx':
            writer = pd.ExcelWriter(FinalFileName, engine='xlsxwriter')
            writer.save()
        elif outputfiletype == '.csv':
            inputfile_csv = inputfile_df.to_csv(FinalFileName)
        else:
            # this is more of a courtesy than anything; the default is set to csv
            # and due to the nature of radio buttons, it's impossible NOT to select
            # an output file type option.
            print("Output File Type Error: Missing Output File Type Selection.")
        if all(matchTF) is False:
            print('File input header warning: headers do not match')
    elif NameIsValid(FinalFileName) is False:
        print('File name error: invalid file name')
        print('Special Characters ( : / \ " | < > ? * ) not allowed!')
    
    progressbarCONCAT.close()
    
    return

def InNameConcatReturn():
    return FinalFileName