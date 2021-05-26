"""
merge two sorted linked lists together
"""


# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = Node(value)
        node.next = self.head
        self.head = node

    def append(self, value):
        """
        not keeping track of tail therefore O(n) operation, else could have been O(1)
        """

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)


def merge(head1, head2):
    if head1 is None:
        return head2

    if head2 is None:
        return head1

    c = Node()
    if head1.val <= head2.val:
        c = head1
        c.next = merge(head1.next, head2)

    else:
        c = head2
        c.next = merge(head1, head2.next)

    return c


if __name__ == '__main__':
    a = [1,3,5,11]
    l1 = LinkedList()
    for elem in a:
        l1.append(elem)

    b = [2,4,6,8]
    l2 = LinkedList()
    for elem in b:
        l2.append(elem)

    c = merge(l1.head, l2.head)

    while c:
        print(c.val, end=' ')
        c = c.next
