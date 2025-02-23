def celebrity(mat,n):
    stack=[]
    for i in range(n):
        stack.append(i)
    
    while len(stack) > 1:
        a=stack.pop()
        b=stack.pop()

        if mat[a][b] == 1:
        #This means that a knows b(b can be potential celebrity)
          stack.append(b)
        else:
        #This means that b knows a(a can be potential celebrity)    
          stack.append(a)
        
    if not stack:
       return -1
    celeb = stack.pop()

    for i in range(n):
       if i != celeb:
          if mat[celeb][i] == 1 or mat[i][celeb] == 0:
             return -1
    return celeb

mat=[[0, 1, 0], 
       [0, 0, 0], 
       [0, 1, 0]]
n=3
print(celebrity(mat,n))      
                 