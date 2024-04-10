"""
HW 2, Marvin Deng


"""

def BFS(TREE):
    """
    1.

    Args:
    - TREE (tuple): A tuple representing a tree

    Returns:
    - tuple: The tuple representing the BFS traversal of TREE
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
