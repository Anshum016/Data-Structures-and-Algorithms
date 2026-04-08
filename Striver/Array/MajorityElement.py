class solution:
    def MajorityElement(self,arr):
        n = len(arr)
        hash_map={}

        for num in arr:
            hash_map[num] = hash_map.get(num,0) + 1

            if hash_map[num] > n // 2:
                return num

arr = [7, 0, 0, 1, 7, 7, 2, 7, 7]
sol = solution()
print(sol.MajorityElement(arr))