def contribute(arr,sum):

    ans = 0
    n = len(arr)
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if(arr[i] + arr[j] + arr[k] < sum):
                    ans +=1

    return ans

arr = [5, 1, 3, 4, 7] 
sum = 12
print("Our Answer",contribute(arr,sum))                