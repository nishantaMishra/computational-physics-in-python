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
f'(x^{(k-1))} \approx \frac{f(x^{(k-1))} - f(x^{(k-2)})}{x^{(k-1)} - x^{(k-2)}} 
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
is so named if you think about the geometric interpretation of our prescription in Eq. $1$ above
From elementary geometry, you may recall that the line that goes through the two points
$(x_0 , y_0 )$ and $(x_1 , y_1)$ is: 
```math
y - y_0 = \frac{y_1 - y_0}{x_1 - x_0} (x - x_0)
```
If you now compute the x axis intercept of this straight line, you will find that it is precisely of the same form 
as in Eq. $(1)$. Thus, in the secant method, at a given step, we
are producing a straight line as the secant through the two points $(x^{(k−1)} , f(x^{(k−1)}))$ and
$(x^{(k−2)} , f(x^{(k−2)}))$. The intercept of that straight line with the x axis gives us the next iterate,
and so on.

---
### Algorithm
Following form of Eq. $1$ has been coded.
```math
x_{new} = x_2 - \frac{(x_2-x_1)}{fn(x_2) - fn(x_1))} \times fn(x_2)
```

---
- [Code](https://github.com/nishantaMishra/computational-physics-in-python/blob/main/SecantMethod/secant1.py)


