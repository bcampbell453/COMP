# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:37:13 2023

@author: blath
"""
'''
Part a)
    Written on paper, describe the method the code is trying to use

Part b) 
    Correct errors in code with justification and identification
'''
import numpy as np
#THEIR CODE

MAX_ITER = 1000000

#Here they have said deg instead of def when attempting to define the function
'''
deg func( x ):
    return (x**3 - 4*(x*2) + 10)
'''
#Correction:
def funct( x ):
#Have changed x*2 to x**2, presuming its meant to be squared
#Have also removed the brackets as this isnt necessary
    return x**3 - 4*(x**2) + 10


#THere are semicolon as well as colon here and 
#it should be b in the bracket not c
#And a function was not defined here
def Code(func, a , b):
    #Changing the condition here as it's if the product is positive that the values are wrong
    if func(a) * func(b) >= 0:
        print("You have not assumed correct values of a and b")
        return -1
    c = a
    c_trueval = ((-5+np.sqrt(41))/2)
    for i in range(MAX_ITER):
        c_old = c
        #The formula for c is wrong, I have corrected it
        #c = (b * func(b) - a * func(a))/ (func(c) - func(a))
        c =  (a * func(b) - b * func(a))/ (func(b) - func(a))
        absolute_error_true = abs(c - c_trueval)
        relative_error_true = absolute_error_true*c
        #It should be if c is equal to zero that the code breaks
        if func(c) == 0:
            print("The value of root is : " , '%.4f' %c, 'relative error:', relative_error_true)
            break
            
        elif func(b) * func(a) < 0:
            # it should be b = c here not a
            b = c
        else:
            a = c
            
    #The indentatino of this is wrong and it shoild come when the function breaks
    #print("The value of root is : " , '%.4f' %c)
    
    
'''
Part c) using the code to find roots
'''

f = lambda x: x**2 + 5*x -4

root = Code(f, -1, 1)
#print(root)

'''
Part d) Modify code to calculate relative true error,
    What alternative root finding method might result#
    in an improved approximation to the root?
    
    
False position can be slow to converge so a better method
would be one that converges faster which in this case
could be NR as the function is well behaved.

Alternatively could modify the false position method
to ensure that a bound does not remain unchanged
for prolonged periods of time and ensures convergence
occurs more quickly.
'''

