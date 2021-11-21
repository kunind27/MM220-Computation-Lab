import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import scipy.optimize as opt

#Open original file
file= open('lat.dat', 'r')

#Open a new file to write into
mod_file= open('mod_lat.dat','w')
data=[]

#line.split() splits the entire line and returns a list of words contained in the line
#Then we apply map function to convert all the values into float (since they are energy, volume values)
#Then we convert one training example pair of (V,E) and add them to a list
#Then we add those values to a new data file called mod_dat!
while True:
    line= file.readline()
    if line:
        data.append(list(map(float, line.split()[0:])))
    if not line:
        break
file.close()

for i in range(len(data)):
    mod_file.write('%6.6f %6.6f \n'%((data[i][0])**3, data[i][1]))
mod_file.close()

V,E  = np.loadtxt('mod_lat.dat', unpack=True)

#Polynomial Fitting begins
coefs= np.polyfit(V,E, 2)
a,b,c=coefs

V0= -b/(2*a)
E0=  a*(V0**2) +b*V0 + c
B0= 2*a*V0
B0_prime= 4

print("Estimated Values of:")
print("E0 = %f"%E0)
print("V0 = %f"%V0)
print("B0 = %f"%B0)
print("B0_prime = %f"%B0_prime)


#Plotting the Parabolic E vs V curve
plt.subplots(figsize=(8,6))
plt.plot(V,E, 'o', mec='black',mew=1.5, ms=8, color='steelblue')

v_fit= np.linspace(min(V), max(V),100)
plt.plot(v_fit, a*(v_fit**2) + b*v_fit + c, color='orange', lw=2.5)
plt.xlabel('Volume (V) in ${\AA}^3$ ')
plt.ylabel('Energy (E) in eV')
plt.legend(['Actual Data', 'Fitted Data'])
plt.show()


def BM_EOS(V, E0, V0, B0, B0_prime):
    a= (V0/V)**(2/3) - 1
    E= E0 + 9/16*V0*B0*(a**3*B0_prime + (a**2)*(6-4*(a+1)))
    return E

#Using Optimiser to get more accurate values of parameters
#For proper curve fit, using initial guess from parabolic fit
popt, pcov= opt.curve_fit(BM_EOS,V,E, p0=[E0,V0,B0,B0_prime])

E_opt= BM_EOS(V,*popt)

print("Optimsed Values of:")
print("E0 = %f"%popt[0])
print("V0 = %f"%popt[1])
print("B0 = %f"%popt[2])
print("B0_prime = %f"%popt[3])

#Plotting the actual function
v_opt= np.linspace(min(V), max(V), 100)

plt.subplots(figsize=(8,6))
plt.plot(v_opt, E_opt, color='mediumblue')
plt.xlabel('Volume (V) in ${\AA}^3$', size=14)
plt.ylabel('Energy (E) in eV', size=15)
plt.title('Plot of BMEOS E vs V')
plt.show()
