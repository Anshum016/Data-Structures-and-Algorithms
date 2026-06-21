class Solution(object):
    def binary_Search(self,nums ,target ):
        n = len(nums)
        l = 0
        r = n-1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif mid < target:
                l = mid + 1
            elif mid > target:
                r = mid - 1

        return -1

sol = Solution()
nums = [-1,0,3,5,9,12]
target = 9
answer  = sol.binary_Search(nums,target)     
print(answer)       



