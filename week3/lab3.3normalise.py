#Program reads a string and strips any leading or trailing spaces and 
#converts the string to lower case. It also outputs the length of of 
# the input and output strings.

inputStr = input('Please enter a sting:')
resultStr = inputStr.strip().lower()
#lowStr = stripStr.lower()

print('That String normalised is:', resultStr)

print('we reduced the input string from {} to {} characters'
.format(len(inputStr), len(resultStr)))