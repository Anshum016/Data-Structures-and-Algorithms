class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
def Intersection(head1,head2):
    ptr1=head1
    ptr2=head2

    if ptr1 is None or ptr2 is None:
        return None

    while ptr1 != ptr2:
        if ptr1:
         ptr1 = ptr1.next  
        else:
            ptr1 = head2
        if ptr2:
            ptr2 = ptr2.next
        else:
            ptr2 = head1
    return ptr1

# def printlist(head):
#     while head is not None:
#         print(head.data,end="->")   
#         head = head.next
#     print("None")

if __name__ == "__main__":
    head1=Node(10)
    head1.next=Node(15)
    head1.next.next=Node(30)

    head2=Node(3)
    head2.next=Node(6)
    head2.next.next=Node(9)
    head2.next.next.next = head1.next

result=Intersection(head1,head2)
print(result.data)