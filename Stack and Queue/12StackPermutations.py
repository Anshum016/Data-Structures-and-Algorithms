def matchpermutation(arr1,arr2):
    stack=[]
    j=0

    for i in arr1:
        stack.append(i)

        while stack and stack[-1] == arr2[j]:
            stack.pop()
            j +=1


    return len(stack) == 0


arr1 = [1, 2, 3, 4]  
arr2 = [3, 1, 2, 4]

if matchpermutation(arr1,arr2):
    print("Possible")
else:
    print("Not Possible")    

