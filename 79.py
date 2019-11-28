class Solution:
    def exist(self, board: [[str]], word: str) -> bool:

        def find(board, word, i, j, m, n):
            if word == '':
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            elif word[0] == board[i][j]:
                board[i][j] = None
                res = find(board, word[1:], i + 1, j, m, n) or find(board, word[1:], i - 1, j, m, n) or find(board,word[1:],i, j + 1,m,n) or find(board, word[1:], i, j - 1, m, n)
                board[i][j] = word[0]

                return res

        if len(word) == 0:
            return True

        m = len(board)
        if m == 0:
            return False
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if find(board, word, i, j, m, n):
                    return True
        else:
            return False
