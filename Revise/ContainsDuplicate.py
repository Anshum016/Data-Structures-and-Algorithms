def duplicate(nums):
    freq={}

    for i in nums:
        freq[i] = freq.get(i,0) + 1
    for i in freq:
        if freq[i] > 1:
           return True
        
    return False
nums=[1, 2, 2, 3, 3, 3, 4, 4, 4, 4]     
answer = duplicate(nums)
print(answer)