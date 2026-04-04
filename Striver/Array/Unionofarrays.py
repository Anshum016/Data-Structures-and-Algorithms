class solution:
    def Union(self,arr1,arr2):
    
        s = set()

        for num in arr1:
            s.add(num)

        for num in arr2:
            s.add(num)


        return sorted(s)

arr1 = [1,2,2,3]
arr2 = [2,3,4]
sol = solution()
print(sol.Union(arr1,arr2))