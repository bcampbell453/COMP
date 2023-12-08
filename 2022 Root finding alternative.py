# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:12:01 2023

@author: blath
"""

'''
 a) Use appropriate root finding technique to determine any
value of x in 0<x<4 where xn = xn+1
'''

import numpy as np

error = 0.001
iterations = 0

#for x in np.arange(0.1,4,0.01):
#    iterations += 1
#    if 0< ((1/(np.sin(x)))+1/4-x) <= 0 + error:
#        print(f"Root found at x = {x} after {iterations} iterations.")
#    else:
#        continue
    
'''
Part b) 
    Closed root interval finding technique to find a root
    within the range (0,4) with all terms placed on rhs
'''

"A closed root findind method would be bisection method"

#Root finding by bisection

def bisection(f,a,b,N,es):
    if f(a)*f(b) >= 0:
       print("a and b do not bound a root")
       return None 
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if abs(f_m_n) <= es:
           print(m_n, "Number of iterations:", n, "the error is", abs(f_m_n))
           break
        elif f(a_n)*f_m_n < 0:
           a_n = a_n
           b_n = m_n
        elif f(b_n)*f_m_n < 0:
           a_n = m_n
           b_n = b_n
        elif f_m_n == 0:
           print("Found exact solution.")
           return m_n
        else:
           print("Bisection method fails.")
           return None
       
            
    return (a_n + b_n)/2
            
#Define the function that bisection method is to be applied to:
f = lambda x: 1/(np.sin(x)) + 1/4 - x

#Root finding
root = bisection(f, 0.1, 4, 1000, error)

'''
Part c)
    Use open root finding to find the same root
    in the same domain
'''

#using secant as f looks difficult to differentiate

def secant(f,a,b,N, es):
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if abs(f_m_n) <= es:
           print(m_n, "Number of iterations:", n, "the error is", abs(f_m_n))
           break
        elif f(a_n)*f_m_n < 0:
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
solution = secant(f,0.1,4,1000, error)
#print('The root found using secant is', solution)
