# Print even numbers from 0 to 10
print("Even numbers from 0 to 10:")
for i in range(0, 11, 2):
    print(i)

# Sum of first 5 numbers (1 to 5)
total_sum = 0
for i in range(1, 6):
    total_sum += i
print("Sum of 1 to 5:", total_sum)

# Multiplication Table
number = int(input("\nEnter the table number: "))
for i in range(1, 11):
    print(f"{i} x {number} = {number * i}")
