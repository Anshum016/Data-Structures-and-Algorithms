from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_same_tree(s, t):
    if not s and not t:
        return True
    if not s or not t:
        return False
    return (s.data == t.data and 
            is_same_tree(s.left, t.left) and 
            is_same_tree(s.right, t.right))

def is_subtree(root, subRoot):  
    if not root:
        return False  
    
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if is_same_tree(node, subRoot):
            return True  

        if node.left:
            queue.append(node.left)
    
        if node.right:
            queue.append(node.right)

    return False  

# Constructing the main tree (root)
root = Node(3)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(2)

# Constructing the subtree (subRoot)
subRoot = Node(4)  
subRoot.left = Node(1)
subRoot.right = Node(2)

# Checking if subRoot is a subtree of root
print(is_subtree(root, subRoot))  
