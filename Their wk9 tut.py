# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 08:52:26 2023

@author: blath
"""
import numpy as np

def rect_rule (f, a, b, n):
    total = 0.0
    dx = (b-a)/float(n)
    for k in range (0, n):
        total += f((a +(k*dx)+0.5*dx))
    return dx*total

def f(x):
    return x**2+4*x-12

print(rect_rule(f, -10, 10, 10000))

def trapz(f,a,b,N=50):
    x = np.linspace(a,b,N+1) # N+1 points make N subintervals
    y = f(x)
    y_right = y[1:] # right endpoints
    y_left = y[:-1] # left endpoints
    dx = (b - a)/N
    T = (dx/2) * np.sum(y_right + y_left)
    return T

def f(x):
    return x**2+4*x-12

a=-10
b=10
n=10000
print(trapz(f,a,b))

def simps(f,a,b,N=50):
    if N % 2 == 1:
        raise ValueError("N must bean even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    
    S = dx/3 * np.sum(y[0:-1:2] +4*y[1::2] + y[2::2])
    return S

f = lambda x: x**2+4*x-12
solution = simps(f,-10,10,2)
print(solution)

def func(x):
    return x**2+4*x-12
# Function to perform calculations
def calculate(func,lower_limit, upper_limit, interval_limit ):
    interval_size = (upper_limit - lower_limit) / interval_limit
    sum = func(lower_limit) + func(upper_limit);
# Calculates value till integral limit
    for i in range(1, interval_limit ):
        if (i % 3 == 0):
            sum = sum + 2 * func(lower_limit + i * interval_size)
        else:
            sum = sum + 3 * func(lower_limit + i * interval_size)
    return ((float( 3 * interval_size) / 8 ) * sum )
    
# driver function

interval_limit = 30

lower_limit = -10
upper_limit = 10
integral_res = calculate(func,lower_limit, upper_limit, interval_limit)
# rounding the final answer to 6 decimal places
print (round(integral_res, 6))

import matplotlib.pyplot as plt

# import all modules . Not that I commented out the f definition within modules 
# ex1 to ex4. This is so I can define f in the master script here.
# If f is defined for example within ex1 this will take priority as it is located
# within the ex1 module and therefore if I redefine f in this master script it won't
# calculate the integral for this new function except if I also change it in ex1.py
# 
# The same applies for a,b and n which I did not define within each module



# define function here
def f(x):
    return x**2+4*x-12

#analytical integral used to obtain exact integral value
def Integral_f(x):
    return 1/3*x**3+2*x**2-12*x

   

a=-10  #lower bound
b=10  #upper bound

n=200 #maximum amount of subdivisions used in the loop at the bottom

Exact_Integral=Integral_f(b)-Integral_f(a)  #exact integral value used for error control

# I have defined all my variables as empty lists so that I can add a value within
# the loop that follows using the append method (read about it online).
# An alternative method would have been to use numpy and np.zeros(n) to get a
# vector of the correct lenght and replacing the zeros within the loop at the bottom

rect=[]     
rect_error=[]

trapezoid=[]
trapezoid_error=[]

simpson=[]
simpson_error=[]

simpson38=[]
simpson38_error=[]

x=[]

#Note that the way we defined simpson's rule we need to use an even number of subdivisions
# That is why I am starting with 2 subdivisions and increasing in steps of 2

for n in range(2,n,2):
    
    x.append(n)
    rect.append(rect_rule(f, a,b, n))  # using the rect_rule function defined in the ex1.py module
    # and adding it to the rect array
    
    rect_error.append(abs(rect_rule(f, a,b, n)-Exact_Integral)) #calculating the absolute
    # value of the error and adding it to the rect_error array
    
    trapezoid.append(trapz(f,a,b,n))
    trapezoid_error.append(abs(trapz(f, a,b, n)-Exact_Integral))
    
    simpson.append(simps(f,a,b,n))
    simpson_error.append(abs(simps(f, a,b, n)-Exact_Integral))
    
    simpson38.append(calculate(f,a,b,n))
    simpson38_error.append(abs(calculate(f,a,b,n)-Exact_Integral))
    

#plotting the solution for the integral as a function of subdivisions used
plt.plot(x,rect,x,trapezoid,x,simpson,x,simpson38)
plt.ylim(400,450)
plt.legend(['MidPoint Rule','Trapezoidal','Simpson Rule','3/8 Simpson'])
plt.show()

#plotting the error as a function of steps used
plt.semilogy(x,rect_error,x,trapezoid_error,x,simpson_error)
plt.legend(['MidPoint Rule','Trapezoidal','Simpson Rule'])

