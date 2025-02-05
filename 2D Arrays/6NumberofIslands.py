def islands(matrix):
    # Check if matrix is empty
    if not matrix:
        return 0

    # Helper function to perform DFS
    def dfs(r, c):
        # Base case: If out of bounds or the cell is water ('0'), return
        if (r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]) or matrix[r][c] == 0):
            return
        
        # Mark the current cell as visited by turning it to water ('0')
        matrix[r][c] = 0
        
        # Explore all 4 directions (up, down, left, right)
        dfs(r - 1, c)  # Up
        dfs(r + 1, c)  # Down
        dfs(r, c - 1)  # Left
        dfs(r, c + 1)  # Right

    islands = 0  # Initialize the island count

    # Traverse the matrix
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            # If we find unvisited land ('1'), we count it as an island
            if matrix[r][c] == 1:
                islands += 1  # Increment island count
                dfs(r, c)  # Mark all cells in this island as visited

    return islands  # Return the final island count

# Example input
matrix = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0]
]

# Call the function and print the result
print(islands(matrix))  # Expected output: 4
