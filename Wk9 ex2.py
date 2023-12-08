# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:51:12 2023

@author: blath
"""
import numpy as np
#import matplotlib.pyplot as plt


#Rectangle Rule

def calculate_dx (a, b, n):
    return (b-a)/float(n)
def rect_rule (f, a, b, n):
    total = 0.0
    dx = calculate_dx(a, b, n)
    for k in range (0, n):
        total = total + f((a + (k*dx)))
    return dx*total

def func(x):
    return x**2 + 4*x - 12

rect_val = rect_rule(func, -10, 10, 1000)
print('From rectangle rule,', rect_rule(func, -10, 10, 1000))


#Trapezoid Rule
def func(x):
    return x**2 + 4*x - 12

x = np.linspace(-10,10,100)
y = func(x)
#plt.plot(x,y)

x0 = -10
x1 = -9
y0 = func(x0)
y1 = func(x1)

#plt.fill_between([x0,x1], [y0,y1])

A = 0.5*(y1 + y0)*(x1 - x0)
#print("Trapezoid area:", A)

def trapz(f,a,b,N=1000):
    x = np.linspace(a,b,N+1) # N+1 points make N subintervals
    y = f(x)
    y_right = y[1:] # right endpoints
    y_left = y[:-1] # left endpoints
    dx = (b - a)/N
    T = (dx/2) * np.sum(y_right + y_left)
    return T
trap_val = trapz(func, -10, 10, 1000)
print('From Trapezium,', trapz(func, -10, 10, 1000))

#Simpson's one third rule

def simps(f,a,b,N=1000):
    
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    #print(S)
    return S
simps1_val = simps(func, -10, 10, 1000)
print('From Simspsons one third,', simps(func, -10, 10, 1000))


#3/8 Simpsons Rule

def calculate(lower_limit, upper_limit, interval_limit ): 
      
    interval_size = (float(upper_limit - lower_limit) / interval_limit) 
    sum = func(lower_limit) + func(upper_limit); 
   
    # Calculates value till integral limit 
    for i in range(1, interval_limit ): 
        if (i % 3 == 0): 
            sum = sum + 2 * func(lower_limit + i * interval_size) 
        else: 
            sum = sum + 3 * func(lower_limit + i * interval_size) 
      
    return ((float( 3 * interval_size) / 8 ) * sum ) 
simps38_val = calculate(-10,10,1000)
print('Simpson three eight,', calculate(-10,10,1000))

#Actual result

import sympy as sym
# define some symbols
x = sym.Symbol('x')

#Equation
func = x**2 + 4*x - 12
lower_lim = -10
upper_lim = 10

true_val = sym.integrate(func, (x, lower_lim, upper_lim))

true_decimal = float(true_val)

print('==============================================')
print('The true result is,', true_val)
print('In decimal form,', true_decimal)
print('==============================================')

print('The relative errors of each method are:')

Rect_error = (rect_val - true_val)/true_val
Trap_error = (trap_val - true_val)/true_val
Simps_one_third_error = (simps1_val - true_val)/true_val
Simps_three_eight_error = (simps38_val - true_val)/true_val

print('Rectangle Error:', Rect_error)
print('Trapezium Error:', Trap_error)
print('Simspons one third Error:', Simps_one_third_error)
print('Simpsons three eight Error:', Simps_three_eight_error)


