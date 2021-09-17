import os
import tempfile

print('Creating a temporary file:')
processID = str(os.getpid())        # get process id from sys
filename = processID+".txt" # create a file name with pid
tmp = open(filename, 'w')           # open as write file current tmp file
print('tmp file:', tmp)              # print info of the current tmp file
tmp.close()                         # close the file before leave
os.remove(filename)                 # clean up the tmp file explicity 
