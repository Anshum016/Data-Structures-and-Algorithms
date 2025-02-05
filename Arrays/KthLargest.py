import heapq
def largest(nums,k):
    heap =[]
    for num in nums:
        heapq.heappush(heap,num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0 ]        
nums = [3,2,1,5,6,4]
k = 2
print("The kth Largest number is",largest(nums,k))