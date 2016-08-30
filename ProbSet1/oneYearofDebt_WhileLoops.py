# -*- coding: utf-8 -*-
##"""
##Created on Sat Aug 27 22:38:45 2016

##@author: marka
##"""

# A Program that calculates the minimum fixed monthly payment needed in 
# order to off a credit card balance within 12 months.

print('Enter the outstanding balance on your Credit Card')
outBal = float(input('$ '))
print('Enter the annual interest rate on the Credit Card')
intRate = float(input('Decimal - '))
months = (range(1, 13))
finalBal = outBal
intMon = 0     # The dollar value of the monthly interest
monPay = 0     # The monthly payment that will be iterated at $10 per iteration
month = 0

while finalBal > 0:
    finalBal = outBal
    monPay += .001
    month = 0
    while finalBal > 0 and finalBal <= (outBal + monPay) and month < 12:
        # three conditions, the debt has not been paid, it is decreasing and 
        # the time to pay is less than a year.  if the debt is increasing the  
        # loop terminates and the payment is increased if months exceed a year 
        # the loop terminates and the monthly payment is increased.  if the 
        # remaining debt goes less than 0 both loops terminate
        # print (month, finalBal)
        month +=1
        intMon = finalBal * intRate / 12
        finalBal = finalBal - monPay + intMon
ppay = str(round(monPay, 2)) # Printable monthly PAYment
pmon = str(month)
pfin = str(round(finalBal, 2))
print('')
print('Results')
print('Monthly payment to pay off debt in 1 year: $ ' + ppay)
print('Number of months needed: ' + pmon) 
print('The final balance after 1 year is: $ ' + pfin)   

        
        