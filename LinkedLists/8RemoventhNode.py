class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

def remove(head,n):
    p1=head
    p2=head
    prev=None
    #Move p1 pointer ahead by n 
    for i in range(n):
        p1=p1.next
    #Now move p1 and p2 pointer ahead by 1 until p1 pointer reaches at the end of list    
    while p1 is not None:
        p1=p1.next
        prev=p2
        p2=p2.next
    #If prev is none meaning the node which we want to remove is the first node    
    if not prev:
        return head.next
    #Now map the prev node with the next of p2 node
    prev.next=p2.next
    return head

def printlist(head):
    while head is not None:
        print(head.data,end="->")
        head=head.next
    print("None")    
 
if __name__ == "__main__":
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)

n=2
result=remove(head,n)
printlist(result)

