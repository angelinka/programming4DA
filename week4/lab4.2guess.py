# Program  prompts the user to guess a number, 
# until the user guesses correctly
#Author: Angelina B

numToGuess = 15

guess = int(input('Please guess an integer between 1 and 100: '))

while guess != numToGuess:
    
    print ('Wrong')
    hint = input('Would you like a hint? y/n: ')
    if hint == 'y':
        print ('The number is devisible by 5')
        guess = int(input('Give it another try: '))
    else:
        guess = int(input('Please try again: '))


print ('Well done! Yes the number was', numToGuess)