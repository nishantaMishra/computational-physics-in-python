# Root Finding

## Secant Method

Secant Method is similar to the Newton's method. But, the secant method replaces the evaluation of the derivative, needed
for Newton’s method, by a single function evaluation. Although a naive finite-diﬀerence
calculation would be bad (how do you pick h?), the secant method is inspired by such an approach. 
Secant method starts from the Newton's method

```math
x^{(k)} = x^{(k-1)} - \frac{f(x^{(k-1)})}{f'(x^{(k-1)}} \quad k = 1, 2, 3, ...
```
and approximates derivative $ f'(x^{(k-1)}$ using the latest two points and function values
```math
f'(x^{(k-1))} \approx \frac{f(x^{(k-1))} - f(x^{(k-2)})}{x^{(k-1)} - x^{(k-2)}}  \tag{$\ast$}
```
Which looks like finite difference, where the spacing h is picked not by being on a grid
or by hand, but by whatever values our latest iterates have; this implies that the spacing
changes at every iteration.
Combining the last two equations, our prescription for the secant method is:
```math
x^{(k)} = x^{(k-1)} - \frac{x^{(k-1)} - x^{(k-2)}}{f(x^{(k-1))} - f(x^{(k-2)})} * f(x^{(k-1)}) \quad \quad k = 2, 3, 4, ...
```
where we start the iteration at k = 2, since we need two initial guesses as starting points.



One might wonder where the name “secant” comes from. This word secant (from the Latin secare, “to cut”.) refers to a
straight line that cuts a curve in two or more points. You can understand why the method
is so named if you think about the geometric interpretation of our prescription in Eq. above
From elementary geometry, you may recall that the line that goes through the two points
(x0 , y0 ) and (x1 , y1 ) is:

\begin{align}
    g &= \int_a^b f(x)dx \label{eq1} \\
    a &= b + c \label{eq2}
\end{align}

See (\ref{eq1})
