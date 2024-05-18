# Numerical integration

## Trapezoidal rule

Problem of numerical integration is to approximate the integral of $f(x)$ over the total interval $[a, b]$. To accomplish this goal, we assume that the interval has been divided into a numeral grid, x, consisting of $n+1$ points with spacing, $h = \frac{b-a}{n}$. 
Denoting all the points in $x$ by $x_i$, where $x+0 = a$ and $x_n = b$. Note that there are n+1 grid points because the count starts at $x_0$. 
[<img src="figure1.png" width="250"/>](figure1.png) 
The **Trapezoidal Rule** estimates the integral of a function $f(x)$ over an interval $[a,b]$ by approximating the region under the curve as a series of trapezoids rather than using the actual curve. The area of each trapezoid is then summed to give the approximate value of the integral. This approximation of the integral to an arbitrary function is shown in Fig. 1.


[<img src="figure2.png" width="250"/>](figure2.png) 
```math 
\text{area of trapezium} = \frac{\text{sum of both bases}}{2} \text{height} 
```
Now for each sub-interval, the trapezoid rule computes the area of a trapezoid with corners at $(x_i, 0), (X_{i+1}, 0), (x_i, f(x_i))$, and $(x_{i+1}, f(x_{i+1}))$ , which is $h\frac{f(x_i) + f(x_{i+1})}{2}$

Thus, trapezoid rule approximates integrals according to the expression
```math
\int_a^b f(x) dx \approx \sum_{i=0}^{i=n-1} h \frac{f(x_i) + f(x_{i+1})}{2}   \tag{$1$} 
```
But the expression 1 is not perfect,  it "double counts" most of the terms in the series. To illustrate this fact, consider the expansion of the trapezoidal rule:
```math
\sum_{i=0}^{i=n-1} h \frac{f(x_i) + f(x_{i+1})}{2} = \frac{h}{2} \left[ (f(x_0) + f(x_1)) + (f(x_1) + f(x_2)) + (f(x_2) + f(x_3)) + ... + (f(x_{n-1}) + f(x_n)) \right]
```
Computationally, this is many extra additions and calls to $f(x)$ than are really necessary. We can be made more computationally efficient using the following expression:
```math
\int_a^b f(x) dx \approx \frac{h}{2}  \left(  f(x_0) + 2 \sum_{i=1}^{n-1} f(x_i) + f(x_n) \right)   \tag{$2$} 
```
This expression 2 is the expression that we shall use for estimating value of integrals.

This expression can also be expressed in terms of $a$ and $b$
```math
\int_a^b f(x) dx \approx \frac{b-a}{2n}  \left(  f(a) + 2 \sum_{i=1}^{n-1} f(a + ih) + f(b) \right) 
```
