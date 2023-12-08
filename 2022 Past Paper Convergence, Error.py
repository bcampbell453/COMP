# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:35:51 2023

@author: blath
"""

'''
QUESTION 1
Series convergence
a) valuate the series solution for N = 10, 100, 1000
b) Compute error for the same number of terms given true solution is pi

Must compute error using a true error and an estimated error
True error = assumes that true pi solution is known
Estimated error = assumes that true solution is not known


In written section, explain what definition was used for true and estimated error
(See pages)
'''

#Part a

import numpy as np

#Setting up code for series

N = 1000 # series length

start = 0 #starting value

approximation = np.zeros(N) #array of the series sums

place_in_series = np.zeros(N) #Stores number

true_error = np.zeros(N) #array of the errors for each sum from 1 to N

estimated_e = np.zeros(N) 
#same as above but uses the difference between 
#old and new values to calculate estimated error as difference 
#should be smaller the closer approximation gets to true value

true_ans = np.pi #the true solution to the series approximation


#loop to calculate sums
for i in range(1,N+1):
    #work out last value
    previous = (start*6.0)**0.5
    
    #make new value summing last to current
    start = start + 1.0/(i**2.0)
    
    #store each value in the approximation array
    approximation[i-1] = (start*6.0)**0.5
    
    #store the iteration in the place array
    place_in_series[i-1] = i 
    
    #Error calculations
    true_error[i-1] = np.absolute(approximation[i-1] - true_ans)
    estimated_e[i-1]  = np.absolute(approximation[i-1] - previous) 
    #print the value at each i along with associated errors and value of i itself
    #print('At point', i, 'The approximate value of series is', approximation[i-1], 'with true error:', true_error[i-1], 'and estimated error', estimated_e[i-1])
    
#Have to print approximations for N = 10, 100, 1000 along with their errors:

print('For N = 10:', 'Approximation is:', approximation[9], 'True error is:', true_error[9], 'Estimated error is:', estimated_e[9])

print('For N = 100:', 'Approximation is:', approximation[99], 'True error is:', true_error[99], 'Estimated error is:', estimated_e[99])

print('For N = 1000:', 'Approximation is:', approximation[999], 'True error is:', true_error[999], 'Estimated error is:', estimated_e[999])