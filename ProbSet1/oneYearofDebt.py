# -*- coding: utf-8 -*-
##"""
##Created on Sat Aug 27 22:38:45 2016

##@author: marka
##"""

# A Program that calculates the minimum fixed monthly payment needed in 
# order to off a credit card balance within 12 months.

print('Enter the outstanding balance on your Credit Card')
outBal = float(input('$'))
print('Enter the annual interest rate on the Credit Card')
intRate = float(input('$'))
months = (range(1, 12))

while outBal > 0:
    for month in months:
        