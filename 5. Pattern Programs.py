# Right Triangle Pattern
num = int(input("Enter the number of rows: "))
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nInverted Right Triangle (Right-Aligned):")
# Inverted Right Triangle Left Side Pattern (Cleaned up logic)
num = int(input("Enter the number of rows: "))
for i in range(num):
    for j in range(i):
        print(" ", end=" ")
    for k in range(num, i, -1):
        print("*", end=" ")
    print()
