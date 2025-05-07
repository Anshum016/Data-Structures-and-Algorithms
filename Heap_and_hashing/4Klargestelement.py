import heapq
def klargestelement(arr,k):
    min_heap = arr[:k]
    heapq.heapify(min_heap)

    for num in arr[k:]:
      if num > min_heap[0]:
        heapq.heapreplace(min_heap,num)

    return sorted(min_heap,reverse=True)

arr = [1, 23, 12, 9, 30, 2, 50]
k = 3

print(klargestelement(arr,k))
    







