# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 11:42:53 2023

@author: blath
"""

import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

for N in [10, 50, 100, 500]:
    n= N
    a = -10
    b = 10
    #Rectangle
    def calculate_dx (a, b, n):
        return (b-a)/float(n)
    def rect_rule (f, a, b, n):
        total = 0.0
        dx = calculate_dx(a, b, n)
        x_values = []
        y_values = []
        
        for k in range(0, n):
            x = a + k * dx
            y = f(x)
            
            x_values.append(x)
            y_values.append(y)
            
            total += y
        
        area = dx * total
        return area, x_values, y_values

    def func(x):
        return x**2 + 4*x - 12
    #print('From rectangle rule,', rect_rule(func, a, b, N))

    # Calculate the area and store values
    true_x = np.linspace(-10,10, 1000)
    true_y = true_x**2 + 4*true_x - 12
    plt.plot(true_x, true_y, color='red', label='True Function')
    area, x_values, y_values = rect_rule(func, a, b, n)
    plt.bar(x_values, y_values, width=(b - a) / n, alpha=0.3, align='edge', label='Rectangles')

    # Add labels and legend
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Rectangle Rule Approximation')
    plt.legend()
    plt.show()
    
    #Trapezium        
    def trapz(f,a,b,N):
        x_values_trap = []
        y_values_trap = []
        x = np.linspace(a,b,N) # N+1 points make N subintervals
        y = f(x)
        y_right = y[1:] # right endpoints
        y_left = y[:-1] # left endpoints
        #x_values_trap.append(x)
        y_values_trap.append(y)
        dx = (b - a)/N
        T = (dx/2) * np.sum(y_right + y_left)
        return T, x_values_trap, y_values_trap
    #print('From Trapezium,', trapz(func, a, b, N))
    
    #Plotting
    
    plt.plot(true_x, true_y, color='red', label='True Function')
    x0 = a; x1 = a+1;
    y0 = func(x0); y1 = func(x1);
    plt.fill_between([x0,x1],[y0,y1])
    plt.show()
    
    #Simps first
    def simps(f,a,b,N):        
        if N % 2 == 1:
            raise ValueError("N must be an even integer.")
        dx = (b-a)/N
        x = np.linspace(a,b,N+1)
        y = f(x)
        S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
        print(S)
        return S
    #print('From Simspsons one third,', simps(func, a, b, N))
    
    #Simps 38
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
    #print('Simpson three eight,', calculate(a, b, ,N))






