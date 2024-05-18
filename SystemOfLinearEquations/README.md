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
a_{2,1}x_1 + a_{2,2}x_2 +  a_{2,3}x_3  + ... + a_{2,n-1}x_{n-1} + a_{2,n}x_n  = y_2
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
a_{1,1} & a_{1,2} & ... & a_{1,n}\\\ a_{2,1} & a_{2,2} & ... & a_{2,n}\\\ \vdots & \vdots & \ddots & \vdots\\\ a_{m,1} & a_{m,2} & ... & a_{m,n} \\\
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


> **Case#1: No Solution Exists**
If rank([A, y]) = rank(A) + 1 then y is linearly independent
from the columns of A. Therefore, because y is not in the range of A, by definition there cannot
be an x that satisfies the equation. Thus, comparing rank([A, y]) and rank(A) provides an easy
way to check if there are no solutions to a system of linear equations.

> **Case#2: There is a unique solution**
If $rank([A, y]) = rank(A)$, then y can be written as a
linear combination of the columns of $A$, and there is at least one solution for the matrix equation.
For there to be only one solution, $rank(A) = n$ must also be true. In other words, the number of
equations must be exactly equal to the number of unknowns. To see why this property results in a
unique solution, consider the following three relationships between $m$ and $n$ : $m < n, m = n$, and
$m > n$.
- For the case $m < n$, $rank(A) = n$ cannot possibly be true because this means we have a “fat”
matrix with fewer equations than unknowns. Thus, we do not need to consider this subcase.
- When $m = n$ and $rank(A) = n$, $A$ is square and invertible. Since the inverse of a matrix is
unique, the matrix equation $Ax = y$ can be solved by multiplying each side of the equation on
the left by $A^{−1}$ . This results in $A^{−1} Ax = A^{−1} y \longrightarrow I x = A−1 y \longrightarrow x = A^{-1} y, which gives the
unique solution to the equation.
- If $m > n$, then there are more equations than unknowns; however, if $rank(A) = n$, then it is
possible to choose n equations (i.e., rows of $A$) such that if these equations are satisfied, then
the remaining $m − n$ equations will also be satisfied. In other words, they are redundant. If the
m − n redundant equations are removed from the system, then the resulting system has an A
matrix that is $n \times n$ and invertible. These facts are not proven in this text. The new system then
has a unique solution, which is valid for the whole system.

> **Case#3: There are infinitely many solutions**
If $rank([A, y]) = rank(A)$, then y is in the
range of A, and there is at least one solution for the matrix equation; however, if $rank(A) < n$,
then there are infinitely many solutions. Although it is not shown here, if $rank(A) < n$, then there
is at least one nonzero vector, $n$, that is in the null space of $A$ (Actually, there are infinitely
many null space vectors under these conditions.). If $n$ is in the nullspace of $A$, then $An = 0$ by
definition. Now if $x^∗$ is a solution to the matrix equation $Ax = y$, then, necessarily, $Ax^∗ = y$;
however, $Ax^∗ + An = y$ or $A(x^∗ + n) = y$. Therefore, $x^∗ + n$ is also a solution for $Ax = y$. In
fact, since $A$ is a linear transformation, $x^∗ + \alpha n$ is a solution for any real number $\alpha$ (you should
try to show this on your own). Since there are infinitely many acceptable values for $\alpha$, there are
infinitely many solutions for the matrix equation.


Practically only the second case, that is the existence of unique solution is of our interest. We will see how to solve them in python using the 
following methods.

- [Gauss Elimination Method]
- [Diagonal Dominance]
- [Jacobi's Method]
- [Gauss-Seidel's Method]
- [Gauss-Jordan Method]

## Gauss Elimination Method
The Gauss elimination method is a procedure that turns the matrix A into an upper-triangular form
to solve the system of equations. Let us use a system of four equations and four variables to illustrate
the idea. Gauss elimination essentially turns the system of equations into

```math
\begin{bmatrix} 
a_{1,1} & a_{1,2} & a_{1,3} & a_{1,4}\\\ 0 & a'_{2,2} & a'_{2,3} & a'_{2,4}\\\ 0 & 0 & a'_{3,3} & a'_{3,4}\\\ 0 & 0 & 0 & a'_{4,4}\\\
\end{bmatrix}
\begin{bmatrix} 
x_1 \\\ x_2 \\\ x_3\\\ x_4\\\
\end{bmatrix}
= 
\begin{bmatrix} 
y'_1 \\\ y'_2 \\\ y'_3\\\ y'_4\\\
\end{bmatrix}
```

By returning to the matrix form using this method, we can see the equations turn into:

```math 
\begin{align}
a_{1,1}x_1 + a_{1,2}x_2 +  a_{1,3}x_3  + a_{1,4}x_4  = y_1 \\ 
a'_{2,2}x_2 +  a'_{2,3}x_3 + a'_{2,4}x_{4} = y_2 \\
a'_{3,3}x_3 + a'_{3,4}x_{4} = y_3 \\
a'_{4,4}x_{4} = y_4 
\end{align}
```
