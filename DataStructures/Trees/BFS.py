"""
visiting tree one level at a time
useful in finding the shortest path in graphs
"""


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


class Tree:
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


from collections import deque


class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, value):
        self.q.appendleft(value)

    def dequeue(self):
        if len(self.q)>0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


def bfs(tree):
    visited = []
    q = Queue()
    node = tree.get_root()
    q.enqueue(node)

    while len(q) > 0:
        node = q.dequeue()
        visited.append(node.get_value())
        if node.has_left_child():
            q.enqueue(node.get_left_child())

        if node.has_right_child():
            q.enqueue(node.get_right_child())

    print(q)
    return visited


bfs_tree = bfs(tree)
print(bfs_tree)
