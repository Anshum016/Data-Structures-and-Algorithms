class solution:
    def secondlargest(self,arr):
        n = len(arr)
        largest = float('-inf')
        slargest = float('-inf')

        for num in arr:
            if num > largest:
                slargest = largest
                largest = num
            elif num < largest and num > slargest:
                slargest = num
        return slargest       
    def secondsmallest(self,arr):
        n = len(arr)
        smallest = float('inf')
        ssmalest = float('inf')

        for num in arr:
            if num < smallest:
                ssmalest = smallest
                smallest = num
            elif num > smallest and num < ssmalest:
                ssmalest = num
        return ssmalest         
              

arr = [1, 2, 4, 7, 7, 5] 
sol = solution()
print(sol.secondlargest(arr))        
print(sol.secondsmallest(arr))