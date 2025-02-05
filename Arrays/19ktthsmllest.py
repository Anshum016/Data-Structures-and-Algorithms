import heapq
def kthsmallest(arr,k):
    heap=[]
    for i in range(len(arr)-1):
        heapq.heappush(heap,arr[i])
        # heapq._heapify_max(heap)

        if (len(heap)>k):
            heapq.heappop(heap)

    return heap[0]

arr=[2, 3, 1, 20, 15]
k = 4 

print("Our answer is",kthsmallest(arr,k))        
