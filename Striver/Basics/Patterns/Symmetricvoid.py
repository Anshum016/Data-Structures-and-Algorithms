class solution(object):
    def pattern(self,n):
        for i in range(1,n+1):
            #stars
            for j in range(n-i+1):
                print("*",end="")
            #spaces
            for k in range(2*i):
                print(" ",end="")
                
            #stars
            for z in range(n-i+1):
                print("*",end="")    
            print()    

        for z in range(1,n+1):
            for a in range(z):
                print("*",end="")
            #spaces
            for b in range(2*(n-z+1)):
                print(" ",end="")
            #stars
            for c in range(z):
                print("*",end="")    
            print()    



sol = solution()
sol.pattern(4)