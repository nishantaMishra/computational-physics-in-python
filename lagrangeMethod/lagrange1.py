#####################################################################
#####  Lagrange Interpolation Method for evaluation of values ######
####################################################################


# For user Input
x = []  
y = []  
print("Enter numerical values seperated by spaces.\n")
x = [float(item) for item in input("Enter the values of x : ").split()]
y = [float(item) for item in input("Enter the values of y : ").split()]
print('Values entered for x are', x)
print('Values entered for y are', y)
      

m = len(x) #length of array x
n = m-1
px = float(input("Enter the value of x for which y has to be calculated: "))
L = 0 #summation initialised from 0.
for i in range(n+1):
    pro = 1 #product is initialised from 1
    for j in range(n+1):
        if j != i:
            pro *= (px -x[j])/(x[i] - x[j])

    L += y[i]*pro 
print('For x = %.1f, y = %.1f'%(px,L))

#Lagrange2.py contains same problen with plot.

