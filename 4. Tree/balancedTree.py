class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinaryTree:
    def __init__(self, root_data=None):
        self.root = None if root_data is None else Node(root_data)

    def is_height_balanced(self, root=None):
        # An empty tree or leaf node is height-balanced
        if root is None:
            return True, 0

        # Check if left child is balanced
        left_balanced, left_height = self.is_height_balanced(root.left)
        if not left_balanced:
            return False, 0

        # Check if right child is balanced
        right_balanced, right_height = self.is_height_balanced(root.right)
        if not right_balanced:
            return False, 0

        # If the difference in heights is more than 1, then tree is not balanced
        if abs(left_height - right_height) > 1:
            return False, 0

        # If this node is balanced, and children are balanced
        return True, max(left_height, right_height) + 1


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

balanced, _ = tree.is_height_balanced()
if balanced:
    print('The tree is balanced')
else:
    print('The tree is not balanced')
