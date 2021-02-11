# Program  prompts the user to guess a number and goves hints 
# if it's too high or too low
# until the user guesses correctly
#Author: Angelina B

import random

numToGuess = random.randint(1,100)
print (numToGuess)

guess = int(input('Please guess an integer between 1 and 100: '))

while guess != numToGuess:
    
    if guess < numToGuess:
        print ('Too low')
    
    else:
        print ('Too high')
    guess = int(input('Please try again: '))

print ('Well done! Yes the number was', numToGuess)