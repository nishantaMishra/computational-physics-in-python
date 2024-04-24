#Root Finding

##Newton-Raphson Method

Let $f(x)$ be a smooth function, and $x_r$ be an unknown root of $f(x)$. Assume that $x_0$ is a guess for
xr . Unless x0 is a very lucky guess, f (x0 ) will not be a root. Given this scenario, we want to find an
x1 that is an improvement on x0 (i.e., closer to xr than x0 ). If we assume that x0 is “close enough”
to xr , then we can improve upon it by taking the linear approximation of f (x) around x0 , which is
a line, and finding the intersection of this line with the x-axis. Written out, the linear approximation
of f (x) around x0 is f (x) ≈ f (x0 ) + f  (x0 )(x − x0 ). Using this approximation, we find x1 such that
f (x1 ) = 0. Plugging these values into the linear approximation results in the following equation:
