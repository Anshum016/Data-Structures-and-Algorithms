def solve(arr):
    frequency={}

    for num in arr:
        frequency[num] = frequency.get(num,0) + 1

        if frequency[num] > len(arr) // 2:
            return num


    return -1

arr = [1, 1, 2, 1, 3, 5, 1]
print("Our answer is",solve(arr))    