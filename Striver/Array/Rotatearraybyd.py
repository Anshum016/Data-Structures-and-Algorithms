class solution:
    def rotate(self,arr,r):
        n = len(arr)
        r = r % n
        arr.reverse()

        arr[:r] = arr[:r][::-1]
        arr[r:] = arr[r:][::-1]


        return arr
    
sol = solution()
arr = [1, 2, 3, 4, 5, 6, 7]
r = 2
print(sol.rotate(arr,r))     
