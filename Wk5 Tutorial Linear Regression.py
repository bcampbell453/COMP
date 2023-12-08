# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 18:33:05 2023

@author: blath
"""

'''
LINEAR REGRESSION:
    fit experimental data with a straight line to determine a model
    linking the two quantities.
    Plot the data before trying to fit
    Use intrinsic python functions np.polyfit and np.poly1d

WHAT IS LINEAR REGRESSION:
    Models relationship by fitting a linear equation to data
    Y = b0 + b1*X + epsilon
    b0 = Y intercept at x=0
    b1 is the slope of the change in y for one change in x
    epsilon is the error term
    linear regression tries to find b0 and b1 with the least error
    often uses least squares method
    
LEAST SQUARES METHOD:
    Y = b0 + b1*X
    an objective function is specified that is the sum of squared
    differences between experimental values and predicted values
    func is called sum of squared errors
    func is minimised, values that minimise the func are the 
    coefficients used to model the straight line approximation
    
    

'''
# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math
import random

x = np.array([0.    ,     0.06666667, 0.13333333, 0.2   ,     0.26666667, 0.33333333,
     0.4   ,     0.46666667, 0.53333333, 0.6   ,     0.66666667, 0.73333333,
     0.8   ,     0.86666667, 0.93333333, 1.    ,    ])

y = np.array([2.17312991, 2.19988829, 2.33988149, 2.33940595, 2.41968027, 2.99955891,
     3.04855788, 3.86631749, 3.66009775, 4.42305111, 4.22747852, 4.11717969,
     3.87539822, 4.53121841, 5.52211102, 5.30792203])
plt.plot(x,y)
plt.title('Experimental data')    

# array containing the points where we want
# to evaluate the fit
x_fit = np.linspace(0,1,num=64)

# ----------------------------------------------------
# Linear regression using least squares 
# with formulas presented in Lecture
#here a0 and a1 are b0 and b1

n = len(x) # len determins number of variabes within x
a_1 = (n*np.sum(x*y) - np.sum(x)*np.sum(y))/(n * np.sum(x**2) - (np.sum(x))**2)
a_0 = np.mean(y) - a_1*np.mean(x) 

# evaluate the linear regression at the desired points 
#this is the equation i described above
y_reg_lin = a_0 + a_1 * x_fit 

# Print coefficients of linear regression:
print('Coefs a_1 and a_0 (our implementation): ', a_1,a_0)
# ----------------------------------------------------

# ----------------------------------------------------
# Linear regression using python functions

# compute the coefficients for the linear regression
coef = np.polyfit(x,y,1)
# generate the linear function that fits the data 
f_reg_lin = np.poly1d(coef)

# evaluate the linear regression at the desired points 
y_reg_lin_py = f_reg_lin(x_fit)

# Print coefficients of linear regression:
print('Coefs a_1 and a_0 (python function): ', coef)
# ----------------------------------------------------


# plot results
plt.figure()
plt.title('least squares method')
plt.plot(x,y,'gh',ms=5)
plt.plot(x_fit,y_reg_lin,'b-')
plt.xlabel('x')
plt.ylabel('y')

plt.figure()
plt.title('python functions')
plt.plot(x,y,'gh',ms=5)
plt.plot(x_fit,y_reg_lin_py,'r-')
plt.xlabel('x')
plt.ylabel('y')


plt.show()
