class solution:
    def Fibonacci(self,n):
        if n <=1:
            return n
        
        return self.Fibonacci(n-1) + self.Fibonacci(n-2)
    
sol = solution()
print(sol.Fibonacci(6))    
    