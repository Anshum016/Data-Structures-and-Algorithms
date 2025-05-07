def stock(prices):
    n= len(prices)
    minimum_price=float('inf')
    maximum_profit=0

    for i in range(n-1):
        if prices[i] < minimum_price:
            minimum_price = prices[i]
        elif prices[i] - minimum_price > maximum_profit:
            maximum_profit = prices[i] - maximum_profit

    return maximum_profit

prices = [7, 1, 5, 3, 6, 4]
print(stock(prices))             

