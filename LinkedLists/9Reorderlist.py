class Node():
  def __init__(self,data):
    self.data=data
    self.next=None
def reorder(head):
  #Divide the list into two halves
  slow = head
  fast = head
  while fast and fast.next is not None:
    slow=slow.next
    fast=fast.next.next
  #Now the slow pointer is pointing towards the middle at 3

  # 1->2->3->4->5  
  #Now reversing the second half
  prev=None
  curr=slow.next  
  slow.next=None
  while curr:
    temp=curr.next
    curr.next=prev
    prev = curr
    curr = temp

  #Now merging the two halves
  first = head
  second = prev
  while second:
    temp1=first.next
    temp2=second.next
    first.next=second
    second.next=temp1
    first=temp1
    second=temp2

def printlist(head):
  while head is not None:
    print(head.data,end="->")
    head=head.next
  print("None")

if __name__ == "__main__":
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)  


  
  print("Original List:")
  printlist(head)

  reorder(head)

  print("Reordered List:")
  printlist(head)


 

    