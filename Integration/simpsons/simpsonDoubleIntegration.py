###############################################################
####   Double Integration using Simpson's 1/3 Rule    #####
##############################################################


""" 
Performing the following integration:-
\begin{equation*}
    I = \int_{-1}^{1} \int_{1}^{2} \big(x^2y + xy^2) dxdy 
\end{equation*}
"""
f = lambda x,y: x**2 * y + x * y**2
ax = 1
bx = 2
ay = -1
by = 1
nx = 10 
ny = 10
hx = (bx-ax)/nx
hy = (by-ay)/ny
sum = 0 
for i in range(0, ny+1):
    if i == 0 or i == ny:
        p = 1
    elif i % 2 == 1:
        p = 4
    else:
        p = 2
    for j in range(0, nx+1):
        if j == 0 or j == nx:
            q = 1
        elif j % 2 == 1:
            q = 4
        else:
            q = 2
        sum += p*q * f(ax + j*hx, ay + i*hy)
Integral = hx*hy/9 * sum
print('Integral = %f' % Integral)