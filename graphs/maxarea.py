# https://leetcode.com/problems/max-area-of-island/
# leetcode 695 medium

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visited = set()
        maxarea = 0
        
        
        def dfs(r,c):
            if r  not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r,c) in visited :
                return 0
            
            visited.add((r,c))
            return (1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))
        
        for r in range(rows):
            for c in range(cols):
                maxarea = max(maxarea,dfs(r,c))
        return maxarea
                