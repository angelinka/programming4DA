# Program  keeps reading numbers until the user 
# enters a 0. Then program print out each of the numbers entered
#  and the average of them
#Author: Angelina B

#Creating empty list
numbers = []

num = int(input('enter number (0 to quit): '))
#while number isn't 0, adding it to the list
while num != 0:
    numbers.append(num)
    #asking for new number
    num = int(input('enter another (0 to quit): '))
#printing all numbers in the list
for num in numbers:
    print (num)

average = float(sum(numbers) / len(numbers))
print ('The average is:', average)