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
- Increment $x$ by the step size $h$:
```math
x_{n+1} = x_n + h
```

## Code 
[secondOrderRungeKutta.py](secondOrderRungeKutta.py) : This solves the equation $\frac{dy}{dx} = xy$ using second order Runge-Kutta Method.

## Fourth Order Runge-Kutta Method

The RK4 method estimates the solution of ODE by combining weighted averages of slopes calculated at different points within each interval. This approach increases accuracy compared to lower-order methods (like Euler's method or the second-order Runge-Kutta method).

### Algorithm of RK4 Method

Given an ODE $\frac{dy}{dx} = f(x,y)$ and initial conditions $x_0$ and $y_0$ , the RK4 method proceeds as follows:

1. Calculate Intermediate Slopes:

​
- $K_1$ : Slope at the beginning of the interval (Euler's method slope).
 ```math
 K_1 = h \cdot f(x_n, y_n)
 ```
 Slope at the midpoint, using 
𝐾
1
K 
1
​
  for estimation.
𝐾
2
=
ℎ
⋅
𝑓
(
𝑥
𝑛
+
ℎ
2
,
𝑦
𝑛
+
𝐾
1
2
)
K 
2
​
 =h⋅f(x 
n
​
 + 
2
h
​
 ,y 
n
​
 + 
2
K 
1
​
 
​
 )
𝐾
3
K 
3
​
 : Another slope at the midpoint, but now using 
𝐾
2
K 
2
​
  for estimation.
𝐾
3
=
ℎ
⋅
𝑓
(
𝑥
𝑛
+
ℎ
2
,
𝑦
𝑛
+
𝐾
2
2
)
K 
3
​
 =h⋅f(x 
n
​
 + 
2
h
​
 ,y 
n
​
 + 
2
K 
2
​
 
​
 )
𝐾
4
K 
4
​
 : Slope at the end of the interval, using 
𝐾
3
K 
3
​
  for estimation.
𝐾
4
=
ℎ
⋅
𝑓
(
𝑥
𝑛
+
ℎ
,
𝑦
𝑛
+
𝐾
3
)
K 
4
​
 =h⋅f(x 
n
​
 +h,y 
n
​
 +K 
3
​
 )
Update the Solution:

Combine the slopes to update 
𝑦
y with a weighted average:
𝑦
𝑛
+
1
=
𝑦
𝑛
+
1
6
(
𝐾
1
+
2
𝐾
2
+
2
𝐾
3
+
𝐾
4
)
y 
n+1
​
 =y 
n
​
 + 
6
1
​
 (K 
1
​
 +2K 
2
​
 +2K 
3
​
 +K 
4
​
 )
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
Explanation of the Slopes
𝐾
1
K 
1
​
 : The slope at the beginning of the interval, similar to what Euler's method would use.
𝐾
2
K 
2
​
  and 
𝐾
3
K 
3
​
 : Slopes at the midpoint of the interval, providing a better estimate of the curvature of the solution.
𝐾
4
K 
4
​
 : The slope at the end of the interval, offering a final adjustment.
The method then takes a weighted average of these slopes to approximate the next value of 
𝑦
y. This approach captures more information about the behavior of the function within each step, leading to higher accuracy.
