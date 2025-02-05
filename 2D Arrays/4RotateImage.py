def RoatateImage(matrix):

    l,r=0,len(matrix)-1

    while l < r:
     for i in range(r - l):
        top, bottom=l,r
          #save the topleft into a variable
        topleft=matrix[top][l + i]
          #move bottomleft to the topmost left
        matrix[top][l + i] = matrix[bottom - i][l]
        # move bottom right to the bottom left
        matrix[bottom - i][l] = matrix[bottom][r - i]
        # move top right to the bottom right
        matrix[bottom][r - i]  = matrix[top + i][r]
        # move top left to the top right
        matrix[top + i][r] = topleft

        l +=1
        r -=1

    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Our Answer is ",RoatateImage(matrix) )      
         

