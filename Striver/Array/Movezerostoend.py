class solution:
    def movezeros(self,arr):
        n = len(arr)
        j = 0

        #Step 1 first j and i 
        for i in range(n):
            if arr[i] == 0:
                j = i
                break

        #Iterate from j to find non-zero numbers
        for i in range(j+1,n):
            if arr[i] != 0:
                arr[i],arr[j] = arr[j],arr[i]
                j +=1

        return arr

arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
sol = solution()
print(sol.movezeros(arr))            


