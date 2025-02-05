class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def reverse(head):
    current = head
    new_head = None

    while current is not None:
        # Swap the next and prev Pointer
        current.prev , current.next = current.next , current.prev
        #new_head
        new_head = current
        # Move to prev node
        current = current.prev

    return new_head    


def printlist(head):
    while head is not None:
        print(head.data,end="->")
        head=head.next
    print("None")         


if __name__ == "__main__":

    head = Node(3)
    head.next = Node(4)
    head.next.prev = head
    head.next.next = Node(5)
    head.next.next.prev = head.next
    

    printlist(head)
    result = reverse(head)
    printlist(result)


