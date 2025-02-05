def find_min(A,N,M):
    A.sort()
    i=0
    j=M-1
    d=float('inf')

    while j<N:
       d=min(d,A[j]-A[i])
       i +=1
       j +=1

    return d 

A=[3,4,1,9,56,7,9,12]    
N = 8
M = 5

print("Our Answer is " ,find_min(A,N,M))