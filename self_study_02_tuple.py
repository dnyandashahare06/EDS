# Practical 02 - Self Study Assignment 2
# Tuple operations

# Tuple is ordered and cannot be changed directly.
numbers = (10, 20, 30, 40, 50, 20, 30)

print("Tuple              :", numbers)
print("First element      :", numbers[0])
print("Last element       :", numbers[-1])
print("Element at index 3 :", numbers[3])

print("\nSlicing")
print("numbers[1:4]       :", numbers[1:4])
print("numbers[:3]        :", numbers[:3])
print("numbers[3:]        :", numbers[3:])
print("Reverse tuple      :", numbers[::-1])

print("\nBasic operations")
print("Length             :", len(numbers))
print("Count of 20        :", numbers.count(20))
print("Index of 30        :", numbers.index(30))
print("Minimum            :", min(numbers))
print("Maximum            :", max(numbers))
print("Sum                :", sum(numbers))

print("\nMembership")
print("40 in tuple        :", 40 in numbers)
print("99 in tuple        :", 99 in numbers)

more_numbers = (60, 70)
joined_tuple = numbers + more_numbers
repeated_tuple = (1, 2) * 3

print("\nConcatenation      :", joined_tuple)
print("Repetition         :", repeated_tuple)

print("\nTuple using loop")
for item in numbers:
    print(item, end=" ")
print()

# Convert tuple to list when a new item needs to be added.
temp_list = list(numbers)
temp_list.append(100)
new_tuple = tuple(temp_list)
print("\nAfter converting to list and adding 100:", new_tuple)

student = ("Kunal", 21, "Computer Engineering")

# Tuple unpacking stores each tuple value in a separate variable.
name, roll_no, branch = student

print("\nTuple unpacking")
print("Name               :", name)
print("Roll No            :", roll_no)
print("Branch             :", branch)
