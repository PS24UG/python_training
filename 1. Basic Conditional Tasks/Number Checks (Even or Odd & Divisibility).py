# Task 2: Even or Odd
number = int(input("Enter the number: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

print("-" * 20)

# Task 3: Divisibility by 3 and 5
number = int(input("Enter the number to check divisibility: "))
if number % 3 == 0 and number % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")
