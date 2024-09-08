# Runge-Kutta Method

## Second Order Runge-Kutta Method
The second-order Runge-Kutta method, also known as the midpoint method, is a straightforward but powerful method to approximate the solution of first-order ODEs.

Given an ODE of the form:
```math
\frac{dy}{dx} = f(x,y)
```

with an initial condition 

```math
y(x_0) = y_0
​```

, the goal is to approximate the value of $y$ over a range of $x$ values.


### Basic Idea
The second-order Runge-Kutta method improves upon Euler's method by making a more accurate estimate of the slope. Instead of using just the initial slope (like in Euler's method), it takes an intermediate step to estimate the slope more accurately.


