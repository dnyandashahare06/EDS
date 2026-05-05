# Practical 02 - Practice Assignment 1
# List operations and dictionary operations

print("List Operations")

# Start with a simple list of numbers.
numbers = [10, 20, 30, 40, 50]
print("Original list       :", numbers)

numbers.append(60)
print("After append        :", numbers)

numbers.insert(2, 25)
print("After insert        :", numbers)

numbers.remove(40)
print("After remove        :", numbers)

deleted_item = numbers.pop()
print("After pop           :", numbers)
print("Deleted item        :", deleted_item)

numbers.sort()
print("After sort          :", numbers)

numbers.reverse()
print("After reverse       :", numbers)

print("Index of 30         :", numbers.index(30))
print("Count of 20         :", numbers.count(20))
print("List slice [1:4]    :", numbers[1:4])
print("Length of list      :", len(numbers))

extra_numbers = [70, 80]
numbers.extend(extra_numbers)
print("After extend        :", numbers)

copied_list = numbers.copy()
print("Copied list         :", copied_list)

print("\nDictionary Operations")

# Dictionary stores data in key-value pairs.
student = {
    "name": "Kunal",
    "roll_no": 21,
    "branch": "Computer Engineering",
    "marks": 85,
}

print("Original dictionary :", student)
print("Student name        :", student["name"])
print("Marks using get     :", student.get("marks"))

student["city"] = "Pune"
print("After adding city   :", student)

student["marks"] = 90
print("After updating marks:", student)

removed_city = student.pop("city")
print("After pop city      :", student)
print("Removed city        :", removed_city)

print("Keys                :", list(student.keys()))
print("Values              :", list(student.values()))
print("Items               :", list(student.items()))
print("Is name present?    :", "name" in student)

print("\nDictionary using loop")
for key, value in student.items():
    print(key, ":", value)

# update() can add more than one key-value pair at the same time.
student.update({"year": "Second Year", "college": "MITAOE"})
print("\nAfter update        :", student)

student_copy = student.copy()
print("Copied dictionary   :", student_copy)
print("Length              :", len(student))
