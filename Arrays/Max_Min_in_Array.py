def set_min(A):
    mini = float('inf')
    for num in A:
        if num < mini:
            mini = num
    return mini        

def set_max(A):
    maxi = float('-inf')
    for num in A:
        if num > maxi:
            maxi = num
    return maxi

A=[1,2,3,4,5,6,7]
print("Minimum number is", set_min(A))
print("Maximum number is", set_max(A))