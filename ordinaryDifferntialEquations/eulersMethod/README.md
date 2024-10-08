# Euler's Method

Euler's Method is a straightforward numerical technique for solving ordinary differential equations (ODEs) that are difficult or impossible to solve analytically. It's particularly useful when you have an initial value problem, where the goal is to find the value of a function given its derivative and an initial condition.

### What is Euler's Method?
Euler's Method approximates the solution to an ODE by stepping forward in small increments from the initial value. The basic idea is to use the slope (derivative) of the function at a known point to estimate the value of the function at the next point.


Consider an initial value problem of the form:

```math
\frac{dy}{dx} = f(x,y), \quad y(x_0)=y_0
```
​
Here, $y$ is the unknown function of $x$, and $f(x,y)$ is a given function that defines the derivative of y with respect to x. The goal is to find  y over some interval, starting from the initial condition $y(x_0) = y_0$ .


### Steps of Euler's Method:

```mermaid
graph TD
    A["`Start: Given ODE <br/> dy/dx = f(x, y) and initial <br/> condition  y(x0) = y0`"] --> B["`Choose step size h`"]
    B --> C["`Set initial values: <br/> x = x0, y = y0`"]
    C --> D["`Calculate slope: <br/> dy = f(x, y)`"]
    D --> E["`Update y: <br/> y = y + h * dy`"]
    E --> F["`Update x: x = x + h`"]
    F --> G{"`Is x < xn?`"}
    G --> |Yes| D
    G --> |No| H["`End: Solution approximated <br/> over the interval [x0, xn]`"]

```
## Example

<table border="0">
 <tr>
    <td><b style="font-size:30px">Analytic solution </b></td>
    <td><b style="font-size:30px">Python Solution </b></td>
 </tr>
 <tr>
    <td>We have to solve the differential equation:

$\frac{dx}{dy} = xy $

with the initial condition $y(0)=1$, over the interval $[0,2]$.

Applying Euler's Method:

Define Function:
$f(x,y)=xy$
<p>&nbsp;</p> <!-- Adds vertical space -->

Initial condition: $(x_0 ,y_0) = (0,1)$

Step size: $ℎ = 0.1$


<p>&nbsp;</p> <!-- Adds vertical space -->
Iteration 1:

$y_1 = y_0 + h \cdot f(x_0, y_0) = 1 + 0.1 \cdot (0 \times 1) = 1$

$x_1 = x_0 + h = 0 + 0.1 = 0.1 $

Iteration 2:

$y_2 = y_1 + h \cdot f(x_1, y_1) = 1 + 0.1 \cdot (0.1 \times 1) = 1.01$

$x_2 = x_1 + h = 0.1 + 0.1 = 0.2$

Continue... till convergence
</td>
    <td>
<pre><code class="language-python">
################################################
#####        Euler's Method           #####
#############################################

""" Solve y' = xy over the domain [0,2]
given y(0)=1
"""
### Define function
dy = lambda x,y: x*y 

### Define interval and step size
x = 0
xn = 2
y = 1
h = 0.1
n = int((xn-x)/h)

### Define iteration loop
for i in range(n):
    y = y + dy(x,y)*h
    x = x + h
    print(x,y)
</code></pre>

</td>
 </tr>
</table>


## Code
[eulersMethod.py](eulersMethod.py) : This code solves the given example using Euler's Method

[eulersMethod2.py](eulersMethod2.py) : This code compares the values from numerical solution with real solution.


### Limitations of Euler's Method:
1. *Accuracy*: Euler's method is a first-order method, meaning its error is proportional to the step size $h$. The smaller the step size, the more accurate the method, but it also requires more computational steps.
2. *Stability*: For some differential equations, especially stiff ones, Euler's method can become unstable unless the step size is very small.

[Runge-Kutta method](https://github.com/nishantaMishra/computational-physics-in-python/tree/main/ordinaryDifferntialEquations/rungeKutta) attempts to overcome this limitation of Euler's Method.



