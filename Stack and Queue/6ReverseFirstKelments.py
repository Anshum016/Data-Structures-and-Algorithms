class queue():
    def __init__(self):
        self.values = []
    
    def enqueue(self, x):
        self.values.append(x)
    
    def dequeue(self):
        if not self.values:
            return None
        front = self.values[0]
        self.values = self.values[1:]
        return front
    
    def size(self):
        return len(self.values)
    
    def front(self):
        if not self.values:
            return None
        return self.values[0]

def returnk(q, k):
    if k > q.size() or k <= 0:
        return q
    
    stack = []

    # Popping the first K elements from queue and storing in stack
    for _ in range(k):
        stack.append(q.dequeue())
    
    # Popping from stack and storing in queue (reversed order)
    while stack:
        q.enqueue(stack.pop())
    
    # Moving remaining elements to the rear
    for _ in range(q.size() - k):
        q.enqueue(q.dequeue())
    
    return q

# Initialize queue and enqueue elements
q = queue()
elements = [1, 2, 3, 4, 5]  # Define elements
for el in elements:
    q.enqueue(el)

k = 3
q = returnk(q, k)

# Print the modified queue
while q.size() > 0:
    print(q.dequeue(), end=" ")
