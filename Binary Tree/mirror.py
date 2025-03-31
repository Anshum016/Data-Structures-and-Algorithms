class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def inorder(root):
    elements=[]

    if root.left:
        elements +=inorder(root.left)     
    
    elements.append(root.data)
    
    if root.right:
        elements +=inorder(root.right)

    return elements    

def mirror(root): 
    if not root:
        return
    mirror(root.left)
    mirror(root.right)
    root.left , root.right = root.right , root.left        


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)

print("Before Mirroring")

print(inorder(root))

mirror(root)

print("after mirroring")

print(inorder(root))