def Product(nums):
    n = len(nums)
    ans = [1] * n

    for i in range(1,n):
        ans[i] = ans[i-1] * nums[i-1]

    right_product = 1

    for i in range(n-1, -1 , -1):
           ans[i] = ans[i] * right_product

           right_product = right_product * nums[i]

    return ans


nums = [1,2,3,4]
print("Product Array is",Product(nums))