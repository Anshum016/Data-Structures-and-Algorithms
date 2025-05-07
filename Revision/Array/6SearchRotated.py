def Search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # If left part is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # search left
            else:
                left = mid + 1   # search right

        # Else right part must be sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # search right
            else:
                right = mid - 1  # search left

    return -1

nums = [6, 7, 8, 1, 2, 3, 4, 5]
target = 3
print(Search(nums, target))  
