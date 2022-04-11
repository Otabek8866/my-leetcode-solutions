class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def paint(x, y, row, col, oldcol, newcol):
            if (not(0 <= x < row and 0 <= y < col)) or image[x][y] != oldcol:
                return
            image[x][y] = newcol
            paint(x, y-1, row, col, oldcol, newcol)
            paint(x-1, y, row, col, oldcol, newcol)
            paint(x, y+1, row, col, oldcol, newcol)
            paint(x+1, y, row, col, oldcol, newcol)

        if image[sr][sc] != newColor:
            paint(sr, sc, len(image), len(image[0]), image[sr][sc], newColor)

        return image
