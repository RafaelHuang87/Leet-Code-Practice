class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        if matrix == []:
            return []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        res = []

        while top < bottom and left < right:

            res += matrix[top][left:right + 1]

            for x in range(top + 1, bottom):
                res.append(matrix[x][right])

            res += matrix[bottom][left:right + 1][::-1]

            for x in range(bottom - 1, top, -1):
                res.append(matrix[x][left])

            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1

        if top == bottom:
            res += matrix[top][left:right + 1]
        elif left == right:
            for x in range(top, bottom + 1):
                res.append(matrix[x][right])

        return res