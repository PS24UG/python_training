# Task 4: Math Operations
a = int(input("Enter the First number: "))
b = int(input("Enter the Second number: "))
c = int(input("Enter the Third number: "))

multiple = a * b * c
add = a + b + c
divide = multiple / add
print("Result of (Multiplication / Addition):", divide)

print("-" * 20)

# Task 5: User Details Formatting
name = input("Enter your name: ")
score = float(input("Enter your score (out of 100): "))
department = input("Enter your department: ")

print(f"\nMy name is {name}")
print(f"My score is {score / 10}/10")
print(f"My department is {department}")
