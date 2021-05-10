class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, val):
        self.value = val

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None


from collections import deque


class Queue:
    def __init__(self):
        self.q = deque()

    def enq(self,val):
        self.q.appendleft(val)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)


class Tree:
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root

    # INSERT in the next empty location
    def insert(self, value):
        q = Queue()
        new_node = Node(value)
        node = self.get_root()
        q.enq(node)

        while len(q) > 0:
            node = q.deq()

            if not node.has_left_child():
                node.set_left_child(new_node)
                break
            else:
                q.enq(node.get_left_child())

            if not node.has_right_child():
                node.set_right_child(new_node)
                break

            else:
                q.enq(node.get_right_child())


if __name__ == '__main__':

    tree = Tree("apple")
    tree.insert("banana")
    tree.insert("cherry")
    tree.insert("dates")

    def dfs(tree):
        visited = []
        root = tree.get_root()

        def traverse(node):
            if node:
                visited.append(node.get_value())
                traverse(node.get_left_child())
                traverse(node.get_right_child())

        traverse(root)
        return visited

    print(dfs(tree))
