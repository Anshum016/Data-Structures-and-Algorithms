class solution:
    def sorted(self,arr):
        n = len(arr)

        for i in range(n-1):
            if arr[i] > arr[i+1]:
                return False
            

        return True

arr = [1,2,4,3,5]        
sol = solution()
print(sol.sorted(arr))