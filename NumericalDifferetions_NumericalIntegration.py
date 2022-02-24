#Askisi2Set2 : Numerical Differentiation and Integration

#Centered differences method
#Simpson's Rule

import numpy as np
import sympy as sp
from sympy import *
import matplotlib.pyplot as plt

#The function
def f(x):
    return(round(x*np.exp(x),6));
#The derivative of the function
def df(x):
    return(round(x*np.exp(x)+np.exp(x),6));

xi=np.array([1.8,1.9,2.0,2.1,2.2]);
yi=np.array([10.889365,12.703199,14.778112,17.148957,19.855030]);

n=len(xi);
h=round(xi[1]-xi[0],1);
yiprime=[];
yiprimereal=[];

#Calculating the derivatives using the method of Central differences and the real values of the derivative
for i in range(n):
    fprime=(f(xi[i]+h)-f(xi[i]-h))/(2*h);
    fprimereal=df(xi[i]);
    yiprime.append(round(fprime,6));
    yiprimereal.append(fprimereal);

fig,(ax1,ax2)=plt.subplots(2,1,sharex=True);
ax1.plot(xi,yi);
ax2.plot(xi,yiprime,'r.',label='Central Difference');
ax2.plot(xi,yiprimereal,'b',label='True values of analytical derivative');
ax2.legend(loc='best');
ax1.set(xlabel='x',ylabel='f(x)=x*exp(x)',title='The plot of function f=x*exp(x)');

fig.tight_layout(pad=2.0);
plt.savefig("Ex2figure.pdf")

print("The values of the derivative of f(x)=x*exp(x) using numerical method at the points:",xi,"are:",yiprime)
print("The real values of the derivative of f(x)=x*exp(x) at points:",xi,"are:",yiprimereal);

#True value of the integral
x=sp.Symbol('x');
Integreal=integrate(x*exp(x),(x,1.8,2.2));
print('The true value of the integral is:',Integreal);
print('*********************************************');

#Using simple form of Simpson's Rule for calculating the integral from xo to xn,where xo=1.8 and xn=2.2
x0=xi[0];
xn=xi[n-1];
Integ1=(0.2/3.0)*(f(x0)+4*f((x0+xn)/2)+f(xn));
print('The value of the integral using the simple form of Simpson Rule is:',Integ1)
et=(Integreal-Integ1)/Integreal;
print('The percent relative error is:et=',et,'%');

#Using the multiple form of Simpson's Rule for calculating the integral from 1.8 to 2.2
sum=0;
for i in range(0,n-1,2):
  sum=sum+f(xi[i])+4*f(xi[i+1])+f(xi[i+2])
  
Integ2=sum*(0.1/3.0)
et=(Integreal-Integ2)/Integreal;
print('*******************************************');
print('The value of the integral using the multiple form of Simpson Rule is:',Integ2);
print('The percent relative error is et=',et,'%');

