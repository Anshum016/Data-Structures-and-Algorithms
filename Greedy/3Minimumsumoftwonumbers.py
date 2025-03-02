def Minimum(arr):
    arr.sort()
    first_num=[]
    second_num=[]
    n= len(arr)
    for i in range(n):
        if i % 2 == 0:
            first_num.append(arr[i])
        else:
            second_num.append(arr[i])

    first_number=int("".join(map(str,first_num)))
    second_number=int("".join(map(str,second_num)))
    
    print(first_number,second_number)
    return first_number + second_number       

arr=[6, 8, 4, 5, 2, 3]
print(Minimum(arr))     