class Node:
    def __init__(self,data=0,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def find_lowest_common(root,p,q):
   while root:
        if p.data < root.data and q.data < root.data:
           root = root.left
        if p.data > root.data and q.data > root.data:
            root = root.right
        else:
            return root.data 
        


n0 = Node(0)
n3 = Node(3)
n5 = Node(5)
n4 = Node(4, n3, n5)
n2 = Node(2, n0, n4)
n7 = Node(7)
n9 = Node(9)
n8 = Node(8, n7, n9)
root = Node(6, n2, n8)
                
p = n2  
q = n4


print(find_lowest_common(root,p,q))

