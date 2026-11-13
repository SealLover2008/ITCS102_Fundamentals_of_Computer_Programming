# Yask 1
loan_amount = float(input("Enter the loan amount: "))
loan_prd = int(input("Enter the loan term in years: "))
interest_rate = 0.00256

months = loan_prd * 12
monthly_principal = loan_amount / months
remaining_loan = loan_amount

print("\nMonth\tPayment\t\tInterest\tPrincipal\tRemaining Loan")

for r in range(months):
    interest = remaining_loan * interest_rate
    monthly_payment = monthly_principal + interest
    remaining_loan = remaining_loan - monthly_principal
    print(str(r + 1) + "\t" + "%.2f" % monthly_payment + "\t\t" + "%.2f" % interest + "\t\t" + "%.2f" % monthly_principal + "\t\t" + "%.2f" % remaining_loan)
#2 Task

rows = int(input("Enter number of rows: "))

for x in range(rows):
    for y in range(rows - x - 1):
        print(" ", end="")
        
    for z in range(2 * x + 1):
        if z == 0 or z == 2 * x or x == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
#3 Task

rows = int(input("Enter number of rows: "))

for a in range(rows):
    for b in range(rows):
        if a == 0 or a == rows - 1 or b == rows - a - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()