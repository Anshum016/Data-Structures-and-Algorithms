import math
def Minimum(coin,n,k):
    coin.sort()
    ans = 0
    coin_needed = math.ceil(1 * n // (k+1))

    for i in range(coin_needed):
      ans += coin[i]
    return ans

coin=[8, 5, 3, 10,  
        2, 1, 15, 25]
n = len(coin)
k= 3
print(Minimum(coin,n,k))

