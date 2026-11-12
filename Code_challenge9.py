
# Yask 1
loan_amount = float(input("Enter the loan amount: "))
loan_prd = int(input("Enter the loan term in years: "))
interest_rate = 0.0025

months = loan_prd * 12
monthly_principal = loan_amount / months
remaining_loan = loan_amount

print("\nMonth\tPayment\t\tInterest\tPrincipal\tRemaining Loan")

for i in range(months):
    interest = remaining_loan * interest_rate
    monthly_payment = monthly_principal + interest
    remaining_loan = remaining_loan - monthly_principal

    print(str(i + 1) + "\t" + 
        format(monthly_payment, ".2f") + "\t\t" +
        format(interest, ".2f") + "\t\t" +
        format(monthly_principal, ".2f") + "\t\t" +
        format(remaining_loan, ".2f"))


#2 Task

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")

    for k in range(2 * i + 1):
        if k == 0 or k == 2 * i or i == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()
    
#3 Task

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows - 1 or j == rows - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


