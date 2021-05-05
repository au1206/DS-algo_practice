class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


from collections import deque

# for printing tree
class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
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


class Tree():
    def __init__(self):
        self.root = None

    def set_root(self, value):
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


    def insert(self, value):
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

    def search(self, value):
        search_node = Node(value)
        node = self.get_root()

        while True:
            compare = self.comparision(node, search_node)
            if compare == 0:
                return True

            elif compare == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    return False

            else:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    return False
    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while (len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s


tree = Tree()
tree.insert(5)
tree.insert(6)
tree.insert(4)
tree.insert(2)

print(f"""
search for 8: {tree.search(8)}
search for 4: {tree.search(4)}
""")
print(tree)
