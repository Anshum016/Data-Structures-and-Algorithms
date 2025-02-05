def findcommon(matrix):
    #Assuming the first row 
    first_row=matrix[0]

    #Assuming the first element to be common
    for element in first_row:
        is_common = True
        

    #Checking the other row
        for row in matrix[1:]:
         if element not in row:
            is_common=False
            break

         if is_common:
          return element
    
    return -1

matrix = [
    [1, 2, 3, 4],
    [2, 4, 5, 6],
    [2, 4, 7, 8]
]
print("Our Answer",findcommon(matrix))        


