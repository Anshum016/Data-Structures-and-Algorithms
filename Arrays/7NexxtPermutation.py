def nextPermutation(nums):
    n = len(nums)
    
    # Step 1: Find the first decreasing element from the end
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    if i >= 0:
        # Step 2: Find the element just bigger than nums[i]
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Step 3: Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]
    
    # Step 4: Reverse the elements after index i
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    
    return nums


nums=[1, 3, 2]

print(nextPermutation(nums))