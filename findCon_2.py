import os
import shutil
'''
 * To use:
 At ipython prompt (one method);
 In [1]: from findCon import *

 In [2]: fc()
 We had to check for files for 83 dates.
 We found 0 constrictor files present.
 We have 83 constrictor files absent, UA.
 Carry on.

 * Requires : Input list of dates to search for
 in format YYYY-MM-DD. This file name is in the code
 below with an open statment.

 * Output : Two output ASSCI text files files
 Output a) contains files found = presentFiles.txt
 Output b) contains files NOT found = absentFiles.txt

 * Test : Use input file test_fc_files.txt and this will return
   Three (3) files found
   Four (4) files not found

   Present                  Absent
   -------                  ------
   1997-06-02               1999-07-03
   2000-06-25               2001-05-19
   2011-05-17               2001-05-25
                            2012-09-03

'''

def fc():
    '''
    Check for presence of constrictor files usually requested via a list
    from Brian Mason for WDS program observations.
    
    Takes the input ASCII text file of dates, adds 'con.gz' to the 
    end and does a search for these files using os module's walk 
    method.
    
    Any files found are copied to constrictor/parkIt for eventually 
    archving in to a tarball and sending on to the requestor.
    '''

    # open and read in list of files:
    # fi = open('missing.txt','r')
    # inFile = 'test_fc_files.txt'
    inFile = 'bob_list5.2025-Aug.txt'
    fi = open(inFile,'r')
    lines = fi.readlines()
    fi.close()

    # Get ready to use os.walk to search all directories
    current_path = os.getcwd()
    # Set path to parkIt for taring
    parkItPath = '/mnt/nofs/projects/NPOI/data/wasp1/constrictor/parkIt'
    
    # Open files to write the names of found and missing 
    # files. And start counters to track numbers of present 
    # and absent files
    presentFiles = open('presentFiles.txt','w')
    # absentFiles = open('absentFiles.txt','w')
    presentCount = 0
    absentCount = 0

    # Loop through list and check for files
    # All confiles are gzipped. 

    for line in lines:
        entries = line.split()[0]
        aFile=line.split()[0]+'.con.gz'
        for dirpath, dirnames, filenames in os.walk(current_path): 
            for filename in filenames:
                if filename == aFile:
                    presentFiles.write(aFile+'\n')
                    presentCount+=1
                    print(f"Found fille: {aFile}")
                    shutil.copyfile(dirpath+'/'+filename, parkItPath+'/'+filename)
        
    # close the output files
    presentFiles.close()
    
    absentCount = len(lines) - presentCount

    # Report!
    print('We had to check for files for '+str(len(lines))+' dates.')
    print(f"Input file search list is: {inFile}\n")
    print('We found '+str(presentCount)+' constrictor files present.')
    print('We have '+str(absentCount)+' constrictor files absent, UA.')
    print('Any files found were sopied to ../constrictor/parkIt ')
    print('Carry on.')


    
