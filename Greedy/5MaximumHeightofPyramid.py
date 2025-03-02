def Maximum(arr):
    n = len(arr)
    left=0
    right=n
    max_height=0

    while left <= right:
        mid =  (left + right) // 2
        required_objects = (mid * (mid+1)) // 2  

        if required_objects <= len(arr):
            max_height = mid
            left = mid + 1
        else:
            right = mid - 1   

    return max_height

arr=[10, 20, 30, 50, 60, 70]
print(Maximum(arr))         