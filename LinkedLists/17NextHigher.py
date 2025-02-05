class Node():
    def __init__(self,data):
        self.data=data
        self.arbit=None
        self.next=None

def segregate(head):
    curr = head
    while curr is not None:
        if curr.next is not None and curr.data < curr.next.data:
             curr.arbit = curr.next
        curr=curr.next
    
    return head

def printlist(head):
    while head is not None:
        # Print both data and arbit data (if arbit is not None)
        arbit_data = head.arbit.data if head.arbit else None
        print(f"{head.data} (arbit -> {arbit_data})", end=" -> ")
        head = head.next
    print("None")

if __name__ == "__main__":
    head = Node(5)
    head.next = Node(10)
    head.next.next = Node(2)
    head.next.next.next = Node(3)      


    # head.arbit = None  
    # head.next.arbit = None      
    # head.next.next.arbit = None 
    # head.next.next.next.arbit = None  


    printlist(head)

    result=segregate(head)

    printlist(result)