class Node():
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None

def invert(root):
    if not root:
        return None

    # swap left and right
    root.left , root.right = root.right , root.left

    invert(root.left)
    invert(root.right)

    return root

from collections import deque

def tree(root):
    if not root:
        return None
    queue = deque([root])
    result =[]

    while queue:
        node = queue.popleft()
        result.append(node.data)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result
               




root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(9)


print("Original Tree:", tree(root))


invert(root)


print("Inverted Tree:", tree(root))





               