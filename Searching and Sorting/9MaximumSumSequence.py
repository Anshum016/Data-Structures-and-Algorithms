def MaximumSumSequence(arr):
    n=len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0] 

    #initializing array
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0],arr[1])

    for i in range(2,n):
        dp[i] = max(dp[i-1],arr[i] + dp[i-2])

    return dp[-1]
arr = [5,5,10,100,10,5]
print("Our Answer is",MaximumSumSequence(arr))             
