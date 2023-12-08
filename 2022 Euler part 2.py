# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 14:40:15 2023

@author: blath
"""

'''
Part c:
    Stiff equation
    determine max value h can be
    use y(0) = 0.02
    
'''
#PART A
import numpy as np
import matplotlib.pyplot as plt
import math


# functions that returns dy/dx
# i.e. the equation we want to solve: dy/dx = - y
def dydt(y,t):
    dydt = 10*y**2 - y**3
    return dydt

# initial conditions
t0 = 0
y0 = 0.02
# total solution interval
t_final = 20
# step size
#A stepsixe of 0.01 was used to provide precision in results 
#Plotting was used to verify euler plot matches plot from quesiton
#Larger stepsize is not accurate enough
#Smaller would increase computational effort beyond a reasonable amount
#h = 0.014

for h in np.arange(0.01,0.02, 0.002):
    # number of steps
    #math.ceil rounds the number up to th next integer
    n_step = math.ceil(t_final/h)

    # Definition of arrays to store the solution
    y_eul = np.zeros(n_step+1)
    t_eul = np.zeros(n_step+1)
    #errors = np.zeros(n_step+1)
    #errors_squared = np.zeros(n_step+1)
    'CHANGE THOS TO PLOT SEPERATE GRAPHS FOR A RANGE'
    'OF H VALUES SO THAT THEY CAN SEE WHAT THE DECISION'
    'WAS MADE BASED OFF'

    # Initialize first element of solution arrays 
    # with initial condition
    y_eul[0] = y0
    t_eul[0] = t0 

    # Populate the x array
    for i in range(n_step):
        t_eul[i+1]  = t_eul[i]  + h
        

    # Apply Euler method n_step times
    for i in range(n_step):
        # compute the slope using the differential equation
        slope = dydt(y_eul[i],t_eul[i]) 
        # use the Euler method
        y_eul[i+1] = y_eul[i] + h * slope  


    plt.plot(t_eul, y_eul, label = f'h= {h}')
    plt.legend(loc= 'lower right')
    plt.show()



'''
Part d is a written question
'''