# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:57:18 2023

@author: blath
"""

'''
Equations of motion and finding general solutions.
'''

'''
Part a)
    Show that eqn 4.2 is the general solution to 4.1
    using appropriate python package
'''

from sympy import symbols, diff, cos, exp, Eq, solve, Function

#Defining time
t = symbols('t')

#Symbols for 4.1
m, b, k = symbols('m b k')

#Symbols for 4.2
A_0, omega, phi = symbols('A_0 omega phi')

#Defining x
x = Function('x')(t)

#Equation 4.2
eqn4_2 = Eq(x, A_0*exp(-b*t/2*m)*cos(omega*t+phi))

dxdt = diff(x, t)

d2xdt2 = diff(x, t, t)

#Defining 4.1
eqn4_1 = Eq(0,  m*d2xdt2 + b*dxdt + k*eqn4_2.rhs)

eqn4_1_simplified = eqn4_1.simplify()

sols_for_A0 = solve(eqn4_1_simplified, A_0)

if all(eqn4_1_simplified.subs(A_0, sol).simplify() == True for sol in sols_for_A0):
    print("Equation 4.2 is the general solution to Equation 4.1.")
else:
    print("4.2 is not the general solution")
    
    
'''
Part b
    By making an appropriate substitution in Equation Q4.1, 
    show that the instantaneous frequency of a damped oscillator
    can be described by Equation Q4.3.
'''


