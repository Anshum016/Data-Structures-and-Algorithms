class Tree:
    def __init__(self,data):
        self.data=data
        self.left = None
        self.right = None

    def add_child(self,data):
        #If there is duplicate data
        if data == self.data:
            return
        # Then add it to left subtree
        if data < self.data:           
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Tree(data)   
        #Then add it to right subtree
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Tree(data) 

    def in_order_traversal(self):
        elements=[] 
        
        # visit left subtree
        if self.left:
            elements += self.left.in_order_traversal()
         
        # visit base subtree 
        elements.append(self.data)

        # visit right subtree
        if self.right:
            elements +=self.right.in_order_traversal()

        return elements
        
    def search(self,val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False     
            
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def delete(self, val):
     if val < self.data:  # Search left
        if self.left:
            self.left = self.left.delete(val)  # Update left child
     elif val > self.data:  # Search right
        if self.right:
            self.right = self.right.delete(val)  # Update right child
     else:  # Found the node to delete
        if self.left is None and self.right is None:
            return None  # Case 1: No children, remove it
        if self.left is None:
            return self.right  # Case 2: Replace with right child
        if self.right is None:
            return self.left  # Case 2: Replace with left child
        
        # Case 3: Two children
        min_val = self.right.find_min()  # Find min in right subtree
        self.data = min_val  # Replace data with min value
        self.right = self.right.delete(min_val)  # Delete duplicate

     return self
                   

    
def build_tree(elements):
        root = Tree(elements[0])
        for i in range(1,len(elements)):
            root.add_child(elements[i])
        return root


if __name__ == "__main__":
    numbers=[17,4,1,20,9,23,18,34]
    numbers_tree = build_tree(numbers) 
    print(numbers_tree.search(20))       






