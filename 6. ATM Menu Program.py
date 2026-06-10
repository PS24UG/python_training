# ATM Menu System
amount = int(input("Enter your initial account balance: "))
print("\n1. Check balance")
print("2. Withdraw")
print("3. Deposit")
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Your balance: ", amount)
    case 2:
        withdraw_amount = int(input("Enter the withdrawal amount: "))
        if withdraw_amount <= amount:
          remaining_amount = amount - withdraw_amount
          print("Withdrawal successful!")
          print("Your remaining balance: ", remaining_amount)
            
        else:
            print("Insufficient balance")
    case 3:
        deposit = int(input("Enter the deposit amount: "))
        total_amount = amount + deposit
        print("Your total balance: ", total_amount)
    case _:
        print("Invalid choice")
