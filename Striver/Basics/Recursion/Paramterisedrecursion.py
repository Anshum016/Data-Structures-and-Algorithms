class solution:
    def function(self,i,sum):
        if i < 1:
            print(sum)
            return
        self.function(i-1,sum+i)

sol = solution()
sol.function(3,3)