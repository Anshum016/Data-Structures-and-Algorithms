class Stack:
    def __init__(self):
        self.values = []
        self.min_stack=[]

    def push(self, x):
        self.values.append(x)

        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if not self.isempty():
            front = self.values[-1]
            self.values = self.values[1:]
            return front
        return "Stack is empty"

    def isempty(self):
        return len(self.values) == 0
        

    def getMin(self):
        # if self.isempty():
        #     return "Stack is empty"
        # min_val = self.values[0]
        # for i in self.values:
        #     if i < min_val:
        #         min_val = i
        # return min_val
        if not self.min_stack:
            return "Empty"
        else:
            return self.min_stack[-1]

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.isempty()
stack.getMin()

print(stack.values)  # Now it prints the actual stack contents
print(stack.getMin())
