# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 10:03:45 2023

@author: blath
"""

import numpy as np

#Root finding by bisection

def bisection(func, a, b, N):
    #Do a and b bound a root?
    if func(a)*func(b) >= 0:
        print("a and b don't bound a root")
        return None
    a_n = a
    b_n = b
    for n in range(1, N+1):
        root_guess = (a_n + b_n)/2
        f_root = func(root_guess)
        
        #error so iterations don't go on infinetely
        error_bound = 0.1
        #if the product of guess function and func(a) is negative,
        #assign the guess as the next b_n variable. (Left shift)
        #If the product of guess function and func(b) is negative, 
        #assign the guess as the next a_n variable. (Right shift)
        if f_root*func(a) < 0:
            a_n = a_n
            b_n = root_guess
        elif f_root*func(b) < 0:
            a_n = root_guess
            b_n = b_n
        elif f_root <= error_bound:
            print("Exact solution has been found on iteration", n)
            break
            return root_guess, N
            
        else:
            print("The bisection method has failed")
            return None
    return (a_n + b_n)/2
            
#Define the function that bisection method is to be applied to:
#f = lambda x: np.sin(x)*np.exp(x**0.1)
f = lambda x: x**2 + 4*x - 12

#Root finding
root = bisection(f, -10, -3, 100)
print("The root found through bisection is:", root)


'''
Simple iterative root finding method, particularly useful for continuous
functions with sign changes.
Specify an initial a,b interval so that f(a) and f(b) have opposite signs
calculate the midpoint and evaluate the function at the midpoint
if the product of f(a) and f(midpoint) is negative, set b = midpoint
if the product of f(b) and f(midpoint) is negative, set a = midpoint
repeat iterations until a close enough solution is found
'''