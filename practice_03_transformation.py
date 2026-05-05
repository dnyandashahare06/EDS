# Practical 01 - Practice Assignment 3
# Transform birth date into age and salary in rupees into dollars

from datetime import date

DOLLAR_RATE = 83.5


def calculate_age(day, month, year):
    """Calculate age from day, month and year of birth."""
    today = date.today()
    age = today.year - year

    # If birthday has not come yet this year, reduce age by 1.
    if (today.month, today.day) < (month, day):
        age = age - 1

    return age


def rupees_to_dollars(salary):
    """Convert rupees to dollars using the fixed assignment rate."""
    return salary / DOLLAR_RATE


name = input("Enter employee name: ")
birth_date = input("Enter birth date (DD/MM/YYYY): ")
salary_rupees = float(input("Enter salary in rupees: "))

# Split DD/MM/YYYY into three integer values.
day, month, year = map(int, birth_date.split("/"))

age = calculate_age(day, month, year)
salary_dollars = rupees_to_dollars(salary_rupees)

print("\nEmployee data after transformation")
print(f"Name        : {name}")
print(f"Age         : {age} years")
print(f"Salary INR  : {salary_rupees:.2f}")
print(f"Salary USD  : {salary_dollars:.2f}")
