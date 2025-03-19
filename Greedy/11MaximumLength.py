def Maximum(pairs):
    pairs.sort()
    n = len(pairs)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if pairs[j][1] < pairs[i][0]:
                dp[i] = max(dp[i],dp[j] + 1) 
    return max(dp)

pairs=[(5, 24), (39, 60), (15, 28), (27, 40), (50, 90)]
result=Maximum(pairs)
print(result)            