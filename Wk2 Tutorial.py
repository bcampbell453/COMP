# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 17:54:36 2023

@author: blath
"""

import numpy as np
import matplotlib.pyplot as plt
'''
def squaresum(n) :
    # Initialise the sum to 0
    sm = 0
    # Iterate i from 1
    # to n finding
    # the square of i and
    # add to sum.
    for i in range(1, n+1) :
        if i%2 !=0:
            sm = sm + (i * i)
        else:
            continue
    return sm
    
    # Main Program
    # Specify n
n = 20
    # Call the function squaresum
sum_numbers = squaresum(n)
    # Print result on screen
print(sum_numbers)

#Zeros array with 20 elements
x = np.zeros(20)

#Filling the array with random numbers between 0 and 10:
N = 20
for i in range(0, N):    
    x[i] = np.random.rand(1)*10
    
#print(x)

for i in range(0,20):
    if 5 < x[i] < 6:
       print(i)


#Make an array of x and y coords and plot:
import matplotlib.pyplot as plt

x_plot = np.linspace(0,2*np.pi, 40)
y_plot = np.sin(x_plot)

plt.plot(x_plot, y_plot)
plt.show()

'''


#Error in a series approximation
N = 1000 # series length
start = 0 #starting value
approximation = np.zeros(N) #array of the series sums
place_in_series = np.zeros(N) #Stores number
true_error = np.zeros(N) #array of the errors for each sum from 1 to N
estimated_e = np.zeros(N) #same as above but uses the difference between 
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

print('For N = 10:', approximation[9], true_error[9], estimated_e[9])

print('For N = 100:', approximation[99], true_error[99], estimated_e[99])

print('For N = 1000:', approximation[999], true_error[999], estimated_e[999])


'''
plt.figure()
plt.plot(nn,pi_n)

plt.figure()
plt.loglog(nn,error_true,'-b',nn,error_ext,'.r')

plt.show()
'''