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
intRate = float(input('Decimal'))
months = (range(1, 13))
finalBal = outBal
intMon = 0     # The dollar value of the monthly interest
monPay = 0     # The monthly payment that will be iterated at $10 per iteration

while finalBal > 0:
    finalBal = outBal
    monPay += 10
    for month in months:
        # print (month, finalBal)
        intMon = finalBal * intRate / 12
        finalBal = finalBal - monPay + intMon
ppay = str(round(monPay, 2)) # Printable monthly PAYment
pmon = str(month)
pbal = str(round(finalBal,2))
print('')
print('Results')
print('Monthly payment to pay off debt in 1 year: $' + ppay)
print('Number of months needed: ' + pmon)   
print('The final balance is $' + pbal) 
        
        
        