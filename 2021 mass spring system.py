# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 09:16:52 2023

@author: blath
"""

#Root finding of a polynomial
'''
Part a)
Given polynomial of fourth order, need to find two possible roots
'''

import numpy as np
import matplotlib.pyplot as plt

cm = 12
sm = 1500

f = lambda omega: omega**4 + 2*(cm)*omega**3 + 3*sm*omega**2 + cm*sm*omega + sm**2

coefficients = [1, 2*cm, 3*sm, cm*sm, sm**2]

roots = np.roots(coefficients)

print('Roots are:', roots)
print('=================================')

'''
part b)
    Smallest possible amount of work done on the second spring
    in its first 10 seconds using the smalleset absolute values 
    for omegas i and r if the system is subjected to initial 
    tensile force of 100N
'''

#Work done is product of force and distance travelled so need x(t)
#After the ten seconds then multiply it by the force of 100N?

omega_r = abs(-0.62301963)
omega_i = abs(24.03024141)
#print(omega_r, omega_i)

A_j = 0.1
phi = np.pi/8

def x(t):
    return A_j*(np.exp(omega_r*t))*(np.cos(omega_i*t + phi))


displacement = x(10)
print('Displacement is', displacement)

def wd(f,d):
    return f*d

work_done = wd(100, abs(displacement))

#Print work done to 2 decimal places
print(f'The smallest work done is {work_done:.2f} N') 

t = np.arange(0, 10.5, 0.01)
plt.plot(t, x(t))
plt.axvline(x=10, color='r', linestyle='--', label='t = 10')
plt.show()

