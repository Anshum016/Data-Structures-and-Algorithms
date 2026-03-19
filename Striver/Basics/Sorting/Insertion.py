class Solution:
    def insertion_sort(self, arr):
        n = len(arr)

        for i in range(1, n):          # start from index 1 (first element is trivially sorted)
            key = arr[i]               # the element we're trying to place
            j = i - 1                  # look at the sorted portion to the left

            while j >= 0 and arr[j] > key:  # shift larger elements one step right
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key           # insert key into its correct position

        return arr

sol = Solution()
arr = [13, 46, 24, 52, 20, 9]
print(sol.insertion_sort(arr))  # [9, 13, 20, 24, 46, 52]