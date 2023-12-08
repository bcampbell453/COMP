# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 18:21:45 2023

@author: blath
"""

'''This is the whole divide the function 
by the root you find to make the others easier to find'''

import numpy as np

def poly_iter(A, t):
    # compute q(x) = f(x)/(x-t) and residual r
    # array A contains coefficients of f(x) 
    n = len(A)-1
    # q: array of integers to store coefficients of q(x)
    q=np.zeros(n,dtype=np.int8)
    r = A[n]
    for a in reversed(range(n)):
        s=A[a]
        q[a]=r
        r = s + r * t
    print('----------------------------------------')
    print('Coefficients a0, a1, a2, ..., an')
    print('of quotient a0+a1*x+a2*x^2+...an*x^n:') 
    print(q)
    print('----------------------------------------')
    print('Residual:')
    print(r)
    print('----------------------------------------')
    return []

#The q that this prints is in reverse order too

#A = np.array([ -24, 2, 1])
#t = 4
#for a function x**2 +2*x - 24
#COEFFICIENTS IN REVERSE ORDER!!!!
A = np.array([ -24, 2, 1])
#T is the number we devide by
t=4

poly_iter(A,t)
