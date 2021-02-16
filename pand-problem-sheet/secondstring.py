#This program asks a user to input a string and outputs every second 
# letter in reverse order.

inpStr = input('Please enter a sentence: ')

#saving every second letter from the input string into secLetter variable
#secLetter = inpStr[1::2]

#reversing the string, example can be found below:
#  https://www.w3schools.com/python/python_howto_reverse_string.asp
#reverStr = secLetter[::-1]

#print (reverStr)

#shorter version:
secLetter = inpStr[1::2][::-1]
print(secLetter)