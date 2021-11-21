#!/usr/bin/env python
# coding: utf-8

# In[1]:

#ALSO PLEASE NOTE! You may have to close the window of the first plot before you get the second plot! Please do that so
#you get all the plots!

import numpy as np
import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


def projectile_drag(angle, v0, time):
    t=np.linspace(0,time,1000)
    dt=t[1]-t[0]
    g=9.8 #m/s^2
    m= 1 #kg
    cd=0.005 #Drag Coefficient
    
    v0=v0
    vx= v0*np.cos(angle)
    vy= v0*np.sin(angle)
    
    x0=0
    y0=0
    vd_x=0 #X dir Velocity decrease due to drag
    vd_y=0 #Y dir velocity decrease due to drag and gravity
    
    #List of position coordinates
    x_list=[x0]
    y_list=[y0]
    vx_list=[vx]
    vy_list=[vy]
    
    for i in range(1, len(t)):
        ay=-g -cd*v0*vy/m
        ax= -cd*v0*vx/m
        
        vd_y= ay*dt
        vy+=vd_y
        y0+= (vy)*dt
        
        
        vd_x= ax*dt
        vx+= vd_x
        x0+= (vx)*dt
        
        v0=np.sqrt(vx**2+vy**2)
        
        if y0>0:
            y_list.append(y0)
            x_list.append(x0)
            vx_list.append(vx)
            vy_list.append(vy)
        
        else:
            break
    return x_list, y_list, vx_list, vy_list

#ALSO PLEASE NOTE! You may have to close the window of the first plot before you get the second plot! Please do that so
#you get all the plots!
# In[3]:


x_list, y_list, vx_list, vy_list= projectile_drag(np.pi/3, 30, 30)

print("Range of the Projectile is %.3f metres"%x_list[::-1][0])


# In[4]:

#Plotting Trajectory of the Projectile
plt.subplots(figsize=(8,6))
plt.plot(x_list, y_list, color='red')

plt.xlabel("X Coordinate (m)", fontweight='bold', size=14)
plt.ylabel("Y Coordinate (m)", fontweight='bold',size=15)
plt.title('Trajectory of Projectile with Air Drag', fontweight='bold')

plt.grid(True)
plt.show()

#ALSO PLEASE NOTE! You may have to close the window of the first plot before you get the second plot! Please do that so
#you get all the plots!
# In[5]:


#Plotting Vx as a function of time
plt.subplots(figsize=(8,6))
plt.plot(np.linspace(0,30,900)[:len(vx_list)], vx_list, color='darkblue')

plt.title("$v_x$ (m/s) v/s Time (s)", fontweight='bold')
plt.xlabel("Time", fontweight='bold', size=14)
plt.ylabel("X component of Velocity", fontweight='bold', size=15)

plt.grid(True)
plt.show()

#ALSO PLEASE NOTE! You may have to close the window of the first plot before you get the second plot! Please do that so
#you get all the plots!
# In[6]:


#Plotting Vy as a function of time
plt.subplots(figsize=(8,6))
plt.plot(np.linspace(0,30,900)[:len(vy_list)], vy_list, color='darkblue')

plt.title("$v_y$ (m/s) v/s Time (s)", fontweight='bold')
plt.xlabel("Time", fontweight='bold', size=14)
plt.ylabel("X component of Velocity", fontweight='bold', size=15)

plt.grid(True)
plt.show()

