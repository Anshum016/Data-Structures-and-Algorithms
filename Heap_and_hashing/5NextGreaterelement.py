def NextGreater(arr):
    n = len(arr)
    result = []
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                result.append(arr[j])
                break
        else:
            result.append(-1)
            
    return result

arr = [1, 3, 2, 4]
print(NextGreater(arr))
