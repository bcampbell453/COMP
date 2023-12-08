# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 12:48:49 2023

@author: blath
"""
'''
Euler and Runge-Kutta methods for solving differential
dy/dx = y(1-y)
with initial condition y0 approx 0.0179862 at x = 0

Solve over 0 to 10 x interval with stepsize h = 0.01

are given exact solution to verify code.

Plot RMQE (Root mean Square Error) against h, stepsize
'''
# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math

# ------------------------------------------------------
# inputs

# functions that returns dy/dx
# i.e. the equation we want to solve: dy/dx = - y
def dydx(y,x):
#    k= - 1
    dydx = y*(1-y)
    return dydx

# initial conditions
x0 = 0
y0 = 0.0176862
# total solution interval
x_final = 10
# step size
h = 1
# ------------------------------------------------------
'EULER'
# ------------------------------------------------------
# Euler method

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
# ------------------------------------------------------
'EXACT SOLUTION'
# ------------------------------------------------------
#exact solution
x_exact = x_eul
y_exact = ((np.exp(x_exact-4))/(np.exp(x_exact-4)+1))


print ('Solution: step x y-eul y-exact error%')
for i in range(n_step+1):
    errors[i] = (y_exact[i]-y_eul[i])
    errors_squared[i] = (y_exact[i]-y_eul[i])**2
    print(i,x_eul[i],y_eul[i], y_exact[i], y_exact[i]-y_eul[i])
#print(errors_squared)
#print('i is', i)

sum_errors_squared = np.sum(errors_squared)
#print(sum_errors_squared)

RMQE = np.sqrt((1/(n_step+1))*sum_errors_squared)
print('the root mean square error is', RMQE)


# plot results
plt.plot(x_exact, y_exact, label = 'Exact')
plt.plot(x_eul, y_eul, label = 'Numerical')
plt.legend(loc='upper left')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()

# ------------------------------------------------------
'RK4'
#SOLVING WITH RUNGE KUTTA 4
# ------------------------------------------------------
# inputs
# ------------------------------------------------------

# ------------------------------------------------------
# Fourth Order Runge-Kutta method



# Definition of arrays to store the solution
y_rk = np.zeros(n_step+1)
x_rk = np.zeros(n_step+1)

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
# ------------------------------------------------------

# ------------------------------------------------------
# super refined sampling of the exact solution c*e^(-x)
# ------------------------------------------------------
# print results on screen
print ('Solution: step x y-eul y-exact error%')
for i in range(n_step+1):
    print(i,x_rk[i],y_rk[i], y0 * math.exp(-x_rk[i]),
            (y_rk[i]- y0 * math.exp(-x_rk[i]))/ 
            (y0 * math.exp(-x_rk[i])) * 100)
# ------------------------------------------------------

# ------------------------------------------------------
# plot results
plt.plot(x_rk, y_rk ,label ="rk4", color = 'b')
plt.plot(x_exact, y_exact , label = "Exact", color = 'r')
plt.legend(loc='upper left')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
# ------------------------------------------------------


