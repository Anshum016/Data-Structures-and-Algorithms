def calculate(A,B,K):

    A.sort()

    B.sort(reverse=True)

    for i in range(len(A)):
        if A[i] + B[i] < K:
            return False

    return True

A= [2, 1, 3] 
B = [ 7, 8, 9 ]
K = 10.            

print("Our Answer is",calculate(A,B,K))