# Regression and Curve Fitting


## Polynomial curve fitting
Concept of Polynomial curve fitting is similar to linear curve fitting. A straight might not be the ideal representative of the data under consideration. Then some polynomial curve might be a good choice,

The polynomial has the form, 
```math
f(x) = a_0 + a_1x + a_2x^2 + ... + a_nx^n
```
If a set of data containing m points is to be fitted by the polynomial curve of degree n, a system of linear equations is formulated to compute values of the coefficients
```math
[A]\{a\} = \{B\}
```
Where, A is a matrix and a and B are vectors.
```math
\begin{bmatrix}
m & \sum x_i & \sum x_i^2 & ... & \sum x_i^n\\
\sum x_i & \sum x_i^2 & \sum x_i^3 & ... & \sum x_i^{n+1}\\
\vdots  & \vdots & \vdots & \vdots & \vdots\\
\sum x_i^n & \sum x_i^{n+1} & \sum x_i^{n+2} & ... & \sum x_i^{2n}\\
\end{bmatrix}

and \quad \quad
\begin{align}
    B &= \begin{bmatrix}
           \sum y_{i} \\
           \sum x_{i}y_i \\
           \vdots \\
           \sum x_{i}^n y_i
         \end{bmatrix}
\end{align}

\tag{$1$}
```
in the above matrices $\sum = \sum_{i=1}^m$. 
(1) is a system of linear equations. Here, our task can be realised in two steps. First, to calculate all the coefficients and then solve the system using a linear system solving technique like Gauss-Elimination Method.

### Codes
- [polynomialfit1.py](https://github.com/nishantaMishra/computational-physics-in-python/blob/main/curveFitting/polynomialCurveFitting/polynomialfit1.py) : Non-interactive program. Data to be solved is hard-coded in it.

- [polynomialfit2.py](https://github.com/nishantaMishra/computational-physics-in-python/blob/main/curveFitting/polynomialCurveFitting/polynomialfit2.py) : This is an interactive code, it asks user to enter number of value pairs (x values and corresponding y values) and degree of polynomial to fit.
```bash
└─# python3 polynomialfit2.py
Enter the number of points: 4
x[0]: 0
x[1]: 1
x[2]: 2
x[3]: 3
y[0]: 2
y[1]: 8
y[2]: 14
y[3]: 28
Enter degree of polnomial to fit 
 2 for quadratic 	 3 for cubic
Degree of polynomial: 2
f(x) = 	 2.400000
	 +2.400000 x^1
	 +2.000000 x^2
```

- [polynomialfit3.py](polynomialfit3.py) : This uses functions of Scipy for solving the equations.
