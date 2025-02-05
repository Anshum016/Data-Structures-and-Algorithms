class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete(node):
    if node is None or node.next is None:
        return node  # Base case: If list is empty or has one node, return it
    
    # Recursive call for the rest of the list
    next_node = delete(node.next)

    # Remove current node if the next node's value is greater
    if next_node.data > node.data:
        return next_node

    # Otherwise, connect current node to the next node
    node.next = next_node
    return node

def printlist(curr):
    while curr is not None:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

if __name__ == "__main__":
    head = Node(12)
    head.next = Node(15)
    head.next.next = Node(10)
    head.next.next.next = Node(11)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(2)

    print("Original List:")
    printlist(head)

    head = delete(head)

    print("Processed List:")
    printlist(head)
