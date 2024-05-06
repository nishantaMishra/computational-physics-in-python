#########################################################
#####  Linear Regression by using Python functions  #####
#########################################################
"""
Find equation of the line that fits the data
x = [2, 5, 4.3, 5.3, 6, 7]
y = [1, 6, 17, 23, 30, 42]
"""
import numpy as np 
x = np.array([2, 5, 4.3, 5.3, 6, 7],float)
y = np.array([1, 6, 17, 23, 30, 42],float)
n = len(x)

a = (np.mean(y)*np.sum(x**2)-np.mean(x)*np.sum(x*y))/(np.sum(x**2)-n*np.mean(x)**2);
b = (np.sum(x*y)-np.mean(x)*np.sum(y))/(np.sum(x**2)-n*np.mean(x)**2)

print('The straight line equation that fits the data is: \n y = (%.2f) + (%.2f)x' % (a,b))
