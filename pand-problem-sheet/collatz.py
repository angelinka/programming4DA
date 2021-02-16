# program asks the user to input any positive integer and outputs the following:
# calculate the next value by taking the current value and, 
# if it is even, divide it by two, but if it is odd, 
# multiply it by three and add one untill current value is one
#author: Angelina B

#Asking user to enter positive integer number
inputNum  = int(input('Please enter a positive integer: '))
#Creating a list and adding input number to it
lst = []
lst.append(inputNum)

#While input number is not equal to 1 performing the following:
while inputNum != 1:
    #if number is even, deviding it by two, add result to the list
    if (inputNum % 2) == 0:
        inputNum /= 2
        lst.append(int(inputNum))
    #else multiplying by three and adding one, add result to the list
    else:
        inputNum = (inputNum * 3) + 1
        lst.append(int(inputNum))

print (lst)
    

