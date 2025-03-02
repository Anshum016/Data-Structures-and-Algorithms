def Minimum(Value):
    deonimations=[1, 2, 5, 10, 20, 50, 100, 500, 1000]
    n = len(deonimations)
    ans=[]
    i = n-1
    while(i >= 0):

        while ( Value >= deonimations[i]):
            Value -= deonimations[i]
            ans.append(deonimations[i])
        i -=1

    for i in range(len(ans)):
        print(ans[i] , end= " ")


if __name__ == "__main__":
    Value=121
    print(Minimum(Value))