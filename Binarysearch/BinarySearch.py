def BinarSearch(nums,target):
    n = len(nums)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif mid  < target:
            left = mid + 1
        else: 
            right = mid - 1
    return -1

nums = [1, 2, 3, 4, 5]
k = 3
print(BinarSearch(nums,k))



