class item:
    def __init__(self,profit,weight):
        self.profit = profit
        self.weight = weight
def knapsack(w,arr):
    arr.sort(key=lambda x: (x.profit/x.weight) , reverse=True)
    
    final_value=0.0

    for item in arr:
        if item.weight <= w:
            w -= item.weight
            final_value += item.profit
        else:
            final_value += item.profit * w / item.weight
            break
    return final_value

if __name__ == "__main__":
    w = 50
    arr = [item(60,10), item(100,20), item(120,30) ]

    result = knapsack(w,arr)
    print(result)        


