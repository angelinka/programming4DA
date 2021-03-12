

# import Python's datetime module

from datetime import date

# get today's date, reference:
# https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
todayDate = date.today()
# print(todayDate) - used for testing

#find the number of the day, method .weekday()returns a number 
# between 0 and 7 
#https://www.hellocodeclub.com/python-get-day-of-week/
dayOfWeek = todayDate.weekday()
#print (dayOfWeek) - used for testing

#if dayOfWeek equals 5 or 6 it means it Sat or Sun - weekend,
#else it's a week day
if dayOfWeek == 5 or dayOfWeek == 6:
    print ('It is the weekend, yay!')
else:
    print('Yes, unfortunately today is a weekday.')