
"""
Mortgage calculator for Kelly

Kelly needs a loan of GHs 1,000,000

Find amount Kelly needs to pay each month to be able to settle the loan.

"""

# Morgage Calclutor

# Welcome Header
print("\u0332".join("MORTGAGE CALCULATOR 1.0\n"))

# Key Variable Inputs
principal = float(input("What is the pricipal loan amount?:\n"))
years = int(input("What is the tenure of mortgage?:\n"))
interest = float(input("What is the annual interest rate?:\n"))

# Months in a year
months = 12 

# Mortgage calculator formula
mortgage_calculation = (1-(1+interest/(months*100))**(-months*years))/(interest/(months*100))

# Calculation for monthly payments
monthly_payments = principal/mortgage_calculation

# Calculation for total mamount
total_amount = monthly_payments * years * months

# Final Results
final = '''\
For a {} year mortgage loan of GHs {:,.2f}
at an annual interest rate of {:.1f}%
you pay GHs {:.2f} monthly'''

print('-'*40)

print(final.format(years, principal, interest, monthly_payments))

print('-'*40)

print("Total amount paid will be GHs {:,.2f}".format(total_amount))
print('-'*62)
print("Total interest to principal paid over period is GHs {:,.2f}".format(total_amount-principal))
print('-'*62)
print()