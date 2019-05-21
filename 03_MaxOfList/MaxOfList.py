def maximum(listy):
    """
    Input: A list of numbers
    Output: The highest number in the list, iteration.
    """
    maxi = 0
    for i in listy:
        if i > maxi:
            maxi = i
    if len(listy) == 0:
        return None
    else:
        return maxi


def o_maximum(listy):
    """
    Input: A list of numbers.
    Output: The highest number in the list, using max function.
    """
    if listy != []:
        return (max(listy))


def maximum_r(listy):
    """
    Input: A list of numbers.
    Output: The highest number in the list, recursion.
    """
    if listy == []:
        return None
    if len(listy) == 1:
        return (listy[0])
    else:
        return (max(listy[0], maximum_r(listy[1:])))