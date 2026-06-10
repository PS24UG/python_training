# Task 1: Loan Eligibility Check
salary = int(input("Enter your salary amount: "))
age = int(input("Enter your age: "))

if salary >= 20000 or age <= 25:
    print("Required for Loan Amount.")
    loan_amount = int(input("Enter the loan amount: "))
    
    if loan_amount <= 50000:
        print("You are eligible for a loan.")
    else:
        print("The maximum loan amount is 50000.")
else:
    print("You are not eligible for a loan.")
