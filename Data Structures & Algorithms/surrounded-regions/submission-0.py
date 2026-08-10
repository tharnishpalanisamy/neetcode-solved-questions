class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board) 
        COLS = len(board[0]) 
        safe = set() 
        def dfs(r,c) :
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in safe or board[r][c] =='X':
                return  
            safe.add((r,c)) 
            dfs(r-1,c) 
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for r in range(ROWS) :
            for c in range(COLS) : 
                if ( r == 0 or c == 0 or r == ROWS - 1 or c == COLS -1 ) and board[r][c] == 'O': 
                    dfs(r,c) 
        for r in range(ROWS) :
            for c in range(COLS) :
                if board[r][c] == 'O' and (r,c) not in safe :
                    board[r][c] = 'X' 
        