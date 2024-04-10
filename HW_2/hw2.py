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