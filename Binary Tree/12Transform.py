class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def Transform(root):
    if root is None :
        return 0

    left_sum=Transform(root.left)
    right_sum=Transform(root.right)

    old_value = root.data

    root.data = left_sum + right_sum

    return old_value + root.data

# left root right 
def inorder(root):
    if root is None :
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


root = Node(10)
root.left = Node(-2)
root.right = Node(6)
root.left.left = Node(8)
root.left.right = Node(-4)
root.right.left = Node(7)
root.right.right = Node(5)

Transform(root)

inorder(root)
