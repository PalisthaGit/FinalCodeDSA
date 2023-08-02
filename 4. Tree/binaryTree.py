class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Traverse preorder
    def traversePreOrder(self):
        result = str(self.val) + ' '
        if self.left:
            result += self.left.traversePreOrder()
        if self.right:
            result += self.right.traversePreOrder()
        return result

    # Traverse inorder
    def traverseInOrder(self):
        result = ''
        if self.left:
            result += self.left.traverseInOrder()
        result += str(self.val) + ' '
        if self.right:
            result += self.right.traverseInOrder()
        return result

    # Traverse postorder
    def traversePostOrder(self):
        result = ''
        if self.left:
            result += self.left.traversePostOrder()
        if self.right:
            result += self.right.traversePostOrder()
        result += str(self.val) + ' '
        return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("Pre order Traversal: ", end="")
print(root.traversePreOrder())
print("In order Traversal: ", end="")
print(root.traverseInOrder())
print("Post order Traversal: ", end="")
print(root.traversePostOrder())
