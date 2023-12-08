# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 11:13:13 2023

@author: blath
"""



#===================================================

'''
#Do algebra first and then do numerical stuff

import matplotlib.pyplot as plt
#plt.style.use('seaborn-white')
import numpy as np
import sympy as sym

k_a = 9
k_b = 2
L_a = 10
L_b = 10
F1 = 2
F2 = 4

x1sym = sym.Symbol('x1sym')
x2sym = sym.Symbol('x2sym')
g1_x1sym = sym.Symbol('g1_x1sym')
g2_x2sym = sym.Symbol('g2_x2sym')
h11_g1_x1sym = sym.Symbol('h11_g1_x1sym')
h12_g1_x2sym = sym.Symbol('h12_g1_x2sym')
h21_g2_x1sym = sym.Symbol('h21_g2_x1sym')
h22_g2_x2sym = sym.Symbol('h22_g2_x2sym')
f = sym.Symbol('f')


f = (0.5*9((sym.sqrt(x1sym**2 + (10-x2sym)**2))-10)**2 + 0.5*2((sym.sqrt(x1sym**2+(10+x2sym)**2))-10)**2 - 2*x1sym - 4*x2sym)
g1_x1sym = sym.diff(f, x1syms)
g2_x2sym = sym.diff(f, x2syms)
h11_g1_x1sym = sym.diff(g1_x1sym, x1sym)
h12_g1_x2sym = sym.diff(g1_x1sym, x2sym)
h21_g2_x1sym = sym.diff(g2_x2sym, x1sym)
h22_g2_x2sym = sym.diff(g2_x2sym, x2sym)


syms X, Y;
%f = X - Y + 2*X^2 + 2*X*Y + Y^2;
f=X^2+12*X*Y+Y^2+6*X
%Initial Guess (Choose Initial Guesses):
    x(1) = 1;y(1) = -5;
    e = 10^(-8); 
    % Convergence Criteriai = 1;
    % Iteration Counter% Gradient and Hessian Computation:
    df_dx = diff(f, X);df_dy = diff(f, Y);

'''
#======================================================================

#======================================================================

#WORKING SOLUTIONS:
    
#For Golden Ratio:
import numpy as np

def gsection(ftn, xl, xm, xr, tol = 1e-9):
    # applies the golden-section algorithm to maximise ftn
    # we assume that ftn is a function of a single variable
    # and that x.l < x.m < x.r and ftn(x.l), ftn(x.r) <= ftn(x.m)
    #
    # the algorithm iteratively refines x.l, x.r, and x.m and
    # terminates when x.r - x.l <= tol, then returns x.m
    # golden ratio plus one
    gr1 = 1 + (1 + np.sqrt(5))/2
    #
    # successively refine x.l, x.r, and x.m
    fl = ftn(xl)
    fr = ftn(xr)
    fm = ftn(xm)
    while ((xr - xl) > tol):
        if ((xr - xm) > (xm - xl)):
            y = xm + (xr - xm)/gr1
            fy = ftn(y)
            if (fy >= fm):
                xl = xm
                fl = fm
                xm = y
                fm = fy
            else:
                xr = y
                fr = fy
        else:
            y = xm - (xm - xl)/gr1
            fy = ftn(y)
            if (fy >= fm):
                xr = xm
                fr = fm
                xm = y
                fm = fy
            else:
                xl = y
                fl = fy
    print(ftn(xm))
    return(xm)
    

xl=0
xm=5
xr=10
def ftn(x):
    return 2*np.sin(x) - (x**2)/10
print('Golden Ratio', gsection(ftn, xl, xm, xr, tol = 1e-9))

#====================================================

#====================================================
#OPTIMISATION OF SPRING SYSTEM

import numpy as np
import matplotlib.pyplot as plt

x1_a = np.linspace(-10,10,100)
x2_a = np.linspace(-10,10,100)

x1, x2 = np.meshgrid(x1_a, x2_a, indexing='ij')

ka=9.
kb=2.
La=10.
Lb=10.
F1=2.
F2=4.

PE = 0.5*(ka*((x1**2+(La-x2)**2)**0.5 - La)**2)+0.5*(kb*((x1**2+(Lb+x2)**2)**0.5 - Lb)**2)-F1*x1-F2*x2

plt.figure()
plt.contour(x1,x2,PE,100)
plt.colorbar()
plt.xlabel('x_1')
plt.ylabel('x_2')
plt.show()
