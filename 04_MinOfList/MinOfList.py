def minimum(listy):
    """
    Input: A list of numbers
    Output: The lowest number in the list, iteration.
    """
    mini = 1000000000000
    for i in listy:
        if i < mini:
            mini = i
    if len(listy) == 0:
        return "None"
    else:
        return mini


def o_minimum(listy):
    """
    Input: A list of numbers.
    Output: The lowest number in the list, using min function.
    """
    if listy != []:
        return (min(listy))


def minimum_r(listy):
    """
    Input: A list of numbers.
    Output: The lowest number in the list, recursion.
    """
    if listy == []:
        return None
    if len(listy) == 1:
        return (listy[0])
    else:
        return (min(listy[0], minimum_r(listy[1:])))