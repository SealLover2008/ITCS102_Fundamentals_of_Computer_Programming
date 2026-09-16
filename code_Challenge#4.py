#Create account screen
print("=====CREATE AN ACCOUNT======")
user = input("Please enter Username--->  ")
user_password = input("Please enter Username Password--->  ")

#login screen Page
print("\n\n======LOGIN======")
user_login = input("Please enter Username--->  ")
user_login_password = input("Please enter Username Password--->  ")

if user == user_login and user_password == user_login_password:
    print("access Granted")

    age = int(input("\nHow Old are you? Max Age is 65 Years Old---->   "))
    is_employed = input("Are you employed? True or False---->   ") == "True"
    credit_score = eval(input("What is your credit score?---->   "))
    annual_outcome = eval(input("What is your annual income?---->   "))
    has_collateral = input("Do you have Collateral? True or False---->   ") == "True"
    loan_amount = float(input("How much would you like to loan? "))

    # Collateral if True
    if has_collateral == True:

        collateral_value = eval(input("What is the value of your collateral? Anything Under 30k is prohibitted---->   "))

        if collateral_value < 30000:
            print("Invalid Collateral Value. Please enter a value greater than 30k")

        else:
            print("Collateral Value Accepted")

            # Tier 1 of True
            if age >= 21 and age < 64 and is_employed == True and credit_score >= 750:

                baseline_interest_rate = 5

                if annual_outcome >= 100000:
                    baseline_interest_rate = 4.5

                interest = loan_amount * (baseline_interest_rate / 100)

                print("Approved at", baseline_interest_rate, "interest")
                print("Calculated Interest:", interest)

            # Tier 2 of True
            elif age >= 21 and age < 64 and credit_score >= 600 and credit_score < 750:

                base_interest_rate = 7

                interest = loan_amount * (base_interest_rate / 100)

                print("Approved at", base_interest_rate, "%", " interest")
                print("Calculated Interest:", interest)

            # Tier 3 of true
            elif age >= 65 or credit_score < 600:

                if credit_score < 600:
                    print("Rejected: Credit score too low")
                else:
                    print("You are not eligible for a loan at this age.")

            # Fails baseline
            else:
                print("Rejected: Fails baseline criteria")

            #Collateral if False
    else:

        # Tier 1 of False
        if age >= 21 and age < 64 and is_employed == True and credit_score >= 750:

            baseline_interest_rate = 5

            if annual_outcome >= 100000:
                baseline_interest_rate = 4.5

            interest = loan_amount * (baseline_interest_rate / 100)

            print("Approved at", baseline_interest_rate, "interest")
            print("Calculated Interest:", interest)

        # Tier 2 Of fails
        elif age >= 21 and age < 64 and credit_score >= 600 and credit_score < 750:

            base_interest_rate = 8

            if annual_outcome < 40000:
                base_interest_rate = 9.5

            interest = loan_amount * (base_interest_rate / 100)

            print("Approved at", base_interest_rate, "interest")
            print("Calculated Interest:", interest)

        # Tier 3 of fasle
        elif age >= 65 or credit_score < 600:

            if credit_score < 600:
                print("Rejected: Credit score too low")
            else:
                print("You are not eligible for a loan at this age.")

        # Fails baseline
        else:
            print("Rejected: Fails baseline criteria")

else:
    print("access denied")


#Worth every secondddddddddddddd, nice.
