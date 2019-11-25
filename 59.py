class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        res = [[0] * n for i in range(n)]
        up = 0
        down = n - 1
        left = 0
        right = n - 1
        val = 1
        while True:
            for j in range(left, right + 1):
                res[up][j] = val
                val += 1
            up += 1
            if up > down:
                break
            for i in range(up, down + 1):
                res[i][right] = val
                val += 1
            right -= 1
            if right < left:
                break
            for j in range(left, right + 1):
                res[down][n - 2 - j] = val
                val += 1
            down -= 1
            if down < up:
                break
            for i in range(up, down + 1):
                res[n - 1 - i][left] = val
                val += 1
            left += 1
            if left > right:
                break
        return res