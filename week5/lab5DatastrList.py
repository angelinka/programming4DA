""" 
Create a program that puts 10 random numbers into a queue(list), the
program should then output all the values in the queue, then take the
numbers from the queue one at a time, print it and the current numbers still
in the queue 
"""
#Author: Angelina B
import random

queue = []
upTo = 1000

#generate random integer in range from 0 to 1000(upTo) and adds it to the list
for i in range (10):
    i = random.randint(0, upTo)
    queue.append(i)
print ('queue is', queue)

#removes first element from the list, prints it out and the rest of the list
for i in range(len(queue)):
    i = queue.pop(0)
    print ('current Number is', i, 'and the quesue is', queue)

print ('the queue is now empty')