def LinearSearch(nums,target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i

nums = [1, 2, 3, 4, 5]
target = 3
print(LinearSearch(nums,target))
        