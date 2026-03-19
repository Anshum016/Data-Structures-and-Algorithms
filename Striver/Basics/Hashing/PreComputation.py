class Solution:
    def frequency(self, arr):
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        return freq


arr = [1,2,3,4,5,1,2,3]

sol = Solution()
result = sol.frequency(arr)

print(result)
