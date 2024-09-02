#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): The non-negative integer for which the factorial is to be computed.

    Returns:
    int: The factorial of the input number 'n'. If 'n' is 0, the function returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the integer from the command-line argument, compute its factorial, and print the result
f = factorial(int(sys.argv[1]))
print(f)

