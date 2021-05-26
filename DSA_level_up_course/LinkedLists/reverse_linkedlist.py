"""
reverse a linked list
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if self.head is None:
            self.head = Node(val)

        else:
            node = self.head
            while node.next:
                node = node.next

            node.next = Node(val)

    def to_list(self):
        out_list = []
        node = self.head
        while node:
            out_list.append(node.val)
            node = node.next

        return out_list


def reverse(node):
    if not node or not node.next:
        return node

    p = reverse(node.next)
    node.next.next = node
    node.next = None
    return p

# For ITERATIVE
# prev = None
# while node
# temp = current.next
# current.next = prev
# prev = current
# current = temp
def reverse_itr(node1):
    if not node1 or not node1.next:
        return node1

    prev = None
    node = node1
    while node:
        temp = node.next
        node.next = prev
        prev = node
        node = temp

    return prev


if __name__ == '__main__':
    a = [1,2,3,4]
    l = LinkedList()
    for elem in a:
        l.append(elem)

    print(l.to_list())
    l2 = reverse_itr(l.head)

    while l2:
        print(l2.val, end=' ')
        l2 = l2.next
