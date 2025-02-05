class ListNode():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next=next
    def merge(list1,lis2):
        dummy=ListNode()
        current=dummy

        while list1 and list2:
          if list1.val < list2.val:
              current.next = list1
              list1 = list1.next
          else:
              current.next=list2
              list2 = list2.next
          current = current.next       

        current.next=list1 if list1 else list2
        return dummy.next    
    
list1=[1,2,4]
list2=[1,3,4]
result=merge(list1,list2)
print("Our Answer is",result)