def Maximum_product_subarray(A):
    prev_max=A[0]
    prev_min=A[0]
    curr_min =A[0]
    curr_max = A[0]
    Result=0

    for i in range(1,len(A)):
        curr_max=max(prev_max*A[i],prev_min*A[i],A[i])
        curr_min=min(prev_max*A[i],prev_min*A[i],A[i])
        prev_max=curr_max
        prev_min=curr_min
        Result=max(prev_max,Result)

    return Result

A=[2,3,-2,4]
print("Maximum subarray is ",Maximum_product_subarray(A))    