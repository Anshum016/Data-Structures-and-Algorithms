class solution(object):
    def pattern(self,n):
        for i in range(n):
            for j in range(n-i):
                print("*",end="")
            print()

sol = solution()
sol.pattern(5)                
