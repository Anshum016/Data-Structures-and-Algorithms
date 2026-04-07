class solution:
    def Sortanarray(self,arr):
        count_0 = arr.count(0)
        count_1 = arr.count(1)
        count_2 = arr.count(2)
        i = 0
        for _ in range(count_0): 
            arr[i] = 0
            i +=1

        for _ in range(count_1): 
            arr[i] = 1
            i +=1    
        
        for _ in range(count_2):
            arr[i] = 2
            i +=1
        return arr
   
arr = [2,0,2,1,1,0]
sol = solution()
print(sol.Sortanarray(arr))
