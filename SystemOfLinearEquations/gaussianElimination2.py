#########################################################
####  Gaussian Elimination Method (Zero element fix)    ##### 
########################################################
""" If some of the elements are zero in our matrix then
python interpreter starts throwing error message. It is
fixed like below """

from numpy import array, zeros

a = array([
    [2, 7, -1, 3, 1],
    [2, 3, 4, 1, 7],
    [6, 2, -3, 2, -1],
    [2, 1, 2, -1, 2],
    [3, 4, 1, -2, 1]],float)

b = array([5,7,2,3,4],float)
n = len(b)
x = zeros(n,float)

#Elimination
for k in range(n-1):
    if a[k,k] == 0: # if diagonal element is detected zero. interchange it with next column
        for j in range(n):
            a[k,j]=a[k+1,j] = a[k,j]=a[k+1,j] 
    for i in range(k+1,n): #for every row k this starts from the row below it
        if a[i,k] == 0: continue # if element is already zero, skip elimination algorithm.
        fctr = a[k,k]/a[i,k]
        b[i] = b[k] - fctr*b[i]
        for j in range(k,n):
            a[i,j] = a[k,j] - fctr*a[i,j]

#Back Substitution
x[n-1] = b[n-1]/a[n-1,n-1]
for i in range(n-2,-1,-1): #from n-2 to 0(called -1 here because last element is not included), 
    terms = 0
    for j in range(i+1,n):
        terms += a[i, j]*x[j]
        x[i] = (b[i] - terms)/a[i,i]
print('The Solution is:')
print(x)
