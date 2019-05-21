def summ(listy):
    """
    Input: A list of numbers.
    Output: The sum of all the numbers in the list, iterative.
    """
    total = 0
    for i in listy:
        total += i
    return total


def o_summ(listy):
    """
    Input: A list of numbers.
    Output: The sum of all the numbers in the list, using sum function.
    """
    return (sum(listy))


def summ_r(listy):
    """
    Input: A list of numbers.
    Output: The sum of all the numbers in the list, recursive.
    """
    if listy == []:
        return 0
    else:
        return (listy[0] + summ_r(listy[1:]))