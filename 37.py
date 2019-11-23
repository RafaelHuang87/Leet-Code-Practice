class Solution:
    def solveSudoku(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isValidSudoku(temp_board: [[str]]) -> bool:
            row = [[False] * 9 for _ in range(9)]
            column = [[False] * 9 for _ in range(9)]
            matrix = [[False] * 9 for _ in range(9)]
            for i in range(len(temp_board)):
                for j in range(len(temp_board[0])):
                    if board[i][j] != '.':
                        k = i // 3 * 3 + j // 3
                        num = int(temp_board[i][j]) - 1
                        if row[j][num] or column[i][num] or matrix[k][num]:
                            return False
                        row[j][num] = column[i][num] = matrix[k][num] = True
            return True

        def backtrack(temp_board1: [[str]]):
            for i in range(9):
                for j in range(9):
                    if temp_board1[i][j] == '.':
                        for c in "123456789":
                            board[i][j] = c
                            if isValidSudoku(temp_board1):
                                backtrack(temp_board1)
                            else:
                                temp_board1[i][j] = '.'

        backtrack(board)