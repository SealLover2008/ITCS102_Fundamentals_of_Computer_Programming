#task 1

loan_amount = float(input("Enter the loan amount: "))
loan_prd = int(input("Enter the loan term in years: "))
interest_rate = 0.00256

for i in range(24):
    monthly_payment = loan_amount * interest_rate / (1 - (1 + interest_rate) ** (-loan_prd * 12))
    for y in range(loan_prd):
        print(f"Month {i + 1}: Payment: {monthly_payment:.2f, i - 1}")
        
      

