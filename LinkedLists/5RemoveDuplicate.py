class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def remove(head):
    hash_set=set()
    curr = head
    prev = None
    while curr is not None:
         #If the data is present in hash table
         if curr.data in hash_set:
             prev.next = curr.next
             curr = curr.next
         # IF it is not present in the hash table
         else:
             hash_set.add(curr.data)
             prev = curr
             curr = curr.next

    return head         
def printlist(head):
    curr = head
    while curr is not None:
          print(curr.data,end=" ")
          curr = curr.next
    print()

if __name__ == "__main__":
    head = Node(12)
    head.next=Node(11)
    head.next.next=Node(12)
    head.next.next.next=Node(21)
    head.next.next.next.next=Node(41)

    result=remove(head)
    printlist(result)

             