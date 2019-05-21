def fibbs(n):
    """
    Input: the nth number.
    Output: the number of the Fibonacci sequence via iteration.
    """
    sequence = []
    for i in range(n+1):
        if i == 0:
            sequence.append(0)
        elif i == 1:
            sequence.append(1)
        else:
            total = sequence[i - 2] + sequence[i - 1]
            sequence.append(total)
    return (sequence[-1])

def fibbs_r(n, a = 0, b = 1):
    """
    Input: the nth number.
    Output: the number of the Fiboacci sequence via recursion.
    """
    if n == a:
        return a
    if n == b:
        return b
    else:
        return (fibbs_r(n-1) + fibbs_r(n - 2))