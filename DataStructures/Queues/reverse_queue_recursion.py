class Node:
    def __init__(self, value):
        self.value  = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail= None
        self.num_elements = 0

    def enqueue(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head

        else:
            self.tail.next = node
            self.tail = self.tail.next

        self.num_elements += 1

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def dequeue(self):
        if self.is_empty():
            return None

        else:
            tmp = self.head
            self.head = self.head.next
            self.num_elements -= 1
            return tmp.value


def reverse_queue(queue):
    if queue.is_empty():
        return None
    tmp = queue.head.value
    queue.dequeue()
    reverse_queue(queue)
    queue.enqueue(tmp)


def test_function(test_case):
    queue = Queue()
    for num in test_case:
        queue.enqueue(num)

    reverse_queue(queue)
    index = len(test_case) - 1
    while not queue.is_empty():
        removed = queue.dequeue()
        if removed != test_case[index]:
            print("Fail")
            return
        else:
            index -= 1
    print("Pass")


if __name__ == '__main__':
    test_case_1 = [1, 2, 3, 4]
    test_function(test_case_1)

    test_case_2 = [1]
    test_function(test_case_2)

