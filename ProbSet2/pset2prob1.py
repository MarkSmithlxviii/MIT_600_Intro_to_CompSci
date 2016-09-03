# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 22:45:21 2016

@author: marka

MIT OCW 6.00 Intro to Comp Sci Problem Set 2 Problem 1

Computes the polynomial finction for a given value x.  Returns that value.

Example:
>>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)  # f(x)= 7x^4 + 9.3x^3 + 5.0x^2
>>> x = -13
>>>print (evaluat_poly(poly,x))  #f(-13)=7(-13)^4+9.3(-13)^3+5.0(-13)^2
1880339.9
poly: tuple of numbers, length > 0
x: number
returns: float
"""

def evaluate_poly(poly, x):
    expn = 0
    f_of_x = 0
    for coeff in poly:
        print(expn, coeff)        
        f_of_x = f_of_x + coeff*(x**expn)
        expn += 1       
    print('f(x)={0:.2f}'.format(f_of_x))