#####################################################
#####  Linear Regression by making logic  #######
#################################################
"""
Find equation of the line that fits the data
x = [2, 5, 4.3, 5.3, 6, 7]
y = [1, 6, 17, 23, 30, 42]
"""

x = [2, 5, 4.3, 5.3, 6, 7]
y = [1, 6, 17, 23, 30, 42]
n = len(x)

sumx = sumxy = sumx2 = sumy = 0
for i in range(n):
    sumx += x[i]
    sumx2 += x[i]**2
    sumxy += x[i]*y[i]
    sumy += y[i]
xmean = sumx/n
ymean = sumy/n

a = (ymean*sumx2 - xmean*sumxy)/(sumx2 - n*xmean**2)
b = (sumxy - xmean*sumy)/(sumx2 - n*xmean**2)
print('The straight line equation that fits the data is: ')
print('y = (%.3f) + (%.3f)x' % (a,b))
