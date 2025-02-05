class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

def solution(head):
    estart=Node(0)
    ostart=Node(0)

    eend=estart
    oend=ostart
    
    curr = head

    while curr is not None:
        val=curr.data
        if val % 2 ==0:
            eend.next=curr
            eend=eend.next

        else:
            oend.next=curr    
            oend=oend.next

        curr = curr.next
        
    oend.next = None    

    eend.next=ostart.next

    return estart.next

def printlist(head):
    while head is not None:
        print(head.data,end="->")
        head=head.next
    print("None")

if __name__ == "__main__":
    head = Node(0)
    head.next = Node(1)
    head.next.next = Node(4)
    head.next.next.next = Node(6)
    head.next.next.next.next = Node(9)
    head.next.next.next.next.next = Node(10)
    head.next.next.next.next.next.next = Node(11)


    printlist(head)


    result = solution(head)

    printlist(result)



