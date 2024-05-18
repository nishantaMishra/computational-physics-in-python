# System of Linear Equations

A **Linear Equation** is an inequality of the form 

```math

\sum_{i=1}^n a_ix_i = y,
```

where, $a_i$ are scalars, and $x_i$ are unknown variables in Real space, and y is a scalar.

A **system of linear equations** is a set of linear equations that share the same variables. consider the following system of equations;
```math 
a_{1,1}x_1 + a_{1,2}x_2 +  a_{1,3}x_3  + ... + a_{1,n-1}x_{n-1} + a_{1,n}x_n  = y_1
```
```math
a_{2,1}x_1 + a_{2,2}x_2 +  a_{3,3}x_3  + ... + a_{2,n-1}x_{n-1} + a_{2,n}x_n  = y_2
```
```math
...
```
```math
a_{{m-1},1}x_1  +  a_{{m-1},2}x_2  +  a_{{m-1},3}x_3  + ... +  a_{{m-1},n-1}x_{n-1} + a_{{m-1},n}x_n  = y_{m-1}
```
```math
a_{{m},1}x_1 + a_{{m},2}x_2 +  a_{{m},3}x_3  + ... +  a_{{m},n-1}x_{n-1} + a_{{m},n}x_n  = y_{m}
```

where $a_{i,j}$ are real numbers. This system of linear equations can also be represented in matrix notation as:

```math
\begin{bmatrix} 
a_{1,1} & a_{1,1} & ... & a_{1,n}\\\ 
a_{2,1} & a_{2,2} & ... & a_{2,n}\\\
\vdots & \vdots & \ddots & \vdots\\\
a_{m,1} & a_{m,2} & ... & a_{m,n} \\\
\end{bmatrix}
\begin{bmatrix} 
x_1 \\\ x_2\\\ \vdots\\\ x_n\\\
\end{bmatrix}
= 
\begin{bmatrix} 
y_1\\\
y_2\\\
\vdots\\\
y_n\\\
\end{bmatrix}
```

