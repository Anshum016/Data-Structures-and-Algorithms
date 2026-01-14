class Solution(object):
    def pattern1(self, n):
        # Upper pyramid
        for i in range(n):
            for j in range(n - i - 1):
                print(" ", end="")
            for k in range(2*i + 1):
                print("*", end="")
            print()

    def pattern2(self, n):
        # Lower inverted pyramid
        for i in range(n - 1):
            for j in range(i + 1):
                print(" ", end="")
            for k in range(2*(n - i - 1) - 1):
                print("*", end="")
            print()


sol = Solution()
sol.pattern1(4)
sol.pattern2(4)
