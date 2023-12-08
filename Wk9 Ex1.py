# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:46:33 2023

@author: blath
"""
import numpy as np

def calculate_dx (a, b, n):
    return (b-a)/float(n)
def rect_rule (f, a, b, n):
    total = 0.0
    dx = calculate_dx(a, b, n)
    for k in range (0, n):
        total = total + f((a + (k*dx)))
    return dx*total

def func(x):
    return x**2 + 4*x - 12

print(rect_rule(func, -10, 10, 1000))