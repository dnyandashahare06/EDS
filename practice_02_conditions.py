# Practical 01 - Practice Assignment 2
# Check number of digits and perform the required operation

n = int(input("Enter a number: "))

# abs() helps us count digits correctly even for negative numbers.
num = abs(n)

if 0 <= num <= 9:
    print(f"{n} is a single digit number.")
    print(f"Square of {n} = {n ** 2}")
elif 10 <= num <= 99:
    print(f"{n} is a two digit number.")
    print(f"Square root of {num} = {num ** 0.5:.2f}")
elif 100 <= num <= 999:
    print(f"{n} is a three digit number.")
    print(f"Cube root of {num} = {num ** (1 / 3):.2f}")
else:
    print("Number should be single, two or three digit only.")
