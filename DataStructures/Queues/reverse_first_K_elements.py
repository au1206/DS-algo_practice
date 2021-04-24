"""
Reversing the first K elements of a Queue

Given an integer k and a queue of integers, we need to reverse the order of the first k elements of the queue,
leaving the other elements in the same relative order.
"""


class Stack:
    def __init__(self):
        self.arr = []

    def push(self, value):
        self.arr.append(value)

    def size(self):
        return len(self.arr)

    def pop(self):
        return self.arr.pop()


class Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, value):
        self.arr.append(value)

    def size(self):
        return len(self.arr)

    def dequeue(self):
        return self.arr.pop(0)


def reverse_first_k(queue, k):
    """

    :param queue: the target queue
    :param k: the index till where reverse is needed
    :return: output queue with k reverse
    """

    stack = Stack()
    if queue.size() == 0:
        return None

    if k > queue.size():
        print("K too large")
        return None

    else:
        for i in range(k):
            stack.push(queue.dequeue())

        while stack.size() != 0:
            queue.enqueue(stack.pop())

        n = queue.size()

        for j in range(k, n):
            queue.enqueue(queue.dequeue())


def Print(Queue):
    tmp = Queue
    while tmp.size() != 0:
        print(tmp.dequeue(), end=" ")


def test(testcase):
    queue = Queue()
    for elem in testcase[0]:
        queue.enqueue(elem)

    reverse_first_k(queue, testcase[1])
    Print(queue)


if __name__ == '__main__':

    print("\n\ntestcase ...")
    testcase1 = ([1, 2, 3, 4, 5], 3)
    test(testcase1)

    print("\n\ntestcase ...")
    testcase2 = ([10, 20], 3)
    test(testcase2)

    print("\n\ntestcase ...")
    testcase3 = ([], 1)
    test(testcase3)

