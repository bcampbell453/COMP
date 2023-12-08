# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:30:25 2023

@author: blath
"""

def objective(X):
    x, y = X
    return (160*x**0.66)*(y**0.33)

#This is the constraint function that has lambda as a coefficient.

def eq(X):
    x, y = X
    return 20*x + 0.15*y - 20000.


import autograd.numpy as np
from autograd import grad

def F(L):
    'Augmented Lagrange function'
    x, y, _lambda = L
    return objective([x, y]) + _lambda *eq([x, y])

# Gradients of the Lagrange function
dfdL = grad(F, 0)

# Find L that returns all zeros inthis function.
def obj(L):
    x, y, _lambda = L
    dFdx, dFdy, dFdlam = dfdL(L)
    return [dFdx, dFdy, eq([x, y])]

from scipy.optimize import fsolve

x, y, _lam = fsolve(obj, [1., 1.,1.0])
print(f'The answer is at {x, y}')
