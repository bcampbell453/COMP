# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 12:21:39 2023

@author: blath
"""

import numpy as np
def linearsolver(A,b):
    n = len(A)
    
    #Initialise solution vector as an empty array
    x = np.zeros(n)
    
    #Join A and use concatenate to form anaugmented coefficient matrix
    M = np.concatenate((A,b.T), axis=1)
    
    #partial pivoting to improve matrix stability
    #Gaussian elimination to get matrix in upper triangular form
    for k in range(n):
        for i in range(k,n):
            if abs(M[i][k]) > abs(M[k][k]):
                M[[k,i]] = M[[i,k]]
            else:
                pass
                for j in range(k+1,n):
                    #q is a multiplier
                    q = M[j][k] / M[k][k]
                    #matrix is updated
                    for m in range(n+1):
                        M[j][m] += -q * M[k][m]
                        
#Python starts indexing with 0, so the last element is n-1
    #Back substitution to find x
    x[n-1] =M[n-1][n]/M[n-1][n-1]
    
    #We need to start at n-2, because ofPython indexing
    for i in range (n-2,-1,-1):
        z = M[i][n]
        for j in range(i+1,n):
            z = z - M[i][j]*x[j]
        x[i] = z/M[i][i]
    return x


A=np.array([[10., -2.0, 0.],[-10., 20., -10.],[0., 20., 10.]])
b=np.array([[19.62, 29.43, 24.525]])

print(linearsolver(A,b))