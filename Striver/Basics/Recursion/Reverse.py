class solution:
    def Reverse(self,arr,i,n):
        if i >=n/2:
            return
        arr[i],arr[n-i-1] = arr[n-i-1],arr[i]

        self.Reverse(arr,i+1,n)

sol = solution()
arr = [1, 2, 3, 4, 5, 6]
sol.Reverse(arr,0,len(arr))
print(arr)
