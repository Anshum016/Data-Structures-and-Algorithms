def nextgreater(arr):
    n=len(arr)
    result= [-1]* n
    stack=[]

    for i in range(n-1,-1,-1):#Traversing from right to left
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])      
    return result

arr = [1, 3, 2, 4]
print(nextgreater(arr))     



def next_greater(arr):
    n=len(arr)
    result=[-1] * n
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] < arr[j]:
               result[i] = arr[j]
               break
    return result

arr = [1, 3, 2, 4]
print(next_greater(arr))         
