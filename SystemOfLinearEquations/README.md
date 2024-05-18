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

where $a_{i,j}$ are real numbers. This system of linear equations can also be represented in matrix notation as $AX = Y$:

```math
\begin{bmatrix} 
a_{1,1} & a_{1,1} & ... & a_{1,n}\\\ a_{2,1} & a_{2,2} & ... & a_{2,n}\\\ \vdots & \vdots & \ddots & \vdots\\\ a_{m,1} & a_{m,2} & ... & a_{m,n} \\\
\end{bmatrix}
\begin{bmatrix} 
x_1 \\\ x_2 \\\ \vdots\\\ x_n\\\
\end{bmatrix}
= 
\begin{bmatrix} 
y_1 \\\ y_2 \\\ \vdots\\\ y_n\\\
\end{bmatrix}
```
If we carry out the matrix multiplication, we will see that we arrive back at the original system of equations.

## Solution of system of Linear Equations.
Consider a system of linear equations in matrix form, Ax = y, where A is an m × n matrix. Recall that
this means there are m equations and n unknowns in our system. A solution to this system of linear
equations is an x in Real space that satisfies the matrix form equation. Depending on the values that populate
A and y, there are three distinct possible solutions for x. Either there is no solution for x, or there is
one unique solution for x, or there are infinitely many solutions for x. This fact is not shown in this
text.


> **NOTE**

It works with almost all markdown flavours (the below blank line matters).

---
