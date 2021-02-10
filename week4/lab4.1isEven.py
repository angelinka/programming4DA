#program asks the user to enter in a number, and the
# program tells the user if the number is even or odd.
#author: Angelina B

num = int(input('Please enter an integer or type -1 to quit: '))

while num != -1:
    if (num % 2) == 0:
        print(num, 'is even')
        num = int(input('Please enter an integer or type -1 to quit: '))
    else:
        print(num, 'is odd')
        num = int(input('Please enter an integer or type -1 to quit: '))