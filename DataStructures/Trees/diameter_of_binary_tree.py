"""
Given the root of a binary tree, find the diameter.

Note: Diameter of a Binary Tree is the maximum distance between any two nodes
"""
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def get_left_child(self):
        return self.left

    def set_left_child(self, left):
        self.left = left

    def get_right_child(self):
        return self.right

    def set_right_child(self, right):
        self.right = right

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, value):
        self.q.appendleft(value)

    def dequeue(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)


class Tree:
    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def comparision(self, node, new_node):
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1  # traverse left
        elif new_node.get_value() > node.get_value():
            return 1   # traverse right

    def insert_with_recursion(self, value):
        new_node = Node(value)
        node = self.get_root()
        if node is None:
            self.root = new_node
            return

        self.insert_recursively(node, new_node)

    def insert_recursively(self, node, new_node):
        compare = self.comparision(node, new_node)

        if compare == 0:
            node.set_value(new_node.get_value())

        if compare == -1:
            if node.has_left_child():
                self.insert_recursively(node.get_left_child(), new_node)

            else:
                node.set_left_child(new_node)

        else:
            if node.has_right_child():
                self.insert_recursively(node.get_right_child(), new_node)

            else:
                node.set_right_child(new_node)




def diameter(tree):
    visited = []
    q = Queue()
    node = tree.get_root()
    level = 0
    q.enqueue((node, level))

    while len(q) > 0:
        node, level = q.dequeue()

        if node is None:
            visited.append(("None", level))
            continue
        visited.append((node, level))

        if node.has_left_child():
            q.enqueue((node.get_left_child(), level+1))
        else:
            q.enqueue((None, level+1))

        if node.has_right_child():
            q.enqueue((node.get_right_child(), level+1))

        else:
            q.enqueue((None, level+1))

    print(visited)
    dia = [0]*len(visited)
    for val, level in visited:
        dia[level] += 1

    print(dia)
    print(f"the diameter is: {max(dia)} at level {dia.index(max(dia))}")


tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

diameter(tree)