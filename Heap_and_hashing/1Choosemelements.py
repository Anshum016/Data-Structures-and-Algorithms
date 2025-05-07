def choose_m_elements(arr,m):
    arr.sort()
    n = len(arr)
    minimum_difference=float('inf')

    for i in range(n-m+1):
        current_difference = arr[i + m - 1] - arr[i]
        minimum_difference = min(minimum_difference,current_difference)
    return minimum_difference

arr = [7, 3, 2, 4, 9, 12, 56]
m = 3

print(choose_m_elements(arr,m))    
