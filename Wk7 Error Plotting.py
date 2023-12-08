# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:36:29 2023

@author: blath
"""

# ------------------------------------------------------

'''
Must now find RMQE for various step sizes and plot them 
against the stepsize value.
'''

# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math

def dydx(y,x):
#    k= - 1
    dydx = y*(1-y)
    return dydx

# initial conditions
x0 = 0
y0 = 0.0176862
# total solution interval
x_final = 10
#step sizes
h_vals = [0.01, 0.05, 0.75, 0.1, 0.25, 0.5, 0.75, 1, 2, 3, 4, 5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
h_1 = np.zeros(len(h_vals))
h_4 = np.zeros(len(h_vals))

for i in range(len(h_vals)):
    h_1[i] = (h_vals[i])**1
    h_4[i] = (h_vals[i])**4

RMQE_eul = []
RMQE_rk4 = []

for h in h_vals:
    
    #EULER
    # number of steps
    #math.ceil rounds the number up to th next integer
    n_step = math.ceil(x_final/h)

    # Definition of arrays to store the solution
    y_eul = np.zeros(n_step+1)
    x_eul = np.zeros(n_step+1)
    errors = np.zeros(n_step+1)
    errors_squared = np.zeros(n_step+1)


    # Initialize first element of solution arrays 
    # with initial condition
    y_eul[0] = y0
    x_eul[0] = x0 

    # Populate the x array
    for i in range(n_step):
        x_eul[i+1]  = x_eul[i]  + h
    

    # Apply Euler method n_step times
    for i in range(n_step):
        # compute the slope using the differential equation
        slope = dydx(y_eul[i],x_eul[i]) 
        # use the Euler method
        y_eul[i+1] = y_eul[i] + h * slope
        
    #exact solution
    x_exact = x_eul
    y_exact = ((np.exp(x_exact-4))/(np.exp(x_exact-4)+1))
    
    #ERROR CALCULATION
    for i in range(n_step):
        errors[i] = (y_exact[i]-y_eul[i])
        errors_squared[i] = (y_exact[i]-y_eul[i])**2
    sum_errors_squared = np.sum(errors_squared)
    #print(sum_errors_squared)

    RMQE = np.sqrt((1/(n_step+1))*sum_errors_squared)
    RMQE_eul.append(RMQE)
    
    
    #RK4
    # Definition of arrays to store the solution
    y_rk = np.zeros(n_step+1)
    x_rk = np.zeros(n_step+1)
    errors_rk = np.zeros(n_step+1)
    errors_squared_rk = np.zeros(n_step+1)

    # Initialize first element of solution arrays 
    # with initial condition
    y_rk[0] = y0
    x_rk[0] = x0 

    # Populate the x array
    for i in range(n_step):
        x_rk[i+1]  = x_rk[i]  + h

    # Apply RK method n_step times
    for i in range(n_step):
       
        # Compute the four slopes
        x_dummy = x_rk[i]
        y_dummy = y_rk[i]
        k1 =  dydx(y_dummy,x_dummy)
        
        x_dummy = x_rk[i]+h/2
        y_dummy = y_rk[i] + k1 * h/2
        k2 =  dydx(y_dummy,x_dummy)

        x_dummy = x_rk[i]+h/2
        y_dummy = y_rk[i] + k2 * h/2
        k3 =  dydx(y_dummy,x_dummy)

        x_dummy = x_rk[i]+h
        y_dummy = y_rk[i] + k3 * h
        k4 =  dydx(y_dummy,x_dummy)

        # compute the slope as weighted average of four slopes
        slope = 1/6 * k1 + 2/6 * k2 + 2/6 * k3 + 1/6 * k4 

        # use the RK method
        y_rk[i+1] = y_rk[i] + h * slope  
        
        
    #RK4 Errors
    for i in range(n_step):
        errors_rk[i] = (y_exact[i]-y_rk[i])
        errors_squared_rk[i] = (y_exact[i]-y_rk[i])**2
    sum_errors_squared_rk = np.sum(errors_squared_rk)
    #print(sum_errors_squared)

    RMQE_rk = np.sqrt((1/(n_step+1))*sum_errors_squared_rk)
    RMQE_rk4.append(RMQE_rk)
    
plt.scatter(h_vals, RMQE_eul, label='Euler Method', color='g')
plt.scatter(h_vals, RMQE_rk4, label='RK4', color='r')
plt.plot(np.log10(h_vals), np.log10(h_1), color = 'g')
plt.plot(np.log10(h_vals), np.log10(h_4), color = 'r')
plt.yscale('log')  
plt.xscale('log')
plt.xlabel('h (log scale)')
plt.ylabel('RMQE')
plt.legend()
plt.show()
    