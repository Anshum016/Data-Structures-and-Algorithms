class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def height(self):
        #left
        if self.left:
            left_height = self.left.height()
        else:
            left_height = 0
        #right    
        if self.right:
            right_height = self.right.height()
        else:
            right_height = 0

        return 1 + max(left_height,right_height)    

# Creating the tree
root = Tree(3)
root.left = Tree(9)
root.right = Tree(20)
root.right.left = Tree(15)
root.right.right = Tree(7)

print("Height of the tree:", root.height())  
