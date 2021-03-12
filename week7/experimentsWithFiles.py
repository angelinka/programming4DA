#Experimenting with files in lab7 
# Author: Angelina B

import os.path

filename = "count.txt"

def readFile():
    try:
        with open(filename) as f:
            count = int(f.read())
            return count
    except IOError:
        return 0


def writeFile(number):
    with open(filename, "wt") as f:
        f.write(str(number))

if not os.path.isfile(filename):
    print ("File does not exist")
    writeFile(0)

number = readFile()
number +=1
writeFile(number)
print ("The program has been run {} times.".format(number))