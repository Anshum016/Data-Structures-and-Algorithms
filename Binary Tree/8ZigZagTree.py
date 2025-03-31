from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def zigzag(root):
        
        if not root:
            return 
        result=[]
        queue = deque([root])
        left_to_right=True        


        while queue:
            level_size=len(queue)
            level_nodes=deque()


            for _ in range(level_size):
                node = queue.popleft()

                if left_to_right:
                    level_nodes.append(node.data)
                else:
                    level_nodes.appendleft(node.data)    

            
            
                if node.left:
                    queue.append(node.left)
            
                if node.right:
                    queue.append(node.right)

            result.extend(level_nodes)
            left_to_right = not left_to_right        

        return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)


print(zigzag(root))


