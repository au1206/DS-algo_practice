"""
We will be using stacks to make sure the parentheses are balanced in mathematical expressions such as:
 ((32+8)∗(5/2))/(2+6).  In real life you can see this extend to many things such as text editor plugins and interactive
 development environments for all sorts of bracket completion checks.

Take a string as an input and return True if it's parentheses are balanced or False if it is not.

"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.num_elements += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.num_elements += 1

    def isempty(self):
        return self.num_elements == 0

    def size(self):
        return self.num_elements

    def pop(self):
        if self.isempty():
            return None
        tmp = self.head
        self.head = self.head.next
        self.num_elements -= 1
        return tmp.value


def checker(data):
    """
    :param data: query string to check the balance
    :return: bool: True if balanced else False

    """
    stack = Stack()
    for char in data:
        if char in "(":
            stack.push(char)
        elif char == ")":
            # condition of hitting ) before (
            if stack.pop() is None:
                return False

    if stack.size() == 0:
        return True

    else:
        return False


if __name__ == '__main__':
    print("Pass" if (checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
    print("Pass" if not (checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")

