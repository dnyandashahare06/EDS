# Practical 01 - Self Study Assignment
# Statistical analysis on employee data


def show_statistics(values, heading):
    """Print common statistics for one list of numbers."""
    total = sum(values)
    average = total / len(values)

    print(f"\n{heading}")
    print("Values  :", values)
    print("Sum     :", total)
    print(f"Average : {average:.2f}")
    print("Maximum :", max(values))
    print("Minimum :", min(values))


employees = [
    {"name": "Amit", "age": 30, "salary": 55000, "experience": 5},
    {"name": "Sneha", "age": 25, "salary": 42000, "experience": 2},
    {"name": "Rohan", "age": 35, "salary": 72000, "experience": 10},
    {"name": "Priya", "age": 28, "salary": 48000, "experience": 3},
    {"name": "Neha", "age": 40, "salary": 90000, "experience": 15},
]

print("Employee Data")
print(f"{'Name':<10} {'Age':>5} {'Salary':>10} {'Experience':>12}")
print("-" * 42)

# Display each employee in table format.
for employee in employees:
    print(
        f"{employee['name']:<10} "
        f"{employee['age']:>5} "
        f"{employee['salary']:>10} "
        f"{employee['experience']:>12}"
    )

# Create separate lists so statistics can be calculated easily.
ages = [employee["age"] for employee in employees]
salaries = [employee["salary"] for employee in employees]
experience = [employee["experience"] for employee in employees]

show_statistics(ages, "Age Statistics")
show_statistics(salaries, "Salary Statistics")
show_statistics(experience, "Experience Statistics")
