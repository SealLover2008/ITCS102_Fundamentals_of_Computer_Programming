# inputs

age = int(input("Enter your age: "))
rev = float(input("Enter your revenue: "))
cc = int(input("Enter your credit score: "))
yrs_b = int(input("Enter the number of years you have been a customer: "))
has_defaulted = input("Have you defaulted on a loan before? (yes/no): ") == "yes"
collat = input("Do you have collateral? (yes/no): ") == "yes"
collat_val = float(input("Enter the value of your collateral: ")) if collat else 0.0


max_Limit = 0
base_fee = 0.0


# baseline requirements

if age >= 21 and yrs_b >= 2 and has_defaulted is False:

    max_Limit = 3 * rev

    if collat_val < max_Limit:
        print("You are not eligible for a credit card due to insufficient collateral.")

    elif cc >= 720:

        if rev >= 50000:
            base_fee = max_Limit * 1.5
            print(base_fee, "Tier 1", max_Limit)

        else:
            base_fee = max_Limit * 2.5
            print(base_fee, "Tier 1.2", max_Limit)

            if collat_val % 5000 != 0:
                base_fee += 250.00

    elif cc >= 620 and cc < 720:

        if yrs_b >= 5:
            base_fee = max_Limit * 2
            print(base_fee, "Tier 2", max_Limit)

        else:
            base_fee = max_Limit * 3.5
            print(base_fee, "Tier 2.2", max_Limit)

            if collat_val % 5000 != 0:
                base_fee += 250.00

    else:
        print("You are not eligible for a credit card due to low credit score. / Tier 3")

else:
    print("You are not eligible for a credit card due to age, years as a customer, or previous defaults.")
