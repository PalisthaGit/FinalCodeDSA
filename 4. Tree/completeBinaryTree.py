class Node:
    def __init__(self, item):
        """Create a new node with the given item."""
        self.item = item
        self.left = None
        self.right = None


def count_nodes(root):
    """Count the number of nodes in a binary tree."""
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def is_complete(root, index, number_nodes):
    """Check if a binary tree is a complete binary tree."""
    # If the tree is empty, it is a complete binary tree.
    if root is None:
        return True
    # If an index is greater or equal than the total number of nodes, 
    # the tree is not a complete binary tree.
    if index >= number_nodes:
        return False
    # Check recursively for all nodes.
    return (is_complete(root.left, 2 * index + 1, number_nodes) and
            is_complete(root.right, 2 * index + 2, number_nodes))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

node_count = count_nodes(root)
index = 0

if is_complete(root, index, node_count):
    print("The tree is a complete binary tree")
else:
    print("The tree is not a complete binary tree")
