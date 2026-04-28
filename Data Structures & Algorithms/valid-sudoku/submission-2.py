class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols= defaultdict(set)
        squares = defaultdict(set)

        row_size= len(board)
        col_size= len(board[0])
        
        for i in range(row_size):
            for j in range(col_size):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rows or 
                    board[i][j] in cols or 
                    board[i][j] in squares[(i//3,j//3)]):
                    return False
                rows[i].add(board[i][j])  
                cols[j].add(board[i][j])  
                squares[(i//3,j//3)].add(board[i][j])
        return True        
                
                    
        