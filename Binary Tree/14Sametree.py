from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def is_same(root1,root2):
    queue1=deque([root1])
    queue2=deque([root2])

    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.data != root2.data:
        return False
    return is_same(root1.left,root2.left) and is_same(root1.right,root2.right)

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)


root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)   

print(is_same(root1,root2))