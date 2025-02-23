def chocolate(arr,m):
    arr.sort()
    n=len(arr)
    mindiff=float('inf')

    for i in range(n-m+1):
        diff = arr[i+m-1] - arr[i]

        if diff < mindiff:
            mindiff = diff
    return mindiff

arr=[7, 3, 2, 4, 9, 12, 56]
m=5
print(chocolate(arr,m))        