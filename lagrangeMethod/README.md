# Lagrange's Method of Interpolation

This method involves constructing a polynomial of degree $n$, where $n$ is determined by the number of points in the dataset; thus, $n+1$ points are required. For instance, to create a cubic polynomial (degree $n$=3), four data points are necessary. This can be expressed as follows:

```math
y(x) = y_1l_1(x) + y_2l_2(x) + y_3l_3(x) + y_4l_4(x)
```
or in general, 
```math
y(x) = \sum_{l=1}^{n+1} y_il_i(x) \quad \tag{$1$}
```

where, 
```math
l_1(x) = \frac{(x - x_2) (x - x_3) (x - x_4)}{(x_1 - x_2) (x_1 - x_3) (x_1 - x_4)} 
```
```math
l_2(x) = \frac{(x - x_1) (x - x_3) (x - x_4)}{(x_2 - x_1) (x_2 - x_3) (x_2 - x_4)} 
```
```math
l_3(x) = \frac{(x - x_1) (x - x_2) (x - x_4)}{(x_3 - x_1) (x_3 - x_2) (x_3 - x_4)} 
```
```math
l_4(x) = \frac{(x - x_1) (x - x_2) (x - x_3)}{(x_4 - x_1) (x_4 - x_2) (x_4 - x_3)} 
```

in general these relations of ls can be expressed as, 
```math
l_i(x) = \prod_{j=1, j \neq i}^{n+1}  \frac{(x - x_j)}{(x_i - x_j)} \quad \tag{$2$}
```
Then using Eq. $(1)$ and $(2)$, the general form of Lagrange's formula can be written as, 

```math
y(x) = \sum_{l=1}^{n+1} y_i (\right y(x) = \sum_{l=1}^{n+1} y_il_i(x) \quad \tag{$1$} \left)
```


### Example 

```bash
└─# python3 lagrange2.py
Enter numerical values seperated by spaces.

Enter the values of x : 2 3 4 5 6
Enter the values of y : 1.3 2.4 4.3 5 6.1

 Values entered for x are: [2.0, 3.0, 4.0, 5.0, 6.0]
Values entered for y are: [1.3, 2.4, 4.3, 5.0, 6.1]

 Enter the value of x for which y has to be calculated: 3.9
For x = 3.9, y = 4.2
```


