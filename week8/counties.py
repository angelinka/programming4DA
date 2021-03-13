# program that has a list of counties (5), some counties appear more than others
# program displays pie chart of the counties
#Author: Angelina B

import matplotlib.pyplot as plt
import numpy as np 

someCounties = ['Kerry', 'Ulster', 'Galway', 'Kildare', 'Sligo']

counties = np.random.choice(someCounties, 
            p=[0.4, 0.1, 0.2, 0.1, 0.2], size = (100))

#print (counties)

countyName, count = np.unique(counties, return_counts=True)

#plt.pie(count, labels= countyName)
plt.bar(countyName, count)
plt.show()

# print (countyName, count)

