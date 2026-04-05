class solution:
    def Intersection(self,arr1,arr2):
        i = 0
        j = 0
        ans=[]
        
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                i +=1

            elif arr1[i] > arr2[2]:
                j +=1

            else:
                if not ans or ans[-1] != arr1[i]:
                    ans.append(arr1[i])
                i +=1
                j +=1
        return ans


arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 3, 5]

sol = solution()
print(sol.Intersection(arr1,arr2))

