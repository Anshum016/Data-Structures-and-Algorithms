from collections import deque
class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def check_level_of_leave(root):
    if not root:
        return True
    queue=deque([(root,0)])
    leaf_level = -1

    while queue:
        node, level = queue.popleft()

        if not node.left and not node.right:
            if leaf_level == -1:
                leaf_level = level
            elif leaf_level != level:
                return False
            
        if node.left:
            queue.append((node.left,level + 1))
        if node.right:
            queue.append((node.right,level +1 ))


    return True


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(10)
root.left.right = Node(15)


print(check_level_of_leave(root))
                             
            


