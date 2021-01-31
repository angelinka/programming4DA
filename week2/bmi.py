#This program calculates Body Mass Index (BMI)
#author: Angelina Belotserkovskaya

# Asks to input height in cm and saves it into variable 
# which is converted into int

height = int(input('Please enter your height in centimetres: '))

# Convert cm to m2
height = (height**2) / 10000

# Asks to input weight in kg and saves it into variable 
# which is converted into int

weight = int(input('Please enter your weight in kg: '))


# Calculating bmi
bmi = weight/height
print ('Your BMI is {:.2f}'.format(bmi))