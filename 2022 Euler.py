# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:59:05 2023

@author: blath
"""

'''
QUESTION 2

ODE with initial condition
exponential increase until two right hand terms balance eachother

dy/dt = 10y**2 - y**3

Euler method for ODEs
'''

'''
a) Write code to solve ODE with euler method 
and report back y at t=4,5,10
Use initial condition y(0) = 0.02
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
h = 0.01

# number of steps
#math.ceil rounds the number up to th next integer
n_step = math.ceil(t_final/h)

# Definition of arrays to store the solution
y_eul = np.zeros(n_step+1)
t_eul = np.zeros(n_step+1)
#errors = np.zeros(n_step+1)
#errors_squared = np.zeros(n_step+1)


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
    
#number in [] is one bigger as euler starts at t=0
#So the 2nd value is actually at t=0 etc   
print('At t=4, the solution is', y_eul[5])
print('At t=5, the solution is', y_eul[6])
print('At t=6, the solution is', y_eul[11])

plt.plot(t_eul, y_eul)



'''
b) Report the ignition delay for the three initial conditoins:
    y(0) = 0.02
    y(0) = 0.01
    y(0) = 0.005
    
From the code below, values are read from graph to be:
    y(0) = 0.02 ignition at t=5s
    y(0) = 0.01 ignition at t=10s
    y(0) = 0.005 ignition at t = 20
'''

#Making a loop to run through the three initial conditions 
#and then plot each so ignition delay can be determined from plots

y_0 = [0.02, 0.01, 0.005]

for y in y_0:
    # initial conditions
    t0 = 0
    y0 = y
    # total solution interval
    t_final = 30
    # step size
    #A stepsixe of 0.01 was used to provide precision in results 
    #Plotting was used to verify euler plot matches plot from quesiton
    #Larger stepsize is not accurate enough
    #Smaller would increase computational effort beyond a reasonable amount
    h = 0.01

    # number of steps
    #math.ceil rounds the number up to th next integer
    n_step = math.ceil(t_final/h)

    # Definition of arrays to store the solution
    y_eul = np.zeros(n_step+1)
    t_eul = np.zeros(n_step+1)
    #errors = np.zeros(n_step+1)
    #errors_squared = np.zeros(n_step+1)


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

    plt.plot(t_eul, y_eul, label=f'y(0)= {y}')
new_x_ticks = np.arange(0, 31, 1)  # Define new tick locations
plt.xticks(new_x_ticks)  # Set the new tick locations
plt.legend(loc = 'lower right')
plt.grid(True)
plt.show()




    