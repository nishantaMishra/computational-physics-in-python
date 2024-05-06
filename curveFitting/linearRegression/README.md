# Regression and Curve Fitting

## Linear Regression


Linear regression is a statistical method used to model the relationship between one or more independent variables (often denoted as X) and a dependent variable (often denoted as Y). The goal of linear regression is to fit a linear equation(a straight line) to the observed(or given) data points in order to understand and predict the relationship between these variables.
In linear regression we will try to fit a line to our data, for example

```math
y = a + bx
```
the coefficients $a$ and $b$ can be found by, 

```math
a = \frac{\overline {y} \sum x_i^{2} - \overline{x} \sum x_iy_i }{\sum x_i^2 - n\overline{x}^2}  \quad \quad \quad  b = \frac{\sum x_iy_i - \overline{x} \sum y_i}{\sum x_i^2 - n\overline{x}^2}
```
where bar represents average of the quantity, 

```math
\overline{x} = \frac{1}{n} \sum_{i=1}^n x_i \quad \quad \quad \overline{y} = \frac{1}{n} \sum_{i=1}^n y_i
```

### Example 

Find equation of the line that fits the data

| $x$ | $2$ | $5$ | $4.3$ | $5.3$ | $6$ | $7$ | 
| ---   | :---:    |  :---:   | :---:  | :---:  | :---: | :---:    |    
| $y$ | $1$ | $6$ | $17$ | $23$ | $30$ | $42$ |

