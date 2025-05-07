def topk(nums,k):
    freq={}

    for num in nums:
        freq[num] = freq.get(num,0) + 1
    keys=list(freq.keys())    
    keys.sort(key=lambda x: freq[x] , reverse=True )

    return keys[:k]

nums = [1, 2, 2, 3, 1, 4, 2]
k = 2
print(topk(nums,k))