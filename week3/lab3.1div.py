#program reads input of two numbers and the integer and reminder of division
#author Angelina B

a = int(input('Please enter first number: '))
b = int(input('Please enter number you want to divide by: '))

answer = a//b
reminder = a%b

print('{} divided by {} is {} with remainder {}'.format(a,b, answer, reminder))