from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q2.put(x)  # Add new element to q2
        while not self.q1.empty():  # Move all elements from q1 to q2
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1  # Swap the queues

    def pop(self):
        if self.q1.empty():
            return "Underflow"  # Return message if stack is empty
        return self.q1.get()  # Remove and return the top element

    def top(self):
        if self.q1.empty():
            return "Empty stack"  # Return message if stack is empty
        return self.q1.queue[0]  # Return the top element without removing

    def is_empty(self):
        return self.q1.empty()  # Check if the stack is empty

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())        # Expected: 3
    print(s.top())        # Expected: 2
    print(s.is_empty())   # Expected: False
