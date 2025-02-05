def findDiagonal(mat):
    rows = len(mat)
    cols = len(mat[0])

    res = []

    curr_row = curr_col = 0
    going_up = True

    while len(res) != rows * cols:
        if going_up:
            while curr_row >= 0 and curr_col < cols:
                res.append(mat[curr_row][curr_col])
                curr_col += 1
                curr_row -= 1

            # Adjust after going out of bounds
            if curr_col == cols:  # Exceeded the right boundary
                curr_col -= 1
                curr_row += 2
            elif curr_row < 0:  # Exceeded the top boundary
                curr_row = 0

            going_up = False

        else:
            while curr_col >= 0 and curr_row < rows:
                res.append(mat[curr_row][curr_col])
                curr_col -= 1
                curr_row += 1

            # Adjust after going out of bounds
            if curr_row == rows:  # Exceeded the bottom boundary
                curr_row -= 1
                curr_col += 2
            elif curr_col < 0:  # Exceeded the left boundary
                curr_col = 0

            going_up = True

    return res

# Example matrix
mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20]
]

print("Our Answer is", findDiagonal(mat))
