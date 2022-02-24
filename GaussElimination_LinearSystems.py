#Ask1Set2:Gauss Elimination 

import numpy as np
import sympy as sp

A=np.array([[1,-1, 2, -1],[2, -2, 3, -3],[1, 1, 1, 0],[1, -1, 4, 3]]);
B=np.array([[-8],[-20],[-2],[4]]);
x1=sp.Symbol('x1');
x2=sp.Symbol('x2');
x3=sp.Symbol('x3');
x4=sp.Symbol('x4');
x=np.array([[x1],[x2],[x3],[x4]]);
n=len(x);

#Printing the representation of the linear system as matrices
for i in range(n):
    print(A[i],x[i],"=",B[i]);

#Creating the upper triangle matrix A using Gauss Elimination
for i in range(n):
    if(A[i][i]==0 and i<n-1):
        #pivoting
       A[[i,i+1]]=A[[i+1,i]];
       B[[i,i+1]]=B[[i+1,i]]
    for j in range(i+1,n):  
        a=A[j][i]/A[i][i];
        A[j]=A[j]-a*A[i];
        B[j]=B[j]-a*B[i];

x=np.array([[0], [0], [0], [0]]);
sum=0;
#Calculating the solutions of the system
for k in range(n-1,-1,-1):   
    for i in range(k+1,n):
        sum=sum+A[k][i]*x[i][0];
    
    x[k][0]=(B[k][0]-sum)/A[k][k];
    sum=0;

print("The solution of the system using Gauss Elimination is:"); 
for j in range(n):
    print("x",j+1,"=",x[j][0]);

    
    
