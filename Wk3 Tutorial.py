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
        elif f_root == 0:
            print("Exact solution has been found")
            return root_guess
        else:
            print("The bisection method has failed")
            return None
    return (a_n + b_n)/2
            
#Define the function that bisection method is to be applied to:
f = lambda x: np.sin(x)*np.exp(x**0.1)

#Root finding
root = bisection(f, 0.1, 5, 1000)
print("The smallest positive root found through bisection is:", root)