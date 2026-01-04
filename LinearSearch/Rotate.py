from collections import deque

    
def rotate( nums, k):
       queue = deque(nums)
       n = len(nums)
       k = k % n

       for _ in range(k):
         number = queue.pop()
         queue.appendleft(number)
       return list(queue)  

nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums,k))     


from collections import deque

class Solution(object):
    def rotate(self, nums, k):
        d = deque()
        ans = []
        
        ## Taking elements in deque...
        for i in nums:
            d.append(i)

        ## Impleamenting logic...
        for i in range(k % len(nums)):
            item = d.pop()
            # print(item)
            d.appendleft(item)
        
        ## Returning element...
        for i in d:
            ans.append(i)
        nums[:] = ans