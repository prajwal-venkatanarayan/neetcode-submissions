class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
       
       # top,right,down,left
        directions =[[0,1],[1,0],[0,-1],[-1,0]]
        islands = 0

        def bfs(r,c):
            q=deque()
            q.append((r,c))

            grid[r][c] = "0" # Mark as visited immediately

            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    r,c = row+dr, col+dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1":
                        q.append((r,c))
                        grid[r][c] = "0"
                             

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands = islands+1

        return islands            