class Solution(object):
    def isArmstrong(self, n):
        duplicate = n
        lastdigit = 0
        sum = 0
        while n > 0:
            lastdigit = n % 10
            sum = sum + (lastdigit * lastdigit * lastdigit)
            n = n // 10 

        if sum == duplicate:
            return True
        else:
            return False        

sol = Solution()
print(sol.isArmstrong(153))        