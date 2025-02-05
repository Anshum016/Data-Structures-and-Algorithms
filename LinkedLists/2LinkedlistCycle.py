class Node():
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def hascycle(head:Node) -> bool:
        slow=head
        fast=head

        while fast and fast.next:
            slow = head.next
            fast = fast.next.next

            if fast == slow:
                return True
        return False
def createlist():
    head=Node(3)
    node2=Node(4)
    node3=Node(5)
    node4=Node(6)

    head.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node2

    return head


head = createlist()
print(hascycle(head))
                      