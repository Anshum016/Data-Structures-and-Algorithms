class Solution(object):
    def pattern1(self, n):
        for i in range(1, n + 1):
            for j in range(i):
                print("*", end="")
            print()

    def pattern2(self, n):
        for i in range(n - 1, 0, -1):
            for j in range(i):
                print("*", end="")
            print()


sol = Solution()
sol.pattern1(4)
sol.pattern2(4)
