import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

#Q1 Begins
#For calculating the symbolic integral
def func(x):
    return x*sp.exp(x)

#For actually calculating value of the function
def func_value(x):
    return x*np.exp(x)

def symbolic_integral(x):
    x= sp.symbols('x')
    integral= sp.integrate(func(x), x)
    return integral

x= sp.symbols('x')
integral= symbolic_integral(x)
integral_values=[]

#To calculate the values of the integral
for i in np.linspace(0,3,100):
    integral_values.append(symbolic_integral(x).evalf(subs={x:i}))

x= np.linspace(0,3,100)

plt.subplots(figsize=(8,6))
plt.plot(x, func_value(x), color='goldenrod')
plt.plot(x, integral_values, color='mediumblue')
plt.xlabel('X', fontweight='bold', size=14)
plt.ylabel('Y', fontweight='bold', size=15)
plt.legend(['f(x)', '$\int$f(x) dx'])
plt.show()