#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


def projectile(angle, v0, time):
    t= np.linspace(0,time,900)
    dt=t[1]-t[0] #Length of each time interval
    g= 9.8 #in m/s^2
    m= 1 #in kg
    
    #Assigning velocity parameters
    v0=v0
    vx=v0*np.cos(angle)
    vy=v0*np.sin(angle)
    
    #Position parameters
    y0=0
    x0=0
    vg=0 #It is to denote the decrease in velocity due to gravity
    
    #A list to store all (x,y) positions during flight
    y_list=[y0]
    x_list=[x0]
    
    #Acceleration initialisation 
    ax=0
    ay=-g
    
    for i in range(1, len(t)):
        #We're updating y coordinate here
        vg+= ay*dt
        y0+=(vg+vy)*dt
        
        #Updating X coordinate
        x0+=vx*dt
        
        #Update until the point the ball hits the ground i.e y0=0
        if y0>0:
            y_list.append(y0)
            x_list.append(x0)
        
        else:
            break
    return x_list, y_list


# In[3]:


x_list, y_list= projectile(np.pi/4,60,25)

print("Range of the Projectile is: %.3f metres"%x_list[::-1][0])


# In[4]:


#Plotting Projectile Trajectory
plt.subplots(figsize=(8,6))
plt.plot(x_list, y_list, color='mediumblue')

plt.xlabel("X Coordinate (m)", fontweight='bold', size=14)
plt.ylabel("Y Coordinate (m)", fontweight='bold',size=15)
plt.title("Trajectory of Projectile without Air Drag", fontweight='bold')
plt.show()

