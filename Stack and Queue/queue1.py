class queue():
    def __init__(self):
        self.values=[]
    def enqueue(self,x):
        self.values.append(x)
    def dequeue(self):
        front = self.values[0]
        self.values = self.values[1:]
        return front


q1=queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.values)