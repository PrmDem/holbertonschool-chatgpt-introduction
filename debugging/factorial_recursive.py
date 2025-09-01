#!/usr/bin/python3
import sys

# Function Description:
	# This function calculates the factorial of a given number n using recursion.
	# Factorial of a number is the product of all positive integers less than or equal to n.
	
# Parameters:
	# n (int): The number for which the factorial is to be computed. n should be a non-negative integer.
	
# Returns:
	# int: The factorial of the input number n. If n is 0, returns 1, as 0! = 1 by definition.

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)