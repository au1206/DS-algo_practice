class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        if not self.head:
            self.head = Node(value)
            return

        node = Node(value)
        node.next = self.head
        self.head = node

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])


"""
implement a prepend function in the linkedlist
create a new linked list and for each element in original prepend to the new list
complexity O(n) in time and O(n) in space
"""


def reverse1(linked_list):
    new_list = LinkedList()
    for elem in linked_list:
        new_list.prepend(elem)

    return new_list


# Time complexity O(N) --- without using prepend
def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    new_list = LinkedList()
    new_list.head = None   # head of new list

    # A bit of a complex operation here. We want to take the
    # node from the original linked list and prepend it to
    # the new linked list
    for val in linked_list:
        new_node = Node(val)
        new_node.next = new_list.head
        new_list.head = new_node
    # new_list.head = prev_node
    return new_list


if __name__ == '__main__':
    llist = LinkedList()
    for value in [4, 2, 5, 1, -3, 0]:
        llist.append(value)
    print(llist)

    flipped = reverse(llist)
    is_correct = list(flipped) == list([0, -3, 1, 5, 2, 4]) and list(llist) == list(reverse(flipped))
    print("Pass" if is_correct else "Fail")
