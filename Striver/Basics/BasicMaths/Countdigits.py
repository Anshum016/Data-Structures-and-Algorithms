class solution(object):
    def pattern(self,n):
        return len(str(abs(n)))

sol = solution()
print(sol.pattern(500))    