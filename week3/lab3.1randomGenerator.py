#program prints out a random number between 1 and 10

import random

x = random.randint(1,10)
print('here is a random number {}'.format(x))

a = int(input('Enter number that the range starts from: '))
b = int(input('Enter number that the range stops at: '))
print ('Your random number is ', random.randint(a,b))