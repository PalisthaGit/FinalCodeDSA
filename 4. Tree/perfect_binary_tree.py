class Node:
    # A Node of the binary tree
    def __init__(self, key):
        self.key = key
        self.right = self.left = None


def calculate_depth(node):
    # Function to calculate the depth of the left-most node
    d = 0
    while node is not None:
        d += 1
        node = node.left
    return d


def is_perfect(root, depth, level=0):
    # Function to check if a tree is a perfect binary tree
    
    # If the tree is empty, it is a perfect binary tree
    if root is None:
        return True

    # If leaf node is reached, check its level with depth of left most leaf
    if root.left is None and root.right is None:
        return depth == level + 1

    # If it is not a leaf node, it must have both children
    if root.left is None or root.right is None:
        return False

    # Check recursively for all nodes
    return (is_perfect(root.left, depth, level + 1) and
            is_perfect(root.right, depth, level + 1))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Calculate depth of tree and use it to check if the tree is perfect
if is_perfect(root, calculate_depth(root)):
    print("The tree is a perfect binary tree")
else:
    print("The tree is not a perfect binary tree")
