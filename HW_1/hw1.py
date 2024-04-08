"""
HW 1, Marvin Deng

My solutions use memoization or recursion to determine the answer to next steps based on the results of previous or next steps.

1. Calculates the Nth number in the Padvan Sequence by memoizing the 3 previous values in order to calculate the next sum

2. Recursively calculates the number of additions required by the PAD function to compute the Nth Padovan number 
    using the number of additions needed to find the 2nd and 3rd previous numbers.

3. Recursively changes the values of the tuples to "?" only when the value of the input isn't a tuple (implying its the value of a leaf)

4. Calculates the height of TREE, or the longest path from the root node to the farthest leaf node.

5. Returns a postorder traversal of the numbers in TREE by recursively searching the left and right subtrees before processing the current node.
"""


def PAD(N):
    """
    1.

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
    2.

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
    3.

    Args:
    - TREE (tuple): A tuple representing a tree

    Returns:
    - tuple: The tuple equal to TREE with its values anonymized to "?"
    """

    if not isinstance(TREE, tuple):
        return "?"

    return tuple(ANON(subtree) for subtree in TREE)
    

def TREE_HEIGHT(TREE):
    """
    4.

    Args:
    - TREE (tuple): A tuple representing a tree

    Returns:
    - int: Longest path from the root to a leaf of TREE
    """

    if not isinstance(TREE, tuple) or not TREE:
        return 0

    return 1 + max(TREE_HEIGHT(subtree) for subtree in TREE)


def TREE_ORDER(TREE):
    """
    5.

    Args:
    - TREE (tuple): A tuple representing an ordered tree in the form (L, m, R) where 
        - L and R are ordered trees
        - m is a number
        - all numbers appearing in L are smaller than m
        - all numbers appearing in R are larger than m

    Returns:
    - tuple: A tuple of the postorder traversal of the numbers in TREE
    """

    if TREE is None:
        return ()

    if not isinstance(TREE, tuple):
        return (TREE,)

    left_subtree = TREE_ORDER(TREE[0]) if TREE[0] is not None else ()
    right_subtree = TREE_ORDER(TREE[2]) if TREE[2] is not None else ()
    root = (TREE[1],)

    return left_subtree + right_subtree + root

