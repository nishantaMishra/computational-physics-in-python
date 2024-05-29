cd# Finding Average (Mean, Median, Mode)

Arithmetic mean, median and mode are the most common measures of central tendency. 

### Mean 
The most commonly used method foe finding the average of given dataset. To find the mean simply add up all the values and divide by total number of values.
If given data is $X = \{ x_1, x_2, x_3, ... x_n \}$ then mean is
```math
\text{mean} = \sum_{i=1}^n \frac{x_i}{n} 
```

### Median 
Median is defined as the value that is exactly in the middle of a data set.

Median could be found by following steps,
1. Sort the data from smallest to largest.
2. Median is the middle number of the sorted set of n values.
```math
\begin{align}
    \text{if n is odd} ; \text{median} = x_{\frac{n + 1}{2}}  \\ 
\text{if n is even}; \text{median} = \frac{x_{\frac{n}{2}}  + x_{\frac{n}{2} + 1}}{2}
\end{align}

```
### Mode
Mode refers to the most occurring number/value in the given set.

## Codes
[This file](average.py) contains the code for calculating mean, median mode of a given data
