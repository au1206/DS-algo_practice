"""
Problem Statement
Given an input string consisting of only { and }, figure out the minimum number of reversals required to make the brackets balanced.

For example:

For input_string = "}}}}, the number of reversals required is 2.

For input_string = "}{}}, the number of reversals required is 1.

If the brackets cannot be balanced, return -1 to indicate that it is not possible to balance them.
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

    def top(self):
        return self.head.value


def minimum_reversal(arr):
    stack = Stack()
    count = 0
    for elem in arr:
        if stack.isempty():
            stack.push(elem)

        else:
            if stack.top() != elem:
                if elem == '}':
                    stack.pop()
                    continue
            stack.push(elem)

    ls = []
    while not stack.isempty():

        elem1 = stack.pop()
        elem2 = stack.pop()

        ls.append(elem1)
        ls.append(elem2)

        if elem1 == '{' and elem2 == '{':
            count += 1

        elif elem1 == '}' and elem2 == '}':
            count += 1

        elif elem1 == '{' and elem2 == '}':
            count += 2

    print(count)
    return count


def test_function(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = minimum_reversal(input_string)

    if output == expected_output:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':

    test_case_1 = ["}}}}", 2]
    test_function(test_case_1)

    test_case_2 = ["}}{{", 2]
    test_function(test_case_2)

    test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]
    test_function(test_case_3)

    test_case_4 = ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
    test_function(test_case_4)

    test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]
    test_function(test_case_5)


