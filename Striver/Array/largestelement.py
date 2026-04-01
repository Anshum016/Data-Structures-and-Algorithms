class solution:
    def largestelement(self,arr):
        largest = arr[0]
        n = len(arr)
        for i in range(n):
            if arr[i] > largest:
                largest = arr[i]

        return largest

arr=[3, 3, 6, 1]
sol = solution()
print(sol.largestelement(arr))            
