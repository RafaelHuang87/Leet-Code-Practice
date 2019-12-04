class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r = len(board)
        if not r:
            return
        c = len(board[0])

        def bfs(board, i, j):
            if 0 <= i < r and 0 <= j < c and board[i][j] == 'O':
                board[i][j] = 'T'
                bfs(board, i, j + 1)
                bfs(board, i, j - 1)
                bfs(board, i + 1, j)
                bfs(board, i - 1, j)

        for i in range(r):
            for j in range(c):
                if (i == 0 or i == r - 1 or j == 0 or j == c - 1) and board[i][j] == 'O':
                    bfs(board, i, j)

        for i in range(r):
            for j in range(c):
                board[i][j] = 'O' if board[i][j] == 'T' else 'X'