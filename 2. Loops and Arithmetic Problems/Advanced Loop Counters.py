# Sum of even numbers between 0 and 10
even_count = 0
for i in range(0, 11, 2):
    even_count += i
print("Sum of even numbers (0-10):", even_count)

# Sum of odd numbers between 1 and 10
odd_count = 0
for i in range(1, 11, 2):
    odd_count += i
print("Sum of odd numbers (1-10):", odd_count)

# Count numbers divisible by both 3 and 5 between 1 and 100
divisible_count = 0
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        divisible_count += 1
print("Count of numbers divisible by 3 and 5 (1-100):", divisible_count)
