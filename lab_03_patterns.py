# Practical 01 - Lab Assignment 3
# Print different patterns

rows = int(input("Enter the number of rows: "))

print("\nPattern 1: Right triangle")
for row in range(1, rows + 1):
    print("* " * row)

print("\nPattern 2: Inverted triangle")
for row in range(rows, 0, -1):
    print("* " * row)

print("\nPattern 3: Pyramid")
for row in range(1, rows + 1):
    spaces = " " * (rows - row)
    stars = "* " * row
    print(spaces + stars)

print("\nPattern 4: Number triangle")
for row in range(1, rows + 1):
    for number in range(1, row + 1):
        print(number, end=" ")
    print()

print("\nPattern 5: Floyd's triangle")
number = 1
for row in range(1, rows + 1):
    for _ in range(row):
        print(number, end=" ")
        number += 1
    print()

print("\nPattern 6: Diamond")
for row in range(1, rows + 1):
    print(" " * (rows - row) + "* " * row)
for row in range(rows - 1, 0, -1):
    print(" " * (rows - row) + "* " * row)
