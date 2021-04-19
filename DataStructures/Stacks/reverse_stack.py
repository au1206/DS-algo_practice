"""
Problem Statement
Reverse a stack. If your stack initially has 1, 2, 3, 4 (4 at the top and 1 at the bottom), after reversing the order must
be 4, 3, 2, 1 (4 at the bottom and 1 at the top).

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        node = Node(value)
        if self.num_elements == 0:
            self.head = node

        else:
            node.next = self.head
            self.head = node

        self.num_elements += 1

    def pop(self):
        if self.num_elements == 0:
            return None

        tmp = self.head
        self.head = self.head.next
        self.num_elements -= 1
        return tmp.value

    def size(self):
        return self.num_elements

    def isempty(self):
        return self.num_elements == 0

    def print_stack(self):
        while not self.isempty():
            elem = self.pop()
            print(elem, end=' ')


# Different Stack ---- Soft reverse
def reverse_stack1(stack):
    """
    This method will return a different reversed stack
    :param stack: Stack to reverse
    :return: Reversed Stack
    """

    rev_stack = Stack()
    while not stack.isempty():
        elem = stack.pop()
        rev_stack.push(elem)
    return rev_stack


# Same Stack --- proper reverse
def reverse_stack(stack):
    holder_stack = Stack()
    while not stack.isempty():
        popped_element = stack.pop()
        holder_stack.push(popped_element)
    _reverse_stack_recursion(stack, holder_stack)


def _reverse_stack_recursion(stack, holder_stack):
    if holder_stack.isempty():
        return
    popped_element = holder_stack.pop()
    _reverse_stack_recursion(stack, holder_stack)
    stack.push(popped_element)

#
# # without holder stack, although same space complexity, because temps would end up taking same space or even more, as 2 tmps
# def insert_at_bottom(stack, item):
#     if stack.isempty():
#         stack.push(item)
#
#     else:
#         tmp = stack.pop()
#         insert_at_bottom(stack, item)
#         stack.push(tmp)
#
#
# def reverse_stack2(stack):
#     if not stack.isempty():
#         temp = stack.pop()
#         reverse_stack2(stack)
#         insert_at_bottom(stack, temp)


def test_function1(test_case):
    stack = Stack()
    for num in test_case:
        stack.push(num)

    stack = reverse_stack1(stack)
    index = 0
    while not stack.isempty():
        popped = stack.pop()
        if popped != test_case[index]:
            print("Fail")
            return
        else:
            index += 1
    print("Pass")


def test_function2(test_case):
    stack = Stack()
    for num in test_case:
        stack.push(num)

    reverse_stack(stack)
    index = 0
    while not stack.isempty():
        popped = stack.pop()
        if popped != test_case[index]:
            print("Fail")
            return
        else:
            index += 1
    print("Pass")


if __name__ == '__main__':
    test_case_1 = [1, 2, 3, 4]
    test_function1(test_case_1)

    test_case_2 = [1]
    test_function1(test_case_2)

    test_case_1 = [1, 2, 3, 4]
    test_function2(test_case_1)

    test_case_2 = [1]
    test_function2(test_case_2)



