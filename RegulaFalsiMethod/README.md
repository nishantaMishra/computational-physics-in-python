# Root Finding

## Regula Falsi Method
```math
x^{(k)} = x^{(k-1)} - \frac{x^{(k-1)} - x^{(k-2)}}{f(x^{(k-1))} - f(x^{(k-2)})} * f(x^{(k-1)}) \quad \quad k = 2, 3, 4, ...   \tag{$1$}
```

The  **regula falsi method** or **false position** is very similar to
the secant method. The diﬀerence is that regula falsi is a bracketing method, so it starts
with $x_0$ and $x_1$ such that $f(x_0) \times f(x_1) < 0$. Like the secant method, it then employs the
line that goes through the two points $(x_0, y_0)$ and $(x_1 , y_1)$, as per Eq. $(1)$, and then
finds the x axis intercept. The false-position method then ensures that it continues
to bracket the root.

---
### Algorithm
Following equation has been coded.
```math
x_{new} = x_2 - \frac{(x_2-x_1)}{y_2 - y_1} \times y_2
```
---
- [Code](https://github.com/nishantaMishra/computational-physics-in-python/blob/main/RegulaFalsiMethod/regulaFalsi1.py)
```python
#### Method of False Position ####

def RegulaFalsi(fn, x1, x2, tol=0.001, ilimit=100): #defining a function called RegulaFalsi.
    y1 = fn(x1)
    y2 = fn(x2)
    xh = 0
    ifalsepos = 0 # Counter of the number of false positions.
    if y1 == 0: xh = x1
    elif y2 == 0: xh = x2
    elif y1*y2 > 0:
        print('No roots of the equation exist within the given interval.')
    else:
        for ifalsepos in range(1, ilimit+1):
            xh = x2 - (x2-x1)/(y2-y1)*y2
            yh = fn(xh)
            if abs(yh) < tol:
                break
            elif y1*yh < 0:
                x2 = xh
                y2 = yh
            else:
                x1 = xh
                y1 = yh
    return xh, ifalsepos   # Function returns two values. 

def y(x): return 2*x**2 - 5*x + 3
x1 = float(input('Enter the value of x1: '))
x2 = float(input('Enter the value of x2: '))

x,n = RegulaFalsi(y, x1, x2, 0.0000001)  #calling the function and assigning x to the first return value and n to the second return value.

print('The root:%f' %x)
print('The number of computed false position: %d' %n)
```
