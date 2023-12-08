# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:42:26 2023

@author: blath
"""
import numpy as np
import matplotlib.pyplot as plt
#CONVERGENCE OF ROOT FINDING METHODS

#Finding one of the two roots using newton raphson method:

def newton(f,df,x0,error,max):
    xn = x0
    for n in range(0, max):
        f_xn = f(xn)
        if abs(f_xn) < error:
            print('appropriate root approximation found after', n, 'iterations')
            return xn
        df_xn = df(xn)
        if df_xn == 0:
            print('No solution found, zero derivative')
            return None
        xn = xn - f_xn/df_xn
    print('Maximum iterations have been exceeded, no solution found')
    return None
    
f = lambda x: x**2 + 4*x - 12
df = lambda x: 2*x + 4

Root = newton(f, df, 0.1, 0.01, 10)
print('The root is:', Root)

#Finding a root over various N iterations, then plotting these roots

# import modules ----------------------------------------
import math
import numpy as np
import matplotlib.pyplot as plt


# definition of function --------------------------------

# Newton 
def newton2(f,Df,x0,N):
    xn = x0
    for n in range(0,N):
        fxn = f(xn)
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    return xn


# Secant
def secant(f,a,b,N):

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


# ----------------------------------------------------------------------------------------
# main program ------------------------------------
n_max=20

n_array_N   = np.zeros(n_max-1)
sol_array_N = np.zeros(n_max-1)
fun_array_N = np.zeros(n_max-1)

n_array_S   = np.zeros(n_max-1)
sol_array_S = np.zeros(n_max-1)
fun_array_S = np.zeros(n_max-1)

# ----------------------------------------------------------------------------------------

f = lambda x: x**2 + 4*x - 12
df= lambda x: 2*x + 4

# Initial guess for Newton
x0=1

# Initial a and b for secant
a=1
b=3

for i in range(1,n_max):
    solution = newton2(f,df,x0,i)
    n_array_N[i-1] = i  
    sol_array_N[i-1] = solution
    fun_array_N[i-1] = np.absolute(f(solution))

    solution = secant(f,a,b,i)
    n_array_S[i-1] = i  
    sol_array_S[i-1] = solution
    fun_array_S[i-1] = np.absolute(f(solution))

plt.figure()
plt.plot(n_array_N,sol_array_N, '-o',n_array_S,sol_array_S, '-o')
plt.xlabel("Number of iterations")
plt.ylabel("Solution")
plt.xlim(0,n_max)

plt.figure()
# plot the error definrd as f(solution)
plt.semilogy(n_array_N,fun_array_N, '-o',n_array_S,fun_array_S, '-o')
# plot a couple of scaling lines to assess convergence rate
plt.semilogy(n_array_S,np.exp(-2.0*n_array_S))
plt.semilogy(n_array_S,np.exp(-2.5*n_array_S))
plt.xlabel("Number of iterations")
plt.ylabel("Error, defined as f(solution)")
plt.xlim(0,n_max)


# ----------------------------------------------------------------------------------------
f = lambda x: math.sin(x) * math.exp(x**0.1)
df= lambda x: (math.exp(x**0.1)*math.sin(x))/(10*x**(9/10))+math.exp(x**0.1)*math.cos(x)

# Initial guess for Newton
x0=4

# Initial a and b for secant
a=1
b=4

for i in range(1,n_max):
    solution = newton2(f,df,x0,i)
    n_array_N[i-1] = i  
    sol_array_N[i-1] = solution
    fun_array_N[i-1] = np.absolute(f(solution))

    solution = secant(f,a,b,i)
    n_array_S[i-1] = i  
    sol_array_S[i-1] = solution
    fun_array_S[i-1] = np.absolute(f(solution))

plt.figure()
plt.plot(n_array_N,sol_array_N, '-o',n_array_S,sol_array_S, '-o')
plt.xlabel("Number of iterations")
plt.ylabel("Solution")
plt.xlim(0,n_max)

plt.figure()
# plot the error defined as f(solution)
plt.semilogy(n_array_N,fun_array_N, '-o',n_array_S,fun_array_S, '-o')
# plot a couple of scaling lines to assess convergence rate
plt.semilogy(n_array_S,np.exp(-2.0*n_array_S))
plt.semilogy(n_array_S,np.exp(-2.5*n_array_S))
plt.xlabel("Number of iterations")
plt.ylabel("Error, defined as f(solution)")
plt.xlim(0,n_max)

'Semilogy creates a plot with a logarithmic scale'


plt.show()
