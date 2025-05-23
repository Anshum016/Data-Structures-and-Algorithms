class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

    head = None

def swap(a,b):
        temp = a.data
        a.data = b.data
        b.data = temp
        
def zigzag(node,flag):
    if (node==None or node.next==None):
        return node
    if (flag==0):
        if(node.data > node.next.data):
            swap(node,node.next)
        return zigzag(node.next,1)
    else:
        if(node.data < node.next.data):
            swap(node,node.next)
        return zigzag(node.next,0)
    
def printlist(head):
    while head is not None:
        print(head.data,end="->")
        head = head.next
    print("None")    

if __name__ == "__main__":

 head = Node(11)
 head.next = Node(15)
 head.next.next = Node(20)
 head.next.next.next = Node(5)
 head.next.next.next.next = Node(10)

printlist(head)
flag=0
zigzag(head,flag)
printlist(head) 




             


        