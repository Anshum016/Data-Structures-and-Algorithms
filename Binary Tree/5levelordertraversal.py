from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None

def levelordertraversal(root):
    queue = deque([root])
    result=[]
    
    if not root:
        return None

    while queue:
        level_nodes = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.data)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(level_nodes)

    return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

print(levelordertraversal(root))



