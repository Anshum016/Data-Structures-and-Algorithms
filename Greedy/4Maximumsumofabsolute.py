def MaximumDifference(a,b):
    a.sort()
    b.sort()
    n = len(a)
    sum=0
    for i in range(n):
       sum += abs(a[i] - b[i])
    return sum

a = [4, 1, 8, 7]
b = [2, 3, 6, 5]

print(MaximumDifference(a,b))