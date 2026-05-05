# Practical 01 - Lab Assignment 1
# Accept marks of five courses and calculate result

PASS_MARK = 40
TOTAL_SUBJECTS = 5

marks = []

print("Enter marks for five courses out of 100")

# Step 1: Read marks for all subjects.
for course_number in range(1, TOTAL_SUBJECTS + 1):
    mark = float(input(f"Course {course_number} marks: "))
    marks.append(mark)

# Step 2: Calculate total and percentage.
total = sum(marks)
percentage = total / TOTAL_SUBJECTS

# A student passes only when every subject has at least PASS_MARK marks.
is_pass = all(mark >= PASS_MARK for mark in marks)

print("\nResult")
print("Marks      :", marks)
print("Total      :", total)
print(f"Percentage : {percentage:.2f}%")

if not is_pass:
    print("Status     : Fail")
else:
    print("Status     : Pass")

    if percentage > 75:
        grade = "Distinction"
    elif percentage >= 60:
        grade = "First Division"
    elif percentage >= 50:
        grade = "Second Division"
    else:
        grade = "Third Division"

    print("Grade      :", grade)
