#Askisi2: Euler's method and RK 4th order method

import numpy as np
import sympy as sp
from sympy import *

def f(t,y):
    return(y*t**2-1.1*y);

#Analytical solution: y=exp(x^3/3-1.1x)
x=sp.Symbol('x');
yt=lambdify(x,sp.exp(x**3/3-1.1*x));

print("The true analytical solution is y(2)=",yt(2));

#Euler's Method
to=0;
tn=2;
h1=0.5;
h2=0.25;
n1=int((tn-to)/h1);
n2=int((tn-to)/h2);
#points from to=0 to t=2 with step h1 and h2
t=0;
y=1; #Initial Value problem
#h=0.5
for i in range(1,n1+1):
    y=y+f(t,y)*h1;
    t=t+h1;
    
eteuler1=abs(yt(2)-y)/yt(2);

print("The solution using Euler's Method with h=0.5 is:",y);
print("The relative percent error is:",eteuler1*100,"%");

#h=0.25
y=1;
t=0;
for i in range(1,n2+1):
    y=y+f(t,y)*h2;
    t=t+h2;

eteuler2=abs(yt(2)-y)/yt(2);

print("The solution using Euler's Method with h=0.25 is:",y);
print("The relative percent error is:",eteuler2*100,"%");

#RK 4th order 
y=1;
t=0;
k1=f(t,y);
k2=f(t+0.5*h1,y+0.5*k1*h1);
k3=f(t+0.5*h1,y+0.5*k2*h1);
k4=f(t+h1,y+k3*h1);
for i in range(1,n1+1):
    y=y+(1/6)*(k1+2*k2+2*k3+k4)*h1;
    t=t+h1;
    k1=f(t,y);
    k2=f(t+0.5*h1,y+0.5*k1*h1);
    k3=f(t+0.5*h1,y+0.5*k2*h1);
    k4=f(t+h1,y+k3*h1);


etrk1=abs(yt(2)-y)/yt(2);
print("The solution using RK 4th order method with h=0.5 is:",y);
print("The relative percent error is:",etrk1*100,"%");

y=1;
t=0;
k1=f(t,y);
k2=f(t+0.5*h2,y+0.5*k1*h2);
k3=f(t+0.5*h2,y+0.5*k2*h2);
k4=f(t+h2,y+k3*h2);
for i in range(1,n2+1):
    y=y+(1/6)*(k1+2*k2+2*k3+k4)*h2;
    t=t+h2;
    k1=f(t,y);
    k2=f(t+0.5*h2,y+0.5*k1*h2);
    k3=f(t+0.5*h2,y+0.5*k2*h2);
    k4=f(t+h2,y+k3*h2);

etrk2=abs(yt(2)-y)/yt(2);

print("The solution using RK 4th order method with h=0.25 is:",y);
print("The relative percent error is:",etrk2*100,"%");


    
    
    

