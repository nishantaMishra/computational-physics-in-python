# Numerical integration

## Simpson's rule

Simpson's rules are the methods of numerical integration proposed by Thomas Simpson. There are two rules given by Thomas Simpson, called Simpson's 1/3 rule and Simpson's 3/8 rule. Both these rules provide more accurate approximations compared to the Trapezoidal Rule by using parabolic or cubic interpolations instead of linear ones.

### Simpson's 1/3 Rule

Consider two consecutive subintervals, $[x_{i-1}, x_i] \text{ and } [x_i, x_{i+1}]$. Simpson's 1/3 rule approximates the area under the curve over these two sub-intervals by fitting a quadratic polynomial through the points $ (x_{i-1}, f(x_{i-1})), (x_i, f(x_i)), \text{ and } (x_{i+1}, f(x_{i+1})), which is a unique polynomial, and then integrates the quadratic exactly. 

[<img src="figure1.png" width="250"/>](figure1.png) 

For an integral $\int_a^b f(x) dx$, where $b-a = 2h$, Simpson's 1/3 rule is, 
```math
\int_a^b f(x) dx \approx \frac{h}{3} \left[  f(a) + 4f(\frac{a+b}{2}) + f(b) \right]
```

