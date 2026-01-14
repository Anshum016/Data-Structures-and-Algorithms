class solution(object):
    def pattern(self,n):
        for i in range(1,n+1):
            print("*",end="")
        print()    
        for j in range(1,n-2):
            print("*",end="")
            for a in range(n-2):
                print(" ",end="")
            print("*")
        for z in range(1,n+1):
            print("*",end="")            
        print()    

sol = solution()
sol.pattern(7)