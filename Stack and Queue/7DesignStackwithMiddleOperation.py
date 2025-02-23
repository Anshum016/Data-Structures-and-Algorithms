from collections import deque

class StackWithMiddle:
    def __init__(self):
        self.stack = []  # First half of elements
        self.deque = deque()  # Second half of elements

    def push(self, data):
        self.deque.append(data)

        # Balancing the stack and deque
        if len(self.deque) > len(self.stack) + 1:
            self.stack.append(self.deque.popleft())  

    def pop(self):
        if not self.deque:
            return None  # Stack is empty
        
        popped_data = self.deque.pop()

        # Balance sizes after popping
        if len(self.deque) < len(self.stack):
            self.deque.appendleft(self.stack.pop())

        return popped_data  # ✅ Return the popped element

    def findMiddle(self):
        if not self.deque:
            return None  # Stack is empty
        return self.deque[0]  # Middle element is the front of the deque

    def deleteMiddle(self):
        if not self.deque:
            return None  # Stack is empty
        
        middle_data = self.deque.popleft()

        # Balance sizes after deletion
        if len(self.deque) < len(self.stack):
            self.deque.appendleft(self.stack.pop())

        return middle_data  # ✅ Return the deleted middle element


stack = StackWithMiddle()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print("Middle element:", stack.findMiddle())  # Output: 3
stack.deleteMiddle()
print("Middle element after deletion:", stack.findMiddle())  # Output: 2
stack.pop()
print("Middle element after pop:", stack.findMiddle())  # Output: 2
