class solution:
    def PrintName(self,i,n):
        if i == n:
            return    
        
        print("Anshum")
        self.PrintName(i+1,n)

sol = solution()        
sol.PrintName(0,5)