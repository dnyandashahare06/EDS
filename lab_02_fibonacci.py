# Practical 01 - Lab Assignment 2
# Fibonacci sequence using recursive function


def fibonacci(n):
    """Return the nth Fibonacci number."""
    # First two Fibonacci numbers are fixed.
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Every next number is the sum of the previous two numbers.
    return fibonacci(n - 1) + fibonacci(n - 2)


terms = int(input("How many Fibonacci numbers to display? "))

print("\nFibonacci sequence:")

for term_number in range(terms):
    print(fibonacci(term_number), end=" ")

print()
