#This program prints out a random fruit

import random

fruits = ['Apple', 'Banana', 'Orange', 'Kiwi', 'Pear']

#generates random num between 0 and length of the list -1
index = random.randint(0, len(fruits)-1)
print ('A random fruit is', fruits[index])

moreFruit = ('Apricot', 'Mandarin', 'Grapes')

index2 = random.randint(0, len(moreFruit)-1)
print ('Another random fruit is',(moreFruit[index2]))
#print (moreFruit)