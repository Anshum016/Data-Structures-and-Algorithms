def solve(arr):
    sorted_arr=sorted(arr)
    n=len(arr)

    #Find mismatch from the front
    front=0
    while front < n and arr[front] == sorted_arr[front]:
        front +=1
    #find mismtach from the back
    back = n-1
    while back >=0 and arr[back] == sorted_arr[back]:
        back -=1
    #If the array is already sorted
    if front >= back:
        return True
    #If mismatch is found
    subarray = arr[front:back + 1]
    if arr[:front] + subarray[::-1] + arr[back + 1:] == sorted_arr:
        return True
    
    return False

arr = [1, 2, 5, 4, 3]
if solve(arr):
    print("Yes")
else:
    print("No")    


           