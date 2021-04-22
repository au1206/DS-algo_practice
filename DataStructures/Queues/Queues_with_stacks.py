"""
Implement a queue using stacks
"""


class Stack:
    def __init__(self):
        self.arr = []

    def size(self):
        return len(self.arr)

    def push(self, value):
        self.arr.append(value)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.arr.pop()


class Queue:
    def __init__(self):
        self.instream = Stack()
        self.outstream = Stack()

    def size(self):
        return self.instream.size() + self.outstream.size()

    def isempty(self):
        return self.size() == 0

    def enqueue(self, data):
        self.instream.push(data)

    def dequeue(self):
        if not self.outstream.arr:
            while self.instream.arr:
                self.outstream.push(self.instream.pop())

        return self.outstream.pop()


if __name__ == '__main__':
    # Setup
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Test size
    print("Pass" if (q.size() == 3) else "Fail")

    # Test dequeue
    print("Pass" if (q.dequeue() == 1) else "Fail")

    # Test enqueue
    q.enqueue(4)
    print("Pass" if (q.dequeue() == 2) else "Fail")
    print("Pass" if (q.dequeue() == 3) else "Fail")
    print("Pass" if (q.dequeue() == 4) else "Fail")
    q.enqueue(5)
    print("Pass" if (q.size() == 1) else "Fail")
