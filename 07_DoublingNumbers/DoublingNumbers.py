def rice(number_blocks):
    """
    Input: The number of blocks on a chess board
    Output: The total number of grains, an iterative function. For each square, the amount of rice doubles. 
    So for the first square, there is one grain of rice. In the second square, there are two grains of rice. ETC. 
    """
    total = 0
    sub_total = 1
    for thing in range(1, number_blocks + 1):
        if thing == 1:
            total += thing
        else:
            sub_total *= 2
            total += sub_total
    return total


def rice_r(number_blocks):
    """
    Input: The number of blocks on a chess board
    Output: The total number of grains, an recursive function. For each square, the amount of rice doubles. 
    So for the first square, there is one grain of rice. In the second square, there are two grains of rice. ETC. 
    """
    if number_blocks == 0:
        return 0
    if number_blocks == 1:
        return 1
    else:
        return (1 + 2 * rice_r(number_blocks -1))