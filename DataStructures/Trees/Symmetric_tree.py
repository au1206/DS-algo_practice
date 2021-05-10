"""
Given a binary tree, check whether it is a mirror of itself.
"""


class Node:

    # Utility function to create new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# root1.key == root2.key
# left_subtree.left == right subtree.right
# left_subtree.right == right_subtree.left

def is_mirror(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None:
        if root1.key == root2.key:
            return is_mirror(root1.left, root2.right) and is_mirror(root1.right, root2.left)

    return False


def is_symmetric(root):
    return is_mirror(root, root)


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

print(is_symmetric(root))


