def ProductofArray(nums):
    n = len(nums) 
    ans = [1] * len(nums)

    prefix = 1
    for i in range(n):
        ans[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n-1,-1,-1):
        ans[i] *= suffix
        suffix *= nums[i]

    return ans

nums = [1, 2, 3, 4]
print(ProductofArray(nums))
    