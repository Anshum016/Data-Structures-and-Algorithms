from collections import deque

class solution:
    def orangeRot(self,mat):
        if not mat:
            return 0
        
      
        rows=len(mat)
        cols=len(mat[0])
        queue=deque()
        fresh_count=0
        time=0
            
            # This block of code will add the positions of rotten oranges in a queue and if it is  fresh then we will increase its
        for i in range(rows):
                for j in range(cols):
                    if mat[i][j] == 2:
                        queue.append((i,j,0))
                    elif mat[i][j] == 1:
                        fresh_count += 1
            # IF there ae only fresh oranges in the whole matrix then we will return -1
        if fresh_count == 0:
            return -1
            
            # Defining the positions we need to move 
        directions=[(0,1),(0,-1),(1,0),(-1,0)]# right, left , down , up
        max_time=0

        while queue:
                x,y,time = queue.popleft()
                max_time=max(max_time,time)

                for dx,dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and mat[nx][ny] == 1:
                        mat[nx][ny] = 2
                        fresh_count -=1
                        queue.append((nx,ny,time + 1))

        return max_time if fresh_count == 0 else  -1
    
sol=solution()
mat1 = [[0, 1, 2], [0, 1, 2], [2, 1, 1]]
print(sol.orangeRot(mat1))


