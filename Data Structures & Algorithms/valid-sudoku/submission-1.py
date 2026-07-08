class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        box = {}

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                box_key = (r//3, c//3)
                if box_key not in box:
                    box[box_key] = set()

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in box[box_key]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                box[box_key].add(board[r][c])

        return True 