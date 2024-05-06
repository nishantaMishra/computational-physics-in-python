# Regression and Curve Fitting


### Polynomial curve fitting
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
```
