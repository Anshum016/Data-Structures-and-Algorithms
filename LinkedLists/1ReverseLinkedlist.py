# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Recursive function to reverse the linked list
    def reverseList(self, head: ListNode) -> ListNode:
        # Base case: If the list is empty or has only one node
        if not head:
            return None

        # Assume we are reversing from the second node onward
        newHead = head
        if head.next:
            # Recursively reverse the rest of the list
            newHead = self.reverseList(head.next)

            # Make the next node point back to the current node
            head.next.next = head
            # Break the forward link to prevent cycles
            head.next = None
        
        # Return the new head of the reversed list
        return newHead

# Helper function to print a linked list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example usage
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print("Original Linked List:")
    printList(head)

    # Reverse the linked list
    solution = Solution()
    reversed_head = solution.reverseList(head)

    print("Reversed Linked List:")
    printList(reversed_head)
