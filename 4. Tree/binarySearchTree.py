class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder(root):
    if root is not None:
        # Traverse the left subtree
        inorder(root.left)

        # Print the root (or current node)
        print(str(root.key) + "->", end=' ')

        # Traverse the right subtree
        inorder(root.right)

def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)

    # If the tree is not empty, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node

def minValueNode(node):
    current = node

    # Loop down to find the leftmost leaf (which is the smallest element in BST)
    while(current.left is not None):
        current = current.left

    return current

def deleteNode(root, key):
    # If the tree is empty, return root
    if root is None:
        return root

    # Recur down the tree
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        # If key is same as root's key, this is the node to be deleted

        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children: Get the inorder successor (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's content to this node
        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal of the given tree")
inorder(root)

print("\n\nDelete 10")
root = deleteNode(root, 10)
print("Modified tree")
inorder(root)