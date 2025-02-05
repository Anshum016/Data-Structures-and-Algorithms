class node:
    def __init__(self,val):
        self.val=val  
        self.next=None
        self.prev=None

class Deque:
    def __init__(self):
       self.head=None
       self.tail=None

    def isEmpty(self):
        if self.head == None:
           print("List is empty")
        else:
            return self.head
        
    def insertfirst(self,val):
        new = node(val)
        if self.head == None: 
            self.head = self.tail = new
            return
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    def insertlast(self,val):
        new = node(val)
        if self.head == None: 
            self.head = self.tail = new
            return
        else:
            new.prev=self.tail
            self.tail.next = new
            self.tail = new

    def removefirst(self):
        if self.head == None:
         print("List is empty")
        else:
            self.head = self.head.next  # Move the head pointer to the next node
            if self.head != None:       # If the list is not empty after the update
               self.head.prev = None   # Set the new head's prev to None

    def removelast(self):
        if self.head == None:
         print("List is empty")
        else:
            self.tail = self.tail.prev 
            if self.tail != None:
                self.tail.next = None

    def display(self):
        if self.head == None:
         print("List is empty")
         return
        curr = self.head
        while curr != None:
           print(curr.val)
           curr = curr.next
        print()

    def size(self):
        curr = self.head
        len = 0
        while curr != None:
           len +=1
           curr = curr.next
        return len


class stack:
    def __init__(self):
      self.stack=Deque()
    def push(self,val):
       self.stack.insertlast(val)
    def pop(self):
       self.stack.removelast()
    def size(self):
       return self.stack.size()
    def display(self):
       self.stack.display()

class queue:
    def __init__(self):
      self.queue=Deque()
    def enqueue(self,val):
       self.queue.insertlast(val)
    def dequeue(self):
       self.queue.removefirst()   
    def size(self):
       return self.queue.size()
    def display(self):
       return self.queue.display()


s=stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
print("Stack Contents")
s.display()
print("Size",s.size())

q=queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
print("queue Contents")
q.display()
print("Size",q.size())
           
           

        

