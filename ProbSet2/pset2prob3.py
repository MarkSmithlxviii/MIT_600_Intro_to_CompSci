# -*- coding: utf-8 -*-
"""
Uses Newton's method to find and return a root of a polynomial function.
Returns a tuple containing the root and the number of iterations required to
get to the root.
Example:
>>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)         #x4 + 3.0x3 + 17.5x2 - 13.39
>>> x_0 = 0.1
>>> epsilon = .0001
>>> print compute_root(poly, x_0, epsilon)
(0.80679075379635201, 8)
poly: tuple of numbers, length > 1.
Represents a polynomial function containing at least one real root.
The derivative of this polynomial function at x_0 is not 0.
x_0: float
epsilon: float > 0
returns: tuple (float, int)

Created on Mon Sep  5 23:56:19 2016

@author: marka
"""

# use the functions that were written for problem set 2 problems 1 and 2.
def evaluate_poly(poly, x):
    expn = 0
    f_of_x = 0
    for coeff in poly:
        #print(expn, coeff)        
        f_of_x = f_of_x + coeff*(x**expn)
        expn += 1
    return f_of_x

def compute_deriv(poly):
    expon = 0
    deriv = ()
    for coeff in poly:
        newcoeff = expon * coeff
        deriv = deriv + (newcoeff,)
        expon += 1
    #print (deriv)
    return deriv    

def compute_root(poly, x_0, epsilon):
    deriv = compute_deriv (poly)
    deriv = deriv [1:]  #The deriv function returns 0 at the coefficient and this needs to be dropped to properly evaluate the derivative at x 
    print (deriv)
    loopCounter = 0
    while abs(evaluate_poly(poly, x_0)) > epsilon:
        x_0 = x_0 - (evaluate_poly (poly, x_0) / evaluate_poly (deriv, x_0))
        loopCounter += 1
    return (x_0, loopCounter)