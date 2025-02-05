def solve(arr,n):
    elements=set(arr)
    for num in arr:
        if num + n in elements or num - n in elements:
            return num,num + n if(num + n) in elements else num - n
        
arr = [5, 20, 3, 2, 50, 80]
n = 78
print("Our Answer is",solve(arr,n))        