def FloodFill(img,sr,sc,color):
    original_color=img[sr][sc]
    if original_color == color:
        return img

    def dfs(r,c):
        if  r < 0 or r >= len(img) or c < 0 or c >= len(img[0]):
            return
        if img[r][c] != original_color:
            return

        img[r][c] = color

        dfs(r+1,c)
        dfs(r,c+1)
        dfs(r-1,c)
        dfs(r,c-1)
    dfs(sr,sc)
    return img

img = [[1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]]

sr = 1
sc = 1
color = 2

result = FloodFill(img, sr, sc, color)
print(result)

