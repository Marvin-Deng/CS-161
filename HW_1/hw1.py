# HW 1, Marvin Deng


def PAD(N):
    """
    Calculates the Nth number in the Padvan Sequence by memoizing the 3 previous values

    Args:
    - N (int): Non-negative position in the Padovan sequence to calculate

    Returns
    - int: The Nth Padovan number
    """

    one_before = 1
    two_before = 1
    three_before = 1

    if N < 3:
        return 1

    for i in range(3, N + 1):
        curr = two_before + three_before
        three_before = two_before
        two_before = one_before
        one_before = curr

    return curr


def SUMS(N):
    """
    Recursively calculates the number of additions required by the PAD function to compute the Nth Padovan number 
    using the number of additions needed to find the 2nd and 3rd previous numbers


    Args:
    - N (int): Non-negative position in the Padovan sequence to calculate

    Returns
    - int: The number of additions
    """

    if N < 3:
        return 0

    return 1 + SUMS(N - 2) + SUMS(N - 3)



    

    

    


