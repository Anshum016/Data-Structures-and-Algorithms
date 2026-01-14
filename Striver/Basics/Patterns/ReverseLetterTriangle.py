class solution(object):
    def pattern(self,n):
        for i in range(1,n+1):
            for j in range(1,n-i+2):
                print(chr(64+j),end="")
            print()   

sol = solution()
sol.pattern(4)