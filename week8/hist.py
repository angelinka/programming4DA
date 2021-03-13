import numpy as np 
import matplotlib.pyplot as plt 

'''
#np.random.seed(1)

normalData = np.random.normal(size = 10000)

plt.hist(normalData)
plt.show()
'''

fruit = np.array(['Apples', 'Orange', 'Pear', 'Kiwi'])
numbers = np.array([35,72, 17, 48])

plt.pie(numbers, labels = fruit)
plt.legend()
plt.show()