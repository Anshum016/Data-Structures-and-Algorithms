def search(board,word):
    ROWS , COLS = len(board) , len(board[0])
    path=set()
    def dfs(r,c,i):
      if (i==len(word)):
         return True
      if (r < 0 or c < 0 or
          r >= ROWS or COLS >= c or
          word[i] != board[r][c] or
          (r,c) in path):
         return False
      
      path.add((r,c))
      res=(dfs(r+1,c,i+1)or
           dfs(r-1,c,i+1)or
           dfs(r,c+1,i+1)or
           dfs(r,c-1,i+1)
           )
      path.remove((r,c))
      return res

    for r in range(ROWS):
         for c in range(COLS):
            if(r,c,0): return True
               
    return False
            
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCED"
print("Our Answer is",search(board,word)) 

          