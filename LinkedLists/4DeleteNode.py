class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def delete(delnode):

    if delnode is None or delnode.next is None:
        return

    temp = delnode.next
    delnode.data = temp.data

    delnode.next = temp.next

    del temp

def printlist(head):
    curr = head
    while curr:
        print(curr.data,end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":

  head = Node(4)
  head.next = Node(5)
  head.next.next = Node(6)
  head.next.next.next = Node(7)

  delete(head)

  printlist(head)

            
        