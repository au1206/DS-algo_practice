class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_left_child(self,node):
        self.left = node

    def set_right_child(self,node):
        self.right = node

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree:
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


# PREORDER DFS
# visit note, traverse lft, traverse right
def preorder(tree):
    visited = []
    root = tree.get_root()

    def traverse(node):
        if node:
            visited.append(node.get_value())
            traverse(node.get_left_child())
            traverse(node.get_right_child())

    traverse(root)
    return visited


pre_order = preorder(tree)
print("PRE-ORDER DFS: ", pre_order)


# In-Order DFS
# traverse left, visit node, traverse right
def inorder(tree):
    visited = []
    root = tree.get_root()

    def traverse(node):
        if node:
            traverse(node.get_left_child())
            visited.append(node.get_value())
            traverse(node.get_right_child())

    traverse(root)
    return visited


in_order = inorder(tree)
print("IN-ORDER DFS: ", in_order)


# Post-Order DFS
# traverse left, traverse right, visit node
def postorder(tree):
    visited = []
    root = tree.get_root()

    def traverse(node):
        if node:
            traverse(node.get_left_child())
            traverse(node.get_right_child())
            visited.append(node.get_value())

    traverse(root)
    return visited


post_order = postorder(tree)
print("POST-ORDER DFS: ", post_order)

