def solve(arr):
    element_count={}
    duplicates=set()

    for num in arr:
        if num in element_count:
            element_count[num] +=1
        else:
            element_count[num] = 1

        if element_count[num] >=2:
            duplicates.add(num)

    return list(duplicates)

arr = [1, 2, 3, 6, 3, 6, 1]
print("Our Answer is",solve(arr))            
          
        