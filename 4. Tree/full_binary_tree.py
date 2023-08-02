class Node:
    """A node in a binary tree."""

    def __init__(self, item):
        """Initialize a new node with the given item."""
        self.item = item
        self.left = None
        self.right = None


def is_full_tree(root):
    """
    Checks if a binary tree is a full binary tree.
    A full binary tree is a tree in which every node has either 0 or 2 children.
    """
    # Tree empty case
    if root is None:
        return True

    # Check if the node has either no child or two children
    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return (is_full_tree(root.left) and is_full_tree(root.right))

    return False


root = Node(1)
root.right = Node(3)
root.left = Node(2)

root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

if is_full_tree(root):
    print("The tree is a full binary tree")
else:
    print("The tree is not a full binary tree")