def counter(listy):
    """
    Input: A list of numbers.
    Output: The number of entries in the list, interation.
    """
    counter = 0
    for i in listy:
        counter += 1
    return counter


def o_counter(listy):
    """
    Input: A list of numbers.
    Ouptut: The number of entries in a list, using the len function.
    """
    return (len(listy))


def counter_r(listy):
    """
    Input: A list of numbers.
    Output: The number of entires in a list, recursion.
    """
    if listy == []:
        return 0
    else:
        return (1 + counter(listy[1:]))