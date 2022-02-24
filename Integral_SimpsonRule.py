#Askisi 1 Set3: Simpson's Rule

import numpy as np
import sympy as sp
from sympy import *

def func(x):
    return(x*np.exp(2*x));

#True value of integral
x=sp.Symbol('x');
Integreal=integrate(x*exp(2*x),(x,0,3));
print("The true value of the integral is:",N(Integreal));

#Simple Simpson's Rule h/3 (xo=0,xn=3)
a=0;
b=3;
Integ1=(b-a)/6*(func(a)+4*func((a+b)/2)+func(b));
et=abs(Integ1-N(Integreal))/N(Integreal);
print("The integral using simple Simpson's Rule h/3 is:",Integ1);
print("The percent relative error is:",et*100,"%");
#Simpson's Rule with n=8
n=8;
step=(b-a)/n;
x=np.arange(a,b+step,step);
sum=0;
for i in range(0,n-1,2):
    sum=sum+func(x[i])+4*func(x[i+1])+func(x[i+2]);

Integ2=(step/3)*sum;
print("**********************************");
print("The integral using Simpson's Rule with n=8:",Integ2);
et=abs(Integ2-N(Integreal))/N(Integreal);
print("The percent relative error is:",et*100,"%");

    

