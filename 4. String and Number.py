# Count the number of digits
num = int(input("Enter the number: "))
digit_count = len(str(abs(num)))  # abs handles negative numbers safely
print(f"{num} has {digit_count} digits.")

# Reverse a number
num = input("Enter the number to reverse: ")
reverse_num = num[::-1]
print("Reversed Number:", reverse_num)

# Count Vowels and Consonants (Fixed spaces/special chars bug)
text = input("\Enter String: ")
vowels = 0
consonants = 0
for ch in text.lower():
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():  # Counts only alphabets as consonants, ignoring spaces
        consonants += 1
print("Vowels =", vowels)
print("Consonants =", consonants)

# Palindrome Check
text = input("\Enter String to check Palindrome: ")
if text.lower() == text.lower()[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
