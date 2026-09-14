age = int(input("How Old are you?"))
is_employed = bool(input("Are you employed? True or False"))
credit_score = eval(input("What is your credit score?"))
annual_outcome = eval(input("What is your annual income?"))
has_collateral = bool(input("Do you have Collateral? True or False"))

if age <= 21 and is_employed == True:
  if credit_score >= 750:
    base_interest = 5.0%
  elif annual_income >= 100000:
    base_interest = 4.5%
if credit_score <= 600 or credit_score >= 750:
  base_interest = 8.0%
  elif:
    has_collateral == True:
    base_interest = 7.0%
else: 
  annual_outcome < 40,000:
  base_interest = 9.5%






else:
  print("You are not eligible for a loan")

 