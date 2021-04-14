"""
Functionality
Our goal will be to implement a `Stack` class that has the following behaviors:

1. `push` - adds an item to the top of the stack
2. `pop` - removes an item from the top of the stack (and returns the value of that item)
3. `size` - returns the size of the stack
4. `top` - returns the value of the item at the top of stack (without removing that item)
5. `is_empty` - returns `True` if the stack is empty and `False` otherwise

"""


class Stack:
    def __init__(self, initial_size=10):
        self.arr = [0]*initial_size
        self.next_idx = 0
        self.num_elements = 0

    def push(self, data):
        if self.next_idx == len(self.arr):
            print("Stack Overflow, increasing Stack space")
            self._handle_stack_capacity_full()

        self.arr[self.next_idx] = data
        self.next_idx += 1
        self.num_elements += 1
        return self.arr[self.next_idx]

    def _handle_stack_capacity_full(self):
        old_arr = self.arr
        self.arr = [0]*(2*len(old_arr))
        for idx, elem in enumerate(old_arr):
            self.arr[idx] = elem

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def top(self):
        return self.arr[self.arr[self.next_idx]]

    def pop(self):
        if self.is_empty():
            self.next_idx = 0
            return None
        self.next_idx -= 1
        self.num_elements -= 1
        return self.arr[self.next_idx]


if __name__ == '__main__':
    MyStack = Stack()

    MyStack.push("Web Page 1")
    MyStack.push("Web Page 2")
    MyStack.push("Web Page 3")

    print(MyStack.arr)

    MyStack.pop()
    MyStack.pop()

    print("Pass" if (MyStack.arr[0] == 'Web Page 1') else "Fail")

    MyStack.pop()

    print("Pass" if (MyStack.pop() == None) else "Fail")
