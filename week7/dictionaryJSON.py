#Experimenting with JSON
# Author: Angelina B

import json

filename = "dict.json"
sample = dict(name = 'john', age = 23, grade = [35, 64, 52])

def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)

# writeDict(sample)

def readDict():
    with open(filename) as f:
        return json.load(f)

testDict = readDict()
print (testDict)