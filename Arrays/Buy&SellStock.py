def best_time(prices):
    min_price=float('inf')
    max_profit=0
    for i in range(len(prices)):
        if(prices[i]<min_price):
            min_price=prices[i]
        elif(prices[i]-min_price>max_profit):
            max_profit=prices[i]-min_price
    return max_profit

prices = [7,1,5,3,6,4]

print("The maximum profit is" ,best_time(prices))