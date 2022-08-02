# https://leetcode.com/problems/pacific-atlantic-water-flow/
# leetcode 417 medium
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights),len(heights[0])
        pac, atl = set(), set()
        # pacific ocean 
        # r = 0 or c = 0
        # altantic ocean
        # r = rows, or c = cols

        def dfs(r,c,visited,preheight):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or heights[r][c]< preheight:
                return False
            visited.add((r,c))
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr,dc in directions:
                dfs(r+dr,c+dc,visited,heights[r][c])
        
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])
        for r in range(rows):
            dfs(r,cols-1,atl,heights[r][cols-1])
            dfs(r,0,pac,heights[r][0])
            
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
