# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 12:25:51 2023

@author: blath
"""

'LAGRANGE MULTIPLIER TECHNIQUE FOR MULTIVARIATE CONSTRAINED OPTIMISATION'

import numpy as np
from scipy.optimize import minimize

def objective(X):
    x, y = X
    return (x-5)**2 + (y-8)**2


#Constraint function
def eq(X):
    x, y = X
    return x*y - 5

import autograd.numpy as np
from autograd import grad

def F(L):
    'Augmented Lagrange function'
    x, y, _lambda = L
    return objective([x, y]) +_lambda * eq([x, y])

#Gradients of the lagrange function
dfdL = grad(F,0)

#find L that returns all the zeros in this function
def obj(L):
    x, y, _lambda = L
    dFdx, dFdy, dFdlam = dfdL(L)
    return [dFdx, dFdy, eq([x,y])]

from scipy.optimise import fsolve

x, y, _lam = fsolve(obj, [0.0, 0.0, 0.0])

print('The answer is at', x,y)