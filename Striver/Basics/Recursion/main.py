class solution(object):
    def function(self,count):
        count +=1
        print(f"Current count {count}")
        if count == 4:
            return True
        return self.function(count)
    
sol = solution()
sol.function(0)    
        
