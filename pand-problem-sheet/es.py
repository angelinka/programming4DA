#Program reads in a text file and outputs the number of e's it contains.
#Author: Angelina Belotserkovskaya

import os
import sys

#Reference to parcing arguments using sys
# https://stackoverflow.com/questions/7033987/python-get-files-from-command-line and
# https://realpython.com/python-command-line-arguments/#a-few-methods-for-parsing-python-command-line-arguments

#Getting  the last argument from the command line (which we assume is the name of the file)
#  and saving it into variable filename
filename = sys.argv[-1]

# print (filename) 

# checking if file exists and if not asking to check that file name is correct
if os.path.exists(filename):
    with open (filename, 'r') as f:  #opening the file for reading
        count = 0
        for line in f:  #iterating through each line and the each character in the file
            for letter in line:
                if letter == 'e':   #if letter "e" is found then adding 1 to count
                    count +=1
                #print ('found an e')
        print (count)
else:
    print("Can't locate file provided please check if file {} exists in the directory".format(filename))

  