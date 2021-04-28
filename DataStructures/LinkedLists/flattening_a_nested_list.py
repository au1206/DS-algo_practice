"""
Flattening a nested linked list
Suppose you have a linked list where the value of each node is a sorted linked list (i.e., it is a nested list).
Your task is to flatten this nested list—that is, to combine all nested lists into a single (sorted) linked list.

"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        node1 = self.head
        while node1.next is not None:
            node1 = node1.next

        node1.next = new_node


def merge(l1, l2):
    """
    :param l1: the first sorted Linkedlist to merge
    :param l2: the second sorted linked list to merge
    :return: l3: a merged sorted linked list
    """
    l3 = LinkedList()

    if l1 is None:
        return l2

    if l2 is None:
        return l1

    n1 = l1.head
    n2 = l2.head

    while n1 is not None or n2 is not None:
        if n2 is None:
            l3.append(n1)
            n1 = n1.next

        elif n1 is None:
            l3.append(n2)
            n2 = n2.next

        elif n1.value <= n2.value:
            l3.append(n1)
            n1 = n1.next

        else:
            l3.append(n2)
            n2 = n2.next

    return l3


class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)

    def _flatten(self, node):
        if node.next is None:
            return merge(node.value, None)
        return merge(node.value, self._flatten(node.next))


if __name__ == '__main__':

    print("testing Merge")
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(3)
    linked_list.append(5)

    second_linked_list = LinkedList()
    second_linked_list.append(2)
    second_linked_list.append(4)

    merged = merge(linked_list, second_linked_list)
    node = merged.head
    while node is not None:
        # This will print 1 2 3 4 5
        print(node.value, end=' ')
        node = node.next

    print('\nLets make sure it works with a None list')
    merged = merge(None, linked_list)
    node = merged.head
    while node is not None:
        # This will print 1 3 5
        print(node.value, end=' ')
        node = node.next

    print("\n\nTesting flatten")
    nested_linked_list = NestedLinkedList()
    nested_linked_list.append(linked_list)
    nested_linked_list.append(second_linked_list)

    flattened = nested_linked_list.flatten()

    node = flattened.head
    while node is not None:
        # This will print 1 2 3 4 5
        print(node.value, end=' ')
        node = node.next




