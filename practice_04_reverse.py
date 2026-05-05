# Practical 01 - Practice Assignment 4
# Print the reverse of a given number

n = int(input("Enter a number: "))

original = n
is_negative = n < 0
n = abs(n)
reverse = 0

# Pick the last digit one by one and build the reversed number.
while n != 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if is_negative:
    reverse = -reverse

print("\nOriginal number :", original)
print("Reversed number :", reverse)
