

class Queue:
    def __init__(self, initial_size=20):
        self.arr = [0]*initial_size
        self.num_elements = 0
        self.tail = 0
        self.head = -1

    def enqueue(self, data):
        if self.num_elements == len(self.arr):
            print("array full")

        self.arr[self.tail] = data
        self.tail += 1
        self.num_elements += 1
        if self.head == -1:
            self.head = 0






