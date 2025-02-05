class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

def multiply(linkedlist1,linkedlist2):
   def linkedlistonumber(head): 
      str_num=""
      while head is not None:
          str_num +=str(head.data)
          head=head.next
      return int(str_num)

   num1=linkedlistonumber(linkedlist1)
   num2=linkedlistonumber(linkedlist2)     
   return num1 * num2

if __name__ == "__main__":
    linkedlist1 = Node(1)
    linkedlist1.next = Node(0)
    linkedlist1.next.next = Node(0)

    # Linked list 2: 1->0
    linkedlist2 = Node(1)
    linkedlist2.next = Node(0)

result = multiply(linkedlist1,linkedlist2)  
print(result)  