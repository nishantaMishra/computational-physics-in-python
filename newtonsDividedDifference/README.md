# Interpolation

## Newton's Interpolation (Divided differences)
If we have a set of value pairs (x values and corresponding y values)
| $x_1$ | $x_2$ | $x_3$ | $x_4$ | $x_5$ | 
| ---   | :---:    |  :---:   | :---:  | :---:    |    
| $y_1$ | $y_2$ | $y_3$ | $y_4$ | $y_5$ | 

then
Newton's method can give the value of function at any given point as
```math
y(x) = a_0 + a_1(x - x_1) + a_2 (x - x_1) (x - x_2) + ... + a_n (x - x_1)(x - x_1) ...(x - x_n) 
```
This can be done in two steps
1. The divided differences procedure to calculate the coefficients of the ploynomial, i.e. coefficient a(s) in above expression.
2. The substitution of values of $x_i$ from the value pairs and the given x to the above polynomial to get interpolated y.

Following is the divided difference table.
|   $x$   |    $y$    |    $\Delta y$    |   3   |   4   |
| ---   | :---:    |  :---:   | :---:  | :---:    |    
| $x_1$ | $y_1^{(1)}$ |     |       |      | 
| $x_2$ | $y_2^{(1)}$  | $y_2^{(2)}$ |   |    |
| $x_3$ | $y_3^{(1)}$  | $y_3^{(2)}$ | $y_3^{(3)}$ | |
| $x_4$ | $y_4^{(1)}$  | $y_4^{(2)}$ | $y_4^{(3)}$ | $y_4^{(4)}$|
| $x_5$ | $y_5^{(1)}$  | $y_5^{(2)}$ | $y_5^{(3)}$| $y_5^{(4)}$|

The General formula for the divided difference is 
