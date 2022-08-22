# https://leetcode.com/problems/rotting-oranges/
# leetcode 994 medium
# bfs
# review
# do multiple bfs at the same time as there could be multiple rotten organes that affects fresh oragnes at the same time 
        rows = len(grid)
        cols = len(grid[0])
        Q = deque()
        time, fresh = 0, 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    Q.append([row,col])
                
        while Q and fresh > 0:
            
            for i in range(len(Q)):
                r,c = Q.popleft()
                for dr,dc in directions:
                    row = r + dr
                    col = c + dc
                    
                    if (row not in range(rows)) or (col not in range(cols)) or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    Q.append([row,col])
                    fresh -= 1
            time += 1
        
        if fresh == 0:
            return time
        else:
            return -1