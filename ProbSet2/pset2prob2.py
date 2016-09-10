# -*- coding: utf-8 -*-
"""
Computes and returns the coefficints of the derivative of a polynomial function.
If the derivative is 0, returns (0.0).

Example:
>>> poly = (-13.39, 0.0, 17.5, 3.0,  1.0)  # x^4, + 3.0x^3 + 17.5x^2 - 13.39
>>> print (compute_deriv(poly))            #4x^3 + 9x^2 + 35x
(0.0, 35.0, 9.0, 4.0)

poly: tuple of numbers, length > 0
returns: tuple of numbers


Created on Wed Aug 31 03:39:51 2016

@author: marka

"""

def compute_deriv(poly):
    expon = 0
    deriv = ()
    for coeff in poly:
        newcoeff = expon * coeff
        deriv = deriv + (newcoeff,)
        expon += 1
    #print (deriv)
    return deriv    