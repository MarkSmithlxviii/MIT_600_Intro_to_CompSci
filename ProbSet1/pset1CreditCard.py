## Mit 6.00 Introduction to Computer Science Spring 2011
## Problem Set 1.  Introduction to Flow Control
## August 10 2016
## Write a probram to calculate interest, minimum Monthly payments
## and the final balance at the end of 12 months for a credit Card 
## Input from the user for starting balance, interest rate, and minimum
## required payment

print("Enter your Credit Card balance in dollars and cents - ")
loan_amount = float(input())
print("Most institutions require a minimum payment that is a portion of")
print("the balance that is still owed.  Typical minimum payments are 2% of") 
print("outstanding Balance.")
print("Enter the Minimum Payment rate - Example for 2% enter 0.02")
minPayRate = float(input())
print('Enter the interest rate charged by you card provider as a decimal.')
print('Example for 18% enter 0.18')
intRate = float(input())
balOutStdg=loan_amount  # This will be the outstandig balance at the end of the
#                       # Calculation Period
monIntChgs = 0          # The dollar value of the monthly interest
minMonPay = 0           # The dolar value of the minimum monthly payment
princePd=0              # The dollar value of principle paid monthly
months = range(1,13)
totalPaid = 0
intTotalPaid = 0

# enhancements add a dict of months, and query the OS for today's date
# have the text for next payment and then the named months for a year 
# after that.

for month in months:
    monIntChgs = intRate / 12 * balOutStdg
    minMonPay = balOutStdg * minPayRate
    if monIntChgs > minMonPay:
        print('Interest charges exceed the minimum payment, ')
        print('the debt cannot be repaid if only the minimum payment is made.')
    princePd = minMonPay - monIntChgs
    balOutStdg = balOutStdg - princePd
    totalPaid += minMonPay
    intTotalPaid += monIntChgs
    print('')
    print('Month: {0}' .format(month))
    print('')
    print('The interest charges for month {0} are ${1:.2f}'.format(month, monIntChgs) )
    print('The minimum payment for month {0} is ${1:.2f}'.format(month, minMonPay))
    print('The principle paid for month {0} is ${1:.2f}'.format(month, princePd))
    print('The outstanding balance at the end of month {0} is ${1:.2f}'.format(month, balOutStdg))
print('')
print('')
print('The total amount paid over 12 months is:            ${0:.2f}'.format(totalPaid))
print('The outstanding balance at the end of 12 months is: ${0:.2f}'.format(balOutStdg))