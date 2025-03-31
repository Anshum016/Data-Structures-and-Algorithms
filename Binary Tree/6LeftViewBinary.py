from collections import deque
class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def leftview(root):
    if not root:
        return None

    queue = deque([root])
    result=[]

    while queue:
        result.append(queue[0].data)

        for _ in range(len(queue)):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)   

    return result



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

print(leftview(root))  




        
        









