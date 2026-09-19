class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        m = len(board)
        n = len(board[0])

        for i in range(m):
            seen = set()
            for j in range(n):
                node = board[i][j]
                if node in seen:
                    return False
                if node != '.':
                    seen.add(node)
        
        for i in range(m):
            seen = set()
            for j in range(n):
                node = board[j][i]
                if node in seen:
                    return False
                if node != '.':
                    seen.add(node)
        
        starts = [
            (0,0), (0,3), (0,6),
            (3,0), (3,3), (3,6),
            (6,0), (6,3), (6,6)
        ]

        for i, j in starts:
            seen = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    node = board[row][col]
                    if node in seen:
                        return False
                    if node != '.':
                        seen.add(node)
        
        return True
