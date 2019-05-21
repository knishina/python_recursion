def factorial(n):
    """
    Input: a number.
    Output: find the factorial of the input number via iteration.
    """
    product = 1
    if n == 0:
        return 0
    for thing in range(1, n+1):
        product *= thing
    return product


import math
def o_factorial(n):
    """
    Input: a number.
    Output: find the factorial of the input number using the math function.
    """
    if n != 0:
        number = math.factorial(n)
        return number
    else: 
        return 0


def factorial_r(n):
    """
    Input: a number.
    Output: find the factorial of the input number using recursion.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return (n * factorial_r(n-1))