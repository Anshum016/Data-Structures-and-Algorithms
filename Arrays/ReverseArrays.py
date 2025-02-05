def reverse_arrays(A,start,end):
    while start<end:
        A[start] , A[end] = A[end] , A[start]
        start += 1 
        end -= 1
    return A    
A=[1,2,3,4,5,6]

print("The reversed array is " ,reverse_arrays(A,0,len(A) - 1))