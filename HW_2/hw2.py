"""
HW 2, Marvin Deng

1. BFS traversal of the tuple tree can be done using a list representing a queue. 
   The queue contains the next subtree in the level to process. We process the queue one level at a time.
   When we reach a leaf node (not a tuple), we can add it to our result.
   When we reach another tuple, we add its children into the queue.

2. DFS traversal of the tuple tree can be done using a list representing a stack. 
   The stack contains the next subtree in the level to process. We pop from the end of the list.
   When we reach a leaf node (not a tuple), we can add it to our result.
   When we reach another tuple, we append its children to the back of the list.

3. DFID traversal of the tuple tree can be done using multiple iterations of a recursive DFS, which 
   only traverses to a certain depth each iteration
"""

def BFS(TREE):
    """
    1.

    Args:
    - TREE (tuple): A tuple representing a tree

    Returns:
    - tuple: The tuple representing the left to right BFS traversal of TREE
    """
    if not isinstance(TREE, tuple):
        return (TREE,)

    bfs_order = []
    queue = [TREE]
    
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            curr = queue.pop(0)
            if not isinstance(curr, tuple):
                bfs_order.append(curr)
            else:
                queue.extend(curr)

    return tuple(bfs_order)


def DFS(TREE):
    """
    2.

    Args:
        - TREE (tuple): A tuple representing a tree

    Returns:
        - tuple: The tuple representing a left to right DFS traversal of TREE
    """
    if not isinstance(TREE, tuple):
        return (TREE,)

    dfs_order = []
    stack = [TREE]

    while stack:
        curr = stack.pop()
        if isinstance(curr, tuple):
            stack.extend(curr[::-1])
        else:
            dfs_order.append(curr)

    return tuple(dfs_order)

def DFID(TREE, D):
    """
    2.

    Args:
        - TREE (tuple): A tuple representing a tree
        - D (int): The depth of the tree

    Returns:
        - tuple: The tuple representing a right to left DFID traversal of TREE
    """

    if not isinstance(TREE, tuple):
        return (TREE,)
     
    def dfs(node, depth, result):

        if depth < 0:
            return
        
        if not isinstance(node, tuple):
            result.append(node)
            return
        
        for child in node[::-1]:
            dfs(child, depth - 1, result)

    result = []
    for depth in range(D + 1):
        dfs(TREE, depth, result)

    return tuple(result)

"""
4.

These functions implement a depth-first solver for the homer-baby-dog-poison
problem. In this implementation, a state is represented by a single tuple
(homer, baby, dog, poison), where each variable is True if the respective entity is
on the west side of the river, and False if it is on the east side.
Thus, the initial state for this problem is (False False False False) (everybody
is on the east side) and the goal state is (True True True True).

The main entry point for this solver is the function DFS_SOL, which is called
with (a) the state to search from and (b) the path to this state. It returns
the complete path from the initial state to the goal state: this path is a
list of intermediate problem states. The first element of the path is the
initial state and the last element is the goal state. Each intermediate state
is the state that results from applying the appropriate operator to the
preceding state. If there is no solution, DFS_SOL returns [].
To call DFS_SOL to solve the original problem, one would call
DFS_SOL((False, False, False, False), [])
However, it should be possible to call DFS_SOL with any intermediate state (S)
and the path from the initial state to S (PATH).
"""

"""
FINAL_STATE

Args:
- S, the current state, and returns True if it

Returns:
- If the goal state (True, True, True, True) and False otherwise.
"""

def FINAL_STATE(S):
    return S == (True, True, True, True)

"""
NEXT_STATE 
- Returns the state that results from applying an operator to the current state. 

Args:
- the current state (S)
- which entity to move (A, equal to "h" for homer only, "b" for homer with baby, "d" for homer
with dog, and "p" for homer with poison).

Returns:
- A list containing the state that results from that move.
- If applying this operator results in an invalid state (because the dog and baby,
or poisoin and baby are left unsupervised on one side of the river)
OR
- when the action is impossible (homer is not on the same side as the entity) it returns [].

NOTE that NEXT_STATE returns a list containing the successor state (which is
itself a tuple)# the return should look something like [(False, False, True, True)].
(homer, baby, dog, poison)
"""

def NEXT_STATE(S, A):
    homer, baby, dog, poison = S

    # Check for invalid current state: Baby unsupervised with dog or poison
    if homer != baby and (baby == dog or baby == poison):
        return []

    new_state = None

    if A == "h":
        new_state = [(not homer, baby, dog, poison)]
    elif A == "b":
        if homer == baby:
            new_state = [(not homer, not baby, dog, poison)]
        else:
            return []
    elif A == "d":
        if homer == dog:
            new_state = [(not homer, baby, not dog, poison)]
        else:
            return []
    elif A == "p":
        if homer == poison:
            new_state = [(not homer, baby, dog, not poison)]
        else:
            return []

    if new_state is None:
        return []

    new_h, new_b, new_d, new_p = new_state[0]

    # Check for invalid new state: Baby unsupervised with dog or poison
    if new_h != new_b and (new_b == new_d or new_b == new_p):
        return []

    return new_state

# SUCC_FN returns all of the possible legal successor states to the current
# state. It takes a single argument (S), which encodes the current state, and
# returns a list of each state that can be reached by applying legal operators
# to the current state.
def SUCC_FN(S):
    succ_states = []
    moves = ["h", "b", "d", "p"]
    for move in moves:
        next_state = NEXT_STATE(S, move)
        if next_state != []:
            succ_states.append(next_state[0])
    return succ_states

"""
ON_PATH checks whether the current state is on the stack of states visited by
this depth-first search. 

Args:
- the current state (S) 
- stack of states visited by DFS (STATES). 

Returns
- True if S is a member of STATES and False otherwise.
"""

def ON_PATH(S, STATES):
    return S in STATES

"""
MULT_DFS is a helper function for DFS_SOL. 

Args
- STATES is a list of states from the initial state to the current state (PATH), and the legal
successor states to the last, current state in the PATH (STATES). 
- PATH is a first-in first-out list of states# that is, the first element is the initial
state for the current search and the last element is the most recent state
explored. 

MULT_DFS does a depth-first search on each element of STATES in
turn. If any of those searches reaches the final state, MULT_DFS returns the
complete path from the initial state to the goal state. Otherwise, it returns
[].
"""

def MULT_DFS(STATES, PATH):
    for state in STATES:
        stack = [(state, PATH + [state])]

        while stack:
            current_state, current_path = stack.pop()

            if FINAL_STATE(current_state):
                return current_path

            for successor in SUCC_FN(current_state):
                if not ON_PATH(successor, current_path):
                    stack.append((successor, current_path + [successor]))

    return []


# DFS_SOL does a depth first search from a given state to the goal state. It
# takes two arguments: a state (S) and the path from the initial state to S
# (PATH). If S is the initial state in our search, PATH is set to []. DFS_SOL
# performs a depth-first search starting at the given state. It returns the path
# from the initial state to the goal state, if any, or [] otherwise. DFS_SOL is
# responsible for checking if S is already the goal state, as well as for
# ensuring that the depth-first search does not revisit a node already on the
# search path (i.e., S is not on PATH).
def DFS_SOL(S, PATH):
    pass