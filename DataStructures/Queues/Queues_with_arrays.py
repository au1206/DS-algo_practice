
"""
Functionality
Once implemented, our queue will need to have the following functionality:

enqueue - adds data to the back of the queue
dequeue - removes data from the front of the queue
front - returns the element at the front of the queue
size - returns the number of elements present in the queue
is_empty - returns True if there are no elements in the queue, and False otherwise
_handle_full_capacity - increases the capacity of the array, for cases in which the queue would otherwise overflow
Also, if the queue is empty, dequeue and front operations should return None.

"""


class Queue:
    def __init__(self, initial_size=20):
        self.arr = [0]*initial_size
        self.num_elements = 0
        self.tail = 0
        self.head = -1

    def enqueue(self, data):

        if self.num_elements == len(self.arr):
            print("array full")
            self._handle_queue_capacity_full()

        self.arr[self.tail] = data
        self.num_elements += 1
        self.tail = (self.tail+1) % len(self.arr)

        if self.head == -1:
            self.head = 0

    def size(self):
        return self.num_elements

    def isempty(self):
        return self.num_elements == 0

    def front(self):
        if self.isempty():
            return None
        return self.arr[self.head]

    def dequeue(self):
        if self.isempty():
            self.head = -1
            self.tail = 0
            return None
        value = self.arr[self.head]
        self.head = (self.head+1) % len(self.arr)
        self.num_elements -= 1
        return value

    def _handle_queue_capacity_full(self):
        old_arr = self.arr
        self.arr = [0] * 2*(len(old_arr))

        idx = 0
        for i in range(self.head, len(old_arr)):
            self.arr[idx] = old_arr[i]
            idx += 1

        for i in range(0, self.head):
            self.arr[idx] = old_arr[i]
            idx += 1

        self.head = 0
        self.tail = idx


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
