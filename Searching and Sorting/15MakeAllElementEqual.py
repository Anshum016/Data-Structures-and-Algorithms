def makeequal(arr):
    arr.sort()
    n=len(arr)

    #finding median
    median=arr[n//2]
    total_cost=0

    for num in arr:
        total_cost += abs(num - median)
        return total_cost
    
arr = [1, 1700, 101]
print("Our Answer is",makeequal(arr) )    

