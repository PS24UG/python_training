# Driving speed limit check
speed = int(input("Enter the speed value: "))
if speed >= 70:
    print("Over speeding! Penalty ticket issued.")
else:
    print("Safe driving.")

# Sum of natural numbers up to N
n = int(input("\nEnter the value of n: "))
total = 0
for i in range(1, n + 1):
    print(i, end=" ")
    total += i
print(f"\nTotal Sum: {total}")

# Cube of numbers up to N
n = int(input("\nEnter the value of n for cubing: "))
for i in range(1, n + 1):
    print(f"Number is {i} and cube of {i} is {i**3}")

# Factorial of a number
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"\nInput: {num}\nOutput (Factorial): {factorial}")

# Prime number check
num = int(input("\Enter a number to check if it's Prime: "))
result = "Prime"
if num <= 1:
    result = "Not Prime"
else:
    for i in range(2, num):
        if num % i == 0:
            result = "Not Prime"
            break
print(f"{num} is {result}")
