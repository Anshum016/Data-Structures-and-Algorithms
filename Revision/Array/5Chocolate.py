def chcoloate(arr,m):
    arr.sort()
    result_array=[]
    for i in range (m):
       result_array.append(arr[i])
    output= result_array[m - 1] - result_array[0] 

    return output

arr=  [7, 3, 2, 4, 9, 12, 56]
m = 5
print(chcoloate(arr,m))

    
       