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

    # finding inorder successor
    def minValueNode(self, node):
        """
        given a non empty tree, returns min value found
        """
        current = node
        while current.has_left_child():
            current = current.get_left_child()

        return current

    def deleteNode(self, root, key):
        """
        deletes key and returns new root
        """

        # base case, root is empty
        if root is None:
            return root

        # root == key
        if root.get_value() == key:
            # c1: leaf node
            if not root.has_left_child() and not root.has_right_child():
                print("leaf node")
                return None

            # only one
            if not root.has_left_child() and root.has_right_child():
                return root.get_right_child()

            if not root.has_right_child() and root.has_left_child():
                return root.get_left_child()

            # both children exist
            # FIND THE INORDER SUCCESSOR: least value in the right subtree
            succ = self.minValueNode(root.get_right_child())

            # copy value of successor
            root.set_value(succ.get_value())

            # delete successor : easy since its a leaf
            root.set_right_child(self.deleteNode(root.get_right_child(), succ.get_value()))

        # key is smaller than root, go left
        elif key < root.get_value():
            root.set_left_child(self.deleteNode(root.get_left_child(), key))

        # if key > root go right
        else:
            root.set_right_child(self.deleteNode(root.get_right_child(), key))

        return root

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




tree2 = Tree()
tree2.insert(50)
tree2.insert(30)
tree2.insert(20)
tree2.insert(40)
tree2.insert(70)
tree2.insert(60)
tree2.insert(80)
print(tree2)


print('\n\n AFTER DELETION\n')
tree2.deleteNode(tree2.get_root(), 50)

print(tree2)

