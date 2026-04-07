class solution:
    def Twosum(self,arr,target):
        arr.sort()
        n = len(arr)
        low = 0
        high = n - 1

        while low < high:
            s = arr[low] + arr[high]

            if s == target:
                return low,high
            elif s > target:
                high -=1
            else:
                low +=1
        return -1            

arr = [2,6,5,8,11]
target = 14
sol = solution()
print(sol.Twosum(arr,target))



