# -*- coding: utf-8 -*-
##"""
##Created on Sat Aug 27 22:38:45 2016

##@author: marka
##"""

# Problem Set 1, Problem 3
# A Program that calculates the minimum fixed monthly payment needed in 
# order to off a credit card balance within 12 months.

# Bisection method

print('')
print('Enter the outstanding balance on your Credit Card')
outBal = float(input('$ '))
print('Enter the annual interest rate on the Credit Card')
intRate = float(input('Decimal - '))
months = (range(1, 13))
lowerBound = outBal / 12  # the minimum payment will be more than the debit/12
# The monthly payment will be less than the debt with a full year of interest
upperBound = (outBal * (1 + intRate / 12)**12)/12
monPay = (lowerBound + upperBound)/2
intMon = 0     # The dollar value of the monthly interest
finalBal = outBal # at the start of the payment period the final balance = the debt

while abs(finalBal) > 0.01:
    finalBal = outBal # reset to the start of the payment period
    monPay = (lowerBound + upperBound)/2
    # determine the final balance owing at the end of 12 months
    for month in months:
        intMon = finalBal * intRate / 12
        finalBal = finalBal - monPay + intMon
    # if the final balance is positive the bisecting value becomes the new lower bound
    if finalBal > 0:
        lowerBound = monPay
    else:
        upperBound = monPay

ppay = str(round(monPay, 2)) # Printable monthly PAYment
pfin = str(round(finalBal, 2))
print('')
print('Results')
print('Monthly payment to pay off debt in 1 year: $ ' + ppay)
print('The final balance after 1 year is: $ ' + pfin)        