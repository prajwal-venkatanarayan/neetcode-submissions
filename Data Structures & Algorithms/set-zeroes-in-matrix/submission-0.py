class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        row = set()
        col = set()


        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)

        
        for i in range(rows):
            for j in range(cols):
                for r in row:
                    matrix[r][j] = 0
                for c in col:
                    matrix[i][c] = 0   
               