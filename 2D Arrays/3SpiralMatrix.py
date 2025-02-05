def SpiralMatrix(matrix):
    res = []
    left= 0 
    right = len(matrix[0])
    top = 0
    bottom = len(matrix)

    while left < right and top < bottom:
        # get every i on first row
        for i in range(left, right):
            res.append(matrix[top][i])
        top +=1

        # get every i on the right col
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -=1

        if not (left < right and top < bottom):
            break

        #get every i on the bottom rows
        for i in range(right - 1, left - 1 , -1):
            res.append(matrix[bottom - 1][i]) 
        bottom -=1

        # get every i on the left col
        for i in range(bottom - 1,top - 1, -1):
            res.append(matrix[i][left])
        left +=1               

    return res     

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Our Answer is ",SpiralMatrix(matrix))