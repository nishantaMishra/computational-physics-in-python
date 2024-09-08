# Runge-Kutta Method

## Second Order Runge-Kutta Method
The second-order Runge-Kutta method, also known as the midpoint method, is a straightforward but powerful method to approximate the solution of first-order ODEs.

Given an ODE of the form:
```math
\frac{dy}{dx} = f(x,y), \text{initial condition} \quad y(x_0) = y_0
```

with an initial condition 

```math
y(x_0) = y_0
```
the goal is to approximate the value of $y$ over a range of $x$ values.


### Basic Idea
The second-order Runge-Kutta method improves upon Euler's method by making a more accurate estimate of the slope. Instead of using just the initial slope (like in Euler's method), it takes an intermediate step to estimate the slope more accurately.


### Steps of Second Order Runge_Kutta Method
Steps of the Second-Order Runge-Kutta Method


Initial Values:

1. Start with the initial conditions: 

$x_0$ and $y_0$

2. Calculate Intermediate Slope:

- Compute the slope at the beginning of the interval:
```math
K_1 = h \cdot f(x_n, y_n)
```

- Compute the slope at the midpoint using $K_1$
```math
K_2 = h \cdot f \left(  x_n + \frac{h}{2}, y_n + \frac{K_1}{2} \right)
```

3. Update the Solution:

- Update the solution using the slope at the midpoint:
```math
y_{n+1} = y_n + K_2
```
Increment $x$ by the step size $h$:
```math
x_{n+1} = x_n + h
```

## Code 
[secondOrderRungeKutta.py](secondOrderRungeKutta.py) : This solves the equation $\frac{dy}{dx} = xy$ using second order Runge-Kutta Method.

