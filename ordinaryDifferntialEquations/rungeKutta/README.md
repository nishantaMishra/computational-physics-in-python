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

Start with the initial conditions: 

x 0and y 0

Calculate Intermediate Slope:

1. Compute the slope at the beginning of the interval:
```math
K_1 = h \cdot f(x_n, y_n)
```

2. Compute the slope at the midpoint using $K_1$
```math
K_2 = h \cdot f \left(  x_n + \frac{h}{2}, y_n + \frac{K_1}{2} \rigth)
```

Update the Solution:

Update the solution using the slope at the midpoint:
𝑦
𝑛
+
1
=
𝑦
𝑛
+
𝐾
2
y 
n+1
​
 =y 
n
​
 +K 
2
​
 
Increment 
𝑥
x by the step size 
ℎ
h:
𝑥
𝑛
+
1
=
𝑥
𝑛
+
ℎ
x 
n+1
​
 =x 
n
​
 +h
