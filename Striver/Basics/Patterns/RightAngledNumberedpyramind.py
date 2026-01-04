class solution(object):
    def pattern(self,n):
        for i in range(n):
            for j in range(0,i+1):
                print(j+1,end="")
            print()

sol = solution()
sol.pattern(5)