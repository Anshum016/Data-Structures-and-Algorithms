def build_prefix(arr):
    prefix = [0] * len(arr)

    prefix[0] = arr[0]

    for i in range(1,len(arr)):
        prefix[i] = prefix[i-1] + arr[i]

    return prefix    

def range_sum(arr,left,right):
    prefix = build_prefix(arr)

    if left == 0:
        return prefix[right]

    return prefix[right] - prefix[left - 1]


arr = [2, 4, 6, 8, 10]

prefix = build_prefix(arr)

print(range_sum(arr,3,5))




    