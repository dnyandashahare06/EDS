# Practical 02 - Lab Assignment 1
# Find the position of a number in a list using linear search


def linear_search(numbers, key):
    """Return the index of key if found, otherwise return -1."""
    for index in range(len(numbers)):
        if numbers[index] == key:
            return index

    return -1


values = input("Enter numbers separated by space: ")

# Convert the input string into a list of integers.
numbers = list(map(int, values.split()))

key = int(input("Enter number to search: "))
position = linear_search(numbers, key)

if position == -1:
    print(key, "is not present in the list.")
else:
    print(key, "is present at index", position)
    print("Position number is", position + 1)
