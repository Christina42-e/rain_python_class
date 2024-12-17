principal_amount = float(input("Enter your principal amount:"))
annual_interest_rate = float(input("Enter your annual interest rate:"))
time_in_years = float(input("Enter your time in years:"))

compound_interest_rate = float((principal_amount * (1 + (annual_interest_rate/100))**(time_in_years) - principal_amount))
print("your compound interest rate is :",compound_interest_rate)
