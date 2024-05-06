# Interpolation

## Polynomial by interpolation

If we have a set of value pairs (x values and corresponding y values)
| $x_1$ | $x_2$ | $x_3$ | $x_4$ | $x_5$ | 
| ---   | :---:    |  :---:   | :---:  | :---:    |    
| $y_1$ | $y_2$ | $y_3$ | $y_4$ | $y_5$ | 

then it is possible to obtain a polynomial function $f(x)$ that represents the given data set. This can be done by using polynomial. If we solve an interpolation equation for the variable(and not for a fixed point) then, we will get a polynomial function instead of a fixed numerical value.

[This code](lagPolynomial.py) will give polynomial according to the Lagrange's interpolation formula.

**Usage** : The program first asks the user to enter number of data points i.e. how many value pairs does he have, then user is supposed to enter all the values of x and all the values of y. After typing every value user should press enter to proceed.

### Example

```bash
└─# python3 polynomial.py
Enter number of data points: 5
Enter values of x:
x[0]1
x[1]2
x[2]3
x[3]4
x[4]5
Enter values of y:
y[0]5
y[1]4
y[2]3
y[3]2
y[4]1
~~~~~~~~~~~~~~~~~~~~~~~~~~

Polynomial according to lagrange interpolation is:
 5.55111512312578e-17*u**4 + 7.105427357601e-15*u**2 - 1.0*u + 6.0
```
