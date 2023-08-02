class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def is_height_balanced(root):
    # An empty tree is height-balanced
    if root is None:
        return True, 0

    # Check if left child is balanced
    left_balanced, left_height = is_height_balanced(root.left)
    if not left_balanced:
        return False, 0

    # Check if right child is balanced
    right_balanced, right_height = is_height_balanced(root.right)
    if not right_balanced:
        return False, 0

    # If the difference in heights is more than 1, then tree is not balanced
    if abs(left_height - right_height) > 1:
        return False, 0

    # If this node is balanced, and children are balanced
    return True, max(left_height, right_height) + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

balanced, _ = is_height_balanced(root)
if balanced:
    print('The tree is balanced')
else:
    print('The tree is not balanced')
