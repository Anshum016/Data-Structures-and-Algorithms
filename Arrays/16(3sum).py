def Sumof3(nums):
    res = []
    nums.sort()

    for i in range(len(nums)):
        # Skip duplicates for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Initialize the two pointers
        l = i + 1
        r = len(nums) - 1

        while l < r:
            s = nums[i] + nums[l] + nums[r]

            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))

                # Skip duplicates for the left pointer
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                # Skip duplicates for the right pointer
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                
                # Move the pointers after finding a valid triplet
                l += 1
                r -= 1

    return res

# Test the function
nums = [-1, 0, 1, 2, -1, -4]
print("The triplets are", Sumof3(nums))
print(len(nums))