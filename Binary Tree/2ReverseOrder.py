from collections import deque
class node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def reverse(root):  
        if not root:
            return
        queue = deque([root]) 
        stack=[]

        while queue:
            node = queue.popleft()
            stack.append(node.data)

            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return stack[::-1]            

if __name__ == "__main__":

   root = node(9)
   root.left = node(8)
   root.right = node(11)

print(reverse(root))   