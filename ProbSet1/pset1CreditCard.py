## Mit 6.00 Introduction to Computer Science Spring 2011
## Problem Set 1.  Introduction to Flow Control
## August 10 2016
## Write a probram to calculate interest and minimum Monthly payments
## for a credit Card 
## Input from the user for starting balance, interest rate, and minimum
## required payment


loan_amount=input("Enter your Credit Card balance in dollars and cents - ")
minPaymentRate=input("Enter the Minimum Payment rate - ")
interestRate=input('Enter the interest rate charged by you card provider - ')
balanceOutstanding=loan_amount 
monthlyInterestCharges = 0
minMonthlyPayment = 0
principlePaid=0

for month in months[1:12]
    monthlyInterestCharges = interestRate/12* balanceOutstanding
    minMonthlyPayment = balanceOutstanding * minPaymentRate
    if monthlyInterestCharges > minMonthlyPayment:
        print('Interest charges exceed the minimum payment, the debt cannot be repaid')
    balanceOutstanding = balanceOutstanding-minMonthlyPayment+monthlyInterestCharges
    principlePaid = minMonthlyPayment - monthlyInterestCharges
    
    


