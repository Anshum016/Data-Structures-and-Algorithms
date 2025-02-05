class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def sort(head):
    cnt=[0,0,0]
    ptr = head

    while ptr is not None:
        cnt[ptr.data] +=1
        ptr=ptr.next

    idx=0
    ptr = head
    while ptr is not None:
        if cnt[idx] == 0:
            idx +=1
        else:
            ptr.data = idx
            cnt[idx] -=1
            ptr = ptr.next   

def printlist(head):
   while head is not None:
    print(head.data,end=" ")
    head=head.next
   print("\n")

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(0)

    print("Linked List before Sorting:")
    printlist(head)  # Call printlist to display the list

    sort(head)

    print("Linked List after Sorting:")
    printlist(head)  # Call printlist to display the sorted list
