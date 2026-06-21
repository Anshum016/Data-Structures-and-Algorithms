class Solution(object):
    def merge(self,nums1,m,nums2,n):
        x = m - 1
        y = n - 1

        for z in range(m + n - 1 ,-1,-1):
            if x < 0:
                nums1[z] = nums2[y]
                y -=1
            elif y < 0:
                break
            elif nums1[x] > nums2[y]:
                nums1[z] = nums1[x]
                x -=1
            else:
                nums1[z] = nums2[y]
                y -=1

sol = Solution()
nums1 = [1,2,3,0,0,0] 
m = 3
nums2 = [2,5,6]
n = 3
answer  = sol.merge(nums1,m,nums2,n)
print(answer)


