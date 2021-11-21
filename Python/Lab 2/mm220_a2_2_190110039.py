# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
"""MM220_A2_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HVpHKKBTetxoydQLP6TztlcLJVXf_AqO
"""

#To get V(r) and F(r)
def differentiate(x,a,b):
    x=sp.symbols('x')
    V= b/(x**12) - a/(x**6)
    F= -sp.diff(V,x)

    return V,F

x= sp.symbols('x')

#Divide by the Boltzmann constant
a=1.024/1.381; b= 1.582/1.381 *10**-3

V,F = differentiate(x,a,b)
V1=[]; F1=[]

#To find values at all points of V(r) and F(r)
for i in np.linspace(0.3,0.8):
    V1.append(V.evalf(subs={x:i}))
    F1.append(F.evalf(subs={x:i}))

x= np.linspace(0.3,0.8)

#To Find Eqm Separation
for i in range(len(V1)):
    if V1[i]== min(V1) :
        r0 = x[i]

print("The equilibrium seperation = %f nm and Force = 0 N here."%r0)

V2,F2= np.array(V1),np.array(F1)

#Multiplying Boltzmann Constant back to get true values
#of Potential V in joule and Force F in newton
plt.plot(x, V2*1.381e-23)
plt.xlabel("r (in nm)")
plt.ylabel('$V(r)$ (in Joule)')
plt.show()

plt.plot(x, F2*1.381e-23)
plt.xlabel("r (in nm)")
plt.ylabel('$F(r)$ in (newton)')
plt.show()