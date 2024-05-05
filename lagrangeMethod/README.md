# Lagrange's Method of Interpolation

This method involves constructing a polynomial of degree $n$, where $n$ is determined by the number of points in the dataset; thus, $n+1$ points are required. For instance, to create a cubic polynomial (degree $n$=3), four data points are necessary. This can be expressed as follows:

```math
y(x) = y_1l_1(x) + y_2l_2(x) + y_3l_3(x) + y_4l_4(x)
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


