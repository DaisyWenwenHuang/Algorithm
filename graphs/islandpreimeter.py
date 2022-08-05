# https://leetcode.com/problems/island-perimeter/
# leetcode  463 easy
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visit = set()
        
        
        def dfs(r,c):
            if (r not in range(rows)) or (c not in range(cols))\
            or grid[r][c] == 0:
                return 1
            if (r,c) in visit:
                return 0
            visit.add((r,c))
            if grid[r][c] == 1:
                perimeter = dfs(r,c+1)
                perimeter += dfs(r,c-1)
                perimeter += dfs(r+1,c)
                perimeter += dfs(r-1,c)
            return perimeter
            
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return dfs(row,col)