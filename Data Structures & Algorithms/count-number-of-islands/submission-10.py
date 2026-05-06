class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        visited=set()

        def dfs(r,c):
            #check th boundaries
            if r not in range(rows) or c not in range(cols) or grid[r][c]== "0" or (r,c) in visited:
                return
            
            #mark as visited
            visited.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        islands=0
        for i in range(rows):
            for j in range(cols):
                # 2. Added check to ensure we only start DFS on unvisited land
                if grid[i][j]=="1" and (i, j) not in visited:
                    dfs(i,j)
                    islands=islands+1

        print(islands)
        return islands            
