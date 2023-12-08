# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 10:32:08 2023

@author: blath
"""

#Scipy codes such as fsolve or root could also be used 


import numpy as np

#Newton Raphson, secant and python modules

def newton(f,Df,x0,epsilon,max_iter):
    '''Approximate solution of f(x)=0 by Newton's method.

    Parameters
    ----------
    f : function
        Function for which we are searching for a solution f(x)=0.
    Df : function
        Derivative of f(x).
    x0 : number
        Initial guess for a solution f(x)=0.
    epsilon : number
        Stopping criteria is abs(f(x)) < epsilon.
    max_iter : integer
        Maximum number of iterations of Newton's method.

    Returns
    -------
    xn : number
        Implement Newton's method: compute the linear approximation
        of f(x) at xn and find x intercept by the formula
            x = xn - f(xn)/Df(xn)
        Continue until abs(f(xn)) < epsilon and return xn.
        If Df(xn) == 0, return None. If the number of iterations
        exceeds max_iter, then return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> Df = lambda x: 2*x - 1
    >>> newton(f,Df,1,1e-8,10)
    Found solution after 5 iterations.
    1.618033988749989
    '''
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None


#function underconsideration:
f = lambda x: x**2 + 4*x - 12
df= lambda x: 2*x + 4
x0=1
epsilon=0.0001
max_iter=100
solution = newton(f,df,x0,epsilon,max_iter)
print(solution)

#How newton raphson works:
'''
Newton's method, is an iterative numerical technique for finding the roots of a real-valued function. It is particularly useful for finding the roots of nonlinear equations. The method is based on linear approximation and involves updating a current guess to get a better estimate of the root in each iteration.
Start with initial guess, formulate iterative root - next root is last root minus func/dfuncdx
Repeat iterations until solution has been found
An error bound to stop iterations can be set up or the max number of iterations can be reached
Newton may not converge depending on initial guess
'''

#How secant works:
'''
Approximates the derivative instead of using actual derivative, 
approximates derivative by computing slope of secant line between
two points of the graph of the function.

Guess x0, x1 to determine secant line
Calculate the slope via m = (f(x1) - f(x0))/(x1-x0)
The x intersect of the secant line is found and used as the next approximation
x2 = next approximation = x1 - f(x1)/m
update x0 and x1 to x1 and x2 and repeat until root is found or error bound is reached

Secant is generally slower than newton but faster than bisection
May not converge when function is near horizontal or changes direction suddenly
'''
def secant(f,a,b,N):
    '''Approximate solution of f(x)=0 on interval [a,b] by the secant method.

    Parameters
    ----------
    f : function
        The function for which we are trying to approximate a solution f(x)=0.
    a,b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    N : (positive) integer
        The number of iterations to implement.

    Returns
    -------
    m_N : number
        The x intercept of the secant line on the the Nth interval
            m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        The initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0
        for some intercept m_n then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iterations, the secant method fails and return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> secant(f,1,2,5)
    1.6180257510729614
    '''
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Secant method fails.")
            return None
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))

f = lambda x: x**2 + 4*x - 12
solution = secant(f,1,5,25)
print(solution)
