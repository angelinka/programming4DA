# Program finds approximate square root of  a positive 
# floating-point number (entered by user) using Newton's method
#Author: Angelina Belotserkovskaya

# Calculation will be based on the following formula:
# root = 0.5 * (guess + (num/guess))
# where num - number of which we are trying to find a square root
# guess - number which we assume to be a square root of N
# credits to https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N.

def sqrt():
    num = float(input('Please enter a positive number to calculate square root: '))
    # we can decide how many iterations of the loop will be performed 
    # or ask the user for that number. Precision of the calculation will depend on it
    # but it also will affect how many computational resources are used and how long
    # the calcualtion will take.
    # In this progam we asking the user to decide on the number of iterations 
    iterations = int(input('Please enter number of iterations you would like to be performed: '))
    
    # Assume that the square root of input number equals that number
    guess = num
    # Calculating square root by using for loop based on user provided amount of iterations.
    for i in range(iterations):
        guess = 0.5 * (guess + (num/guess))
    print('The square root of {} is approx:'.format(num))    
    print(round(guess,2))

sqrt()