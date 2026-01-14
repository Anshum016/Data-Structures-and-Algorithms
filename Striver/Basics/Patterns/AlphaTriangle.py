class solution(object):
    def pattern(self, n):
        for i in range(n):
            start = 65 + n - i - 1   # starting letter
            for j in range(i + 1):
                print(chr(start + j), end=" ")
            print()

sol = solution()
sol.pattern(5)
