#Author: Angelina B
import matplotlib.pyplot as plt
import numpy as np 

numbers = 10
minSalary = 20000
maxSalary = 80000
minAge = 21
maxAge = 65

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numbers)
ages = np.random.randint(minAge, maxAge, numbers)

plt.scatter(ages, salaries, label = 'salaries')

#Adding a line to this plot that shows y= x2 
xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color = 'pink', label = 'x squared')
plt.legend()
plt.title('Random salaries')
plt.xlabel('age')
plt.ylabel('salaries')
plt.show()

#plt.savefig('prettier-plot.png')