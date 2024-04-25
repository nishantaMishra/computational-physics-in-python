# Root Finding

## Regula Falsi Method
```math
x^{(k)} = x^{(k-1)} - \frac{x^{(k-1)} - x^{(k-2)}}{f(x^{(k-1))} - f(x^{(k-2)})} * f(x^{(k-1)}) \quad \quad k = 2, 3, 4, ...   \tag{$1$}
```
The  **regula falsi method** or **false position** which is very similar to
the secant method. The diﬀerence is that regula falsi is a bracketing method, so it starts
with $x_0$ and $x_1$ such that $f(x_0) \times f(x_1) < 0$. Like the secant method, it then employs the
line that goes through the two points $(x_0, y_0)$ and $(x_1 , y_1)$, as per Eq.$(1)$, and then
finds the x axis intercept. The false-position method then ensures that it continues
to bracket the root.

