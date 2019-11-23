class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        row = [[False]*9 for _ in range(9)]
        column = [[False]*9 for _ in range(9)]
        matrix = [[False]*9 for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    k = i//3*3 + j//3
                    num = int(board[i][j]) - 1
                    if row[j][num] or column[i][num] or matrix[k][num]:
                        return False
                    row[j][num] = column[i][num] = matrix[k][num] = True
        return True

s = Solution()
print(s.isValidSudoku(
 [["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]]))