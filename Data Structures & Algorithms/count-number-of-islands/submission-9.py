class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
       
       # top,right,down,left
       # directions =[[0,1],[1,0],[0,-1],[-1,0]]
        visited = set()
        islands = 0

        def dfs(r,c):
            #check boundaries and skip water
            if r not in range(rows) or c not in range(cols) or grid[r][c] == "0" :
                return
            
            # Mark as visited immediately
            grid[r][c] = "0"

            #for dr,dc in directions:
            #    dfs(r+dr,c+dc)

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited :
                    dfs(r,c)
                    islands = islands+1  
        
        return islands