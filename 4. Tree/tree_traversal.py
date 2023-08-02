class Node:
    """A node in a binary tree."""
    
    def __init__(self, item):
        """Initializes a new node with the given item."""
        self.left = None
        self.right = None
        self.val = item

def inorder_traversal(root):
    """Performs an inorder traversal of the tree rooted at root.
    Returns the traversal as a string."""
    if root is None:
        return ""
    else:
        return (inorder_traversal(root.left) + 
                str(root.val) + "->" + 
                inorder_traversal(root.right))

def postorder_traversal(root):
    """Performs a postorder traversal of the tree rooted at root.
    Returns the traversal as a string."""
    if root is None:
        return ""
    else:
        return (postorder_traversal(root.left) + 
                postorder_traversal(root.right) + 
                str(root.val) + "->")

def preorder_traversal(root):
    """Performs a preorder traversal of the tree rooted at root.
    Returns the traversal as a string."""
    if root is None:
        return ""
    else:
        return (str(root.val) + "->" + 
                preorder_traversal(root.left) + 
                preorder_traversal(root.right))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal")
print(inorder_traversal(root))

print("\nPreorder traversal")
print(preorder_traversal(root))

print("\nPostorder traversal")
print(postorder_traversal(root))
