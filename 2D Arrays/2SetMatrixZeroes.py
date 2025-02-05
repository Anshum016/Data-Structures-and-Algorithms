def SetZeros(matrix):
    rows=len(matrix)
    cols=len(matrix[0])

    #check if first row has zeros
    firstrow=False
    for j in range(cols):
        if matrix[0][j] == 0:
            firstrow=True
            break
    #check if first col has zeros
    firstcol=False
    for i in range(rows):
        if matrix[i][0] == 0:
            firstcol=True
            break
    #Now marking the rows and columns
    for i in range(1,rows):
        for j in range(1,cols):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    #Now Zero out that row and column
    for i in range(1,rows):
        for j in range(1,cols):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

    #Now Handling First row if it has zeros
    if firstrow:
        for j in range(cols):
            matrix[0][j] = 0

    #Now handling First Col if it has zeros
    if firstcol:
        for i in range(rows):
            matrix[i][0] = 0   
    
    
    return matrix               
                      
                   
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print("Our Answer is",SetZeros(matrix))
