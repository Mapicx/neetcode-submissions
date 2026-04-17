class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        COLS = collections.defaultdict(set)
        ROWS = collections.defaultdict(set)
        Squares = collections.defaultdict(set) # key = (r//3, c//3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if (
                    board[r][c] in COLS[c] or
                    board[r][c] in ROWS[r] or
                    board[r][c] in Squares[(r//3, c//3)]
                    ):
                    return False
                
                ROWS[r].add(board[r][c])
                COLS[c].add(board[r][c])
                Squares[(r//3, c//3)].add(board[r][c])
        return True

        