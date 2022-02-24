#Askisi1:Bisection Method and Newton-Raphson Method
import numpy as np
import sympy as sp
import matplotlib
import matplotlib.pyplot as plt



def f1(x):
    return (np.exp(x)-2*x*np.cos(x)-3); #(0,2)

def fprime1(x):
    return(np.exp(x)-2*np.cos(x)+2*x*np.sin(x));

def f2(x):
    return(x**2+np.sin(x)+np.exp(x)-2); #(0,1)

def fprime2(x):
    return(2*x+np.cos(x)+np.exp(x)); 

def newtonraphson(f,g,x):
    iter=0;
    itermax=100;
    es=0.5*10**(-3); #scarborough formula
    while True:
        temp=x;
        x=x-(f(x)/g(x));
        iter=iter+1;
        ea=abs((x-temp)/x)*100;
        iter=iter+1;
        if(g(x)==0):
            print("Undefined value of x because f'(x)=0");
            break;
        if(ea<es or iter>itermax):
            break;
    print('The number of iterations for Newton Raphson method is:',iter);
    return x;

def bisection(f,a,b):
    x=(a+b)/2;
    es=0.5*10**(-3);
    iter=0;
    itermax=100;
    while True:
        
        x=(a+b)/2;
        if(f(a)*f(x)<0):
            b=x;
        else:
            a=x;
        iter=iter+1;
        if(abs(a-b)<es or f(x)==0 or iter>itermax):
            break;
    print('The total number of iterations for Bisection Method is:',iter);
    return x;      
        
        
        

print('Newton Raphson Method:');
print('Function: f(x)=exp(x)-2*cos(x)*x-3');
x=np.linspace(0,2,1000);
y1=np.exp(x)-2*np.cos(x)-3;
y2=np.exp(x)+x**2+np.sin(x)-2;
fig,(ax1,ax2)=plt.subplots(2,1,sharex=True);
ax1.plot(x,y1);
ax2.plot(x,y2);
ax1.set(xlabel='x',ylabel='f(x)=exp(x)-2*cos(x)-3',title='The plot of function f(x)=exp(x)-2*cos(x)-3');
ax2.set(xlabel='x',ylabel='f(x)=exp(x)+x^2+sin(x)-2',title='The plot of function f(x)=exp(x)+x^2+sin(x)-2');
fig.tight_layout(pad=2.0);
plt.savefig("Ex1figure.pdf");
rootnr1=newtonraphson(f1,fprime1,0.5);
print('The root of f(x)=0 using the Newton-Raphson method is:',rootnr1);
print('The value of the function at x=',rootnr1,'is:', f1(rootnr1));
print('-------------------');

print('Function: f(x)=x^2+sin(x)+e^x-2');
rootnr2=newtonraphson(f2,fprime2,0.5);
print('The root of f(x)=0 using the Newton-Raphson method is:',rootnr2);
print('The value of the function at x=',rootnr2,'is:', f2(rootnr2));
print('******************************');

print('Bisection Method:');

print('Function: f(x)=exp(x)-2*cos(x)*x-3');
rootbis1=bisection(f1,0,2);
print('The root of f(x)=0 using the Bisection method is:',rootbis1);
print('The value of the function at x=',rootbis1,'is:', f1(rootbis1));
print('----------------------');

print('Function: f(x)=x^2+sin(x)+e^x-2');
rootbis2=bisection(f2,0,1);
print('The root of f(x)=0 using the Bisection method is:',rootbis2);
print('The value of the function at x=',rootbis2,'is:', f2(rootbis2));







