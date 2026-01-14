class solution(object):
    def pattern(self,n):
        for i in range(1,n+1):
            #spaces
            for s in range(n-i):
                print(" ",end="")
            
            #increasing letter
            for j in range(i):
                print(chr(65+j),end="")


            #decreasing letter
            for k in range(i-2,-1,-1):
                print(chr(65 + k),end="")

            print()

sol = solution()
sol.pattern(5)

