class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

def deleteloop(head):
    if head and head.next is None:
         return None
    slow=head
    fast=head
    #Detection of loop
    while fast and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
         
        if slow == fast:
             break
    if slow !=fast:
         return  
    #Removal of loop
    slow=head
    #If the loop starts from the beginning
    if slow == fast:
        while fast.next != slow:
            fast = fast.next
    else:
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
    fast.next = None                
def printlist(head):         
    while head is not None:
        print(head.data,end="->")
        head=head.next
    print()

if __name__ == "__main__":
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    head.next.next.next.next=head.next.next

deleteloop(head)
printlist(head)                