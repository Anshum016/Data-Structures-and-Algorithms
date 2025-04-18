class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def height(root):
    if not root:
        return 0
    left_height=height(root.left)
    right_height=height(root.right)

    return 1 + max(left_height,right_height)


def check_balanced(root):
    if not root:
        return True
    left_side_height = height(root.left)
    right_side_height = height(root.right)

    if abs(left_side_height - right_side_height) > 1:
        return False
    
    return check_balanced(root.left) and check_balanced(root.right)


root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.left.left = Node(4)


print(check_balanced(root))