''' Write a Python function that calculates the factorial of a given positive integer using
recursion'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
number = 10
result = factorial(number)

print(f"The factorial of {number} is: {result}")

