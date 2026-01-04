class Solution(object):
    def pattern(self,n):
        for i in range(n):
            for j in range(n):
                print("*",end="")
            print()    
               

sol = Solution()
sol.pattern(4)