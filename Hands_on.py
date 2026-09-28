#inputs 

age = int(input("Enter your age: "))
rev = float(input("Enter your revenue: "))
cc = int(input("Enter your credit score: "))
yrs_b = int(input("Enter the number of years you have been a customer: "))
has_defaulted = input("Have you defaulted on a loan before? (yes/no): ") == "yes"
collat = input("Do you have collateral? (yes/no): ") == "yes"
collat_val = float(input("Enter the value of your collateral: ")) if collat else 0.0



max_Limit = 0 
base_fee = 0.0

#baseline requirements
if age >= 21 and yrs_b >= 2 and has_defaulted is False:
    max_Limit =  0.03 * rev



    if cc >= 720 and collat_val >= max_Limit:
        if rev >= 50000:
            base_fee = max_Limit * 0.015
            print("Tier 1")

        else:
             base_fee = max_Limit * 0.025
             print("Tier 1.2")
            


    if cc <= 620 or cc < 720 and collat_val >= max_Limit:
        max_Limit = 0.15 * rev
        if yrs_b >= 5:
            base_fee = max_Limit * 0.02
            print("Tier 2")
        else:
            base_fee = max_Limit * 0.035
            print("Tier 2.2")


    if cc < 620:
        print("You are not eligible for a credit card due to low credit score.")

else:
    print("You are not eligible for a credit card due to age, years as a customer, or previous defaults.")



       