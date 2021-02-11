#program generates 10 random numbers (0-100) ,
# prints them out then prints out the top three.
#Author: Angelina B

import random

numbers = []

#Adding 10 random int numbers to the list
for i in range (0,10):
    n = random.randint(0,100)
    numbers.append(n)

print("10 random numbers:", numbers)
#sorting in reverse order https://www.w3schools.com/python/python_lists_sort.asp
numbers.sort(reverse = True)
#Printing first 3 items of the sorted list
print ("The top 3 are ", numbers[:3])
