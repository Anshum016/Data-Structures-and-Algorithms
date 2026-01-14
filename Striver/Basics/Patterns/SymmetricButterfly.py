class solution(object):
    def pattern(self,n):
        for i in range(1,n+1):
            for j in range(i):
                print("*",end="")
            for k in range(2*(n-i)):
                print(" ",end="")
            for z in range(i):
                print("*",end="") 
            print()
        for a in range(n-1,0,-1):
            for b in range(a):
                print("*",end="")
            for c in range(2*(n-a)):
                print(" ",end="")
            for d in range(a):
                print("*",end="")
            print()    

sol = solution()
sol.pattern(5)