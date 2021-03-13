#Author: Angelina B
import matplotlib.pyplot as plt
import numpy as np 

numbers = 10
minSalary = 20000
maxSalary = 80000

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numbers)

'''
highSalaries = salaries + 5000
salariesMult = salaries * 1.05
newSalaries = salariesMult.astype(int)
print(newSalaries)
'''
plt.hist(salaries)
plt.show()