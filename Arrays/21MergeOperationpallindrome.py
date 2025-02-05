def MergeOperations(nums):
    i=0
    j=len(nums)-1
    mergecount=0

    while i<j:
        if nums[i] == nums[j]:
            i +=1
            j -=1
        elif nums[i] < nums[j]:
            nums[i+1] += nums[i]
            i +=1
            mergecount +=1
        else:
            nums[j-1] += nums[j]
            j -=1
            mergecount +=1
    return  mergecount           
nums=[11, 14, 15, 99]
print("Our answer is",MergeOperations(nums))            
     
