
class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return

        node = DoubleNode(value)

        self.tail.next = node
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

        return


if __name__ == '__main__':
    linked_list2 = DoublyLinkedList()
    linked_list2.append(1)
    linked_list2.append(-2)
    linked_list2.append(4)

    print("Going forward through the list, should print 1, -2, 4")
    node = linked_list2.head
    while node:
        print(node.value)
        node = node.next

    print("\nGoing backward through the list, should print 4, -2, 1")
    node = linked_list2.tail
    while node:
        print(node.value)
        node = node.prev
