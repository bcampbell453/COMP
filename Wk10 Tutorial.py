# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:06:21 2023

@author: blath
"""

#Ex1, find differential

import sympy as sym
# define some symbols
x = sym.Symbol('x')
y = sym.Symbol('y')
a = sym.Symbol('a')
c = sym.Symbol('c')
dydx = sym.Symbol('dydx')

# define the function y(x)
y=c*sym.sin(a*x)

# compute derivative
dydx = sym.diff(y, x)

# print them
#print('function y(x): ',y)
print('derivative dy/dx: ',dydx)

#Exercise 2, second derivative
d2ydx2 = sym.Symbol('d2ydx2')
d2ydx2 = sym.diff(dydx, x)

print('derivative d2y/dx2: ', d2ydx2)

#New function z(x)
z = dydx + d2ydx2
print('z(x) =', z)

#New func s(x)
s = (1/y)*dydx
print('s(x) = ', s)

s_new = sym.simplify(s)
print('Simplified s =', s_new)

s_taylor = sym.series(s_new, x)
print('Taylor series of s =', s_taylor)




import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline
a = -10
b = 10
N = 10


def func(x):
    return x**2 + 4*x - 12


