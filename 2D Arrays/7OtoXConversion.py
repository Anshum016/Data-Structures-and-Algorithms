def floodfill(matrix,r,c,oldvalue,newvalue):
    rows=len(matrix)
    cols=len(matrix[0])

    
    if (r < 0 or c < 0 or
        r>=rows or c >=cols or
        matrix[r][c] != oldvalue):

        return
         
    matrix[r][c] = newvalue

    floodfill(matrix,r-1,c,oldvalue,newvalue)
    floodfill(matrix,r+1,c,oldvalue,newvalue)
    floodfill(matrix,r,c-1,oldvalue,newvalue)
    floodfill(matrix,r,c+1,oldvalue,newvalue)

    

def solveit(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    #Marking left and right border connected from  O to T
    for r in range(rows):
        if matrix[r][0] == "O": #left border
            floodfill(matrix,r,0,'O','T')
        if matrix[r][cols-1] == 'O':
            floodfill(matrix,r,cols-1,'O','T')

    #Now marking top and bottom borders connected from O to T 
    for c in range(cols):
        if matrix[0][c] == 'O':
          floodfill(matrix,0,c,'O','T')
        if matrix[rows-1][c] == 'O':
          floodfill(matrix,rows-1,c,'O','T')

    #Now converting all other O to X
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'O':
               matrix[r][c] = 'X' 

    #Replacing the border T with o
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'T':
               matrix[r][c] = 'O'


    return matrix           

matrix= [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'O']
]
print("Our Answer is",solveit(matrix))                
                            

