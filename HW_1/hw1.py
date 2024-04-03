# HW 1, Marvin Deng


def PAD(N):
    """
    1. Calculates the Nth number in the Padvan Sequence by memoizing the 3 previous values

    Args:
    - N (int): Non-negative position in the Padovan sequence to calculate

    Returns:
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
    2. Recursively calculates the number of additions required by the PAD function to compute the Nth Padovan number 
    using the number of additions needed to find the 2nd and 3rd previous numbers

    Args:
    - N (int): Non-negative position in the Padovan sequence to calculate

    Returns:
    - int: The number of additions needed to find the Nth Padovan number
    """

    if N < 3:
        return 0

    return 1 + SUMS(N - 2) + SUMS(N - 3)


def ANON(TREE):
    """
    3. Recursively changes the values of the tuples to "?"

    Args:
    - TREE (tuple): A tuple representing the tree

    Returns:
    - tuple: The tuple representin TREE with its values anonymized to "?"

    """
    if not isinstance(TREE, tuple):
        return "?"

    return tuple(ANON(subtree) for subtree in TREE)
    
