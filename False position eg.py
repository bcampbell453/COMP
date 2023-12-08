# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:51:58 2023

@author: blath
"""

'''
How it works:
    Initial interval chosen so f(a) and f(b) have opposite sign
    a root guess, c, is interpolated using 
    c = a - (f(a)*(b-a))/(f(b)-f(a))
    if the product of f(a) and f(c) is negative, c is set as 
    the new b value, otherwise c is set to the next a value
    unless f(c) == 0, in which case the iterations stop and c
    is spat out as the root.
    
    
False position is better than bisection as it takes into consideration
the magnitude of the function vals at a and b bounds
Root estimate is the common point of the two triangles (see paper notes)
'''



MAX_ITER = 1000000
  
# An example function whose solution 
# is determined using Bisection Method.  
# The function is x^3 - x^2 + 2 
def func( x ): 
    return (x**2+4*x-19) 
  
# Prints root of func(x) in interval [a, b] 
def regulaFalsi( a , b): 
    if func(a) * func(b) >= 0: 
        print("You have not assumed right a and b") 
        return -1
      
    c = a # Initialize result 
      
    for i in range(MAX_ITER): 
          
        # Find the point that touches x axis 
        c = (a * func(b) - b * func(a))/ (func(b) - func(a)) 
          
        # Check if the above found point is root 
        if func(c) == 0: 
            break
          
        # Decide the side to repeat the steps 
        elif func(c) * func(a) < 0: 
            b = c 
        else: 
            a = c 
    print("The value of root is : " , '%.4f' %c) 
    print(i)
  
# Driver code to test above function 
# Initial values assumed 
a =-6
b = 6
regulaFalsi(a, b) 


