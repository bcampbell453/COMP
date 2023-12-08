# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:22:29 2023

@author: blath
"""

'''
 a) Use appropriate root finding technique to determine any
value of x in 0<x<4 where xn = xn+1
'''
import numpy as np
from scipy.optimize import fsolve

#If xn = xn+1 we can just use one variable, x, to solve:
def function(x):
    x = 1/(np.sin(x)) + 1/4
    return x

for n in np.arange(0.1,4.1):
    x_val = fsolve(function, n)
    print(x_val)
    
    
'''
Part b) 
    Closed root interval finding technique to find a root
    within the range (0,4) with all terms placed on rhs
'''

"A closed root findind method would be bisection method"

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
f = lambda x: 1/(np.sin(x)) + 1/4 - x

#Root finding
root = bisection(f, -1, 4, 100)
print("The root found through bisection is:", root)




'''
Part c)
    Use open root finding to find the same root
    in the same domain
'''

#using secant as f looks difficult to differentiate

def secant(f,a,b,N):
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Secant method fails.")
            return None
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))

f = lambda x: 1/(np.sin(x)) + 1/4 - x
solution = secant(f,1,5,100)
print('The root found using secant is', solution)