# program reads in a students percentage mark and
# prints out corresponding grade
#author Angelina B

persantage = round(float(input('Please enter the percentage: ')))

if persantage < 0 or persantage > 100:
    print ('Persentage should be between 0 and 100')
elif persantage < 40:
    print ('Fail')
elif persantage < 50:
    print ('Pass')
elif persantage < 60:
    print ('Merit 2')
elif persantage < 70:
    print ('Merit 1')
else:
    print ('Destinction')