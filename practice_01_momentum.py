# Practical 01 - Practice Assignment 1
# Momentum calculation using the formula e = m * c^2

# Read input values from the user.
mass = float(input("Enter mass of the object (in kg): "))
velocity = float(input("Enter velocity of the object (in m/s): "))

# The assignment uses the square of velocity in the formula.
momentum = mass * velocity * velocity

print("\nResult")
print("Mass     :", mass, "kg")
print("Velocity :", velocity, "m/s")
print("Momentum :", momentum)
