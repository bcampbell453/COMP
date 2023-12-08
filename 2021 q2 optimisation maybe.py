# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 14:27:16 2023

@author: blath
"""

#Need to root find beta and then sub the two lowest roots into
#eqn 3 to find the lowest beta value.
#I'm not 100% sure this is right as last question used root finding,
#This could be optimisation? >That is root finding.'

'''
Question 2
    Determine two lowest values for natural frequency that satisfy
    beta equation
    
    m = 7850
    L = 0.9
    E = 200e9
    I = 3.255e-11
    
    beta = ((((2*np.pi*f_i)**2)*((m*L**3)/E*I))**(1/4))
'''


import numpy as np
from scipy.optimize import fsolve

m = 7850
L = 0.9
E = 200e9
I = 3.255e-11


def y_beta(beta):
    return np.cosh(beta)*np.cos(beta) + 1

for i in np.arange(0.1, 10, 1): 
    guesses_beta = i

    beta_root = fsolve(y_beta, guesses_beta)
    
    
    f_i = ((1/np.pi)*np.sqrt(((beta_root**4)*E*I)/(m*L**3)))
    print('The beta is', beta_root, 'for f_i:', f_i)
    

