# Regression and Curve Fitting

## Linear Regression


Linear regression is a statistical method used to model the relationship between one or more independent variables (often denoted as X) and a dependent variable (often denoted as Y). The goal of linear regression is to fit a linear equation(a straight line) to the observed(or given) data points in order to understand and predict the relationship between these variables.
In linear regression we will try to fit a line to our data, for example

```math
y = a + bx
```
the coefficients a and b can be found by, 

```math
a = \frac{\overline {y} \sum x_i^{2} - \overline{x} \sum X_iY_i }{\sum x_i^2 - n\overline{x^2}}
```
