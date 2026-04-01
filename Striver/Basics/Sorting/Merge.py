class solution:
    def merge_Sort(self,arr):
        if len(arr) <= 1:
          return arr

        mid = len(arr) // 2

        left = self.merge_Sort(arr[:mid])
        right = self.merge_Sort(arr[mid:])

        return self.merge(left,right)
    def merge(self,left,right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i +=1
            else:
                result.append(right[j])
                j +=1
        result.extend(left[i:])
        result.extend(right[j:])

        return result             


arr = [38, 27, 43, 3, 9, 82, 10]
sol = solution()
print(sol.merge_Sort(arr))