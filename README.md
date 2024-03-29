# NumericalAnalysis
This repository contains problems in numerical analysis with Python.

### Bisection and Newton Raphson Method

- Bisection Method

Bisection method is a bracketing method used for numercial calculation of a function's root. In this method, we assume that the root is in the interval [a,b]
and we bisect the interval in an iterative method and calculate the value of the function in the middle of the interval,
until we reach the root or an accuracy that we set or even a maximum number of iterations.

- Newton Raphson Mehtod 

Newton Raphson method is an open method used for the numerical calculation of a function's root. In this method, we begin with an assumption about the root, xo.
We calculate the 1st derivative of the function in xo f'(xo) which is the slope of the tangential. In this way we can find the bisection point of the tangantial 
and Ox axis xi=xo-f(xo)/f'(xo) and by several iterations we can reach an accuracy for the root, xi.

### Gauss Elimination in Linear Systems

- Gauss Elimination

Gauss Elimination is a method for solving linear systems. In this method, the linear system is being represented by matrices.
There are several transformations that can be performed in a linear system that won't change the outcome. 
These transformations are conducted in this method in order to create the upper triangle matrix of the initial matrix. 
We calculate the last root and then we go up to calculate the other variables. 

### Euler and Runge Kutta method

- Euler method

The Euler method for the numerical solution of differential equations is based on the Taylor series preserving only first order terms. In this example the differential equation y'(x)=yx^2-1.1x is given and we need to find the value of y(2) with initial value y(0)=1. The method is tested for two steps, 0.5 and 0.25 and the corresponding errors have been calculated.

- Runge Kutta method

The 4th order Runge-Kutta method is also used for the solution of the same differential equation with step size 0.25. The four coefficients k1,k2,k3,k4 have been calculated for every iteration. 
