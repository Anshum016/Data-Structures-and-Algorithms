from collections import deque
class Node:
    def __init__(self,data):
       self.data=data
       self.left=None
       self.right=None

def is_isomorphic(root1,root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.data != root2.data:
        return False
    
    same_structure=is_isomorphic(root1.left,root2.left) and is_isomorphic(root1.right,root2.right)
    flipped_Structure=is_isomorphic(root1.left,root2.right) and is_isomorphic(root1.right,root2.left)


    return same_structure or flipped_Structure

# Constructing Tree 1
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.right = Node(6)
root1.left.right.left = Node(7)
root1.left.right.right = Node(8)


# Constructing Tree 2
root2 = Node(1)
root2.left = Node(3)
root2.right = Node(2)
root2.left.right = Node(6)
root2.right.left = Node(4)
root2.right.right = Node(5)
root2.right.left.left = Node(8)
root2.right.left.right = Node(7)


print(is_isomorphic(root1,root2))




