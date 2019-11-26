class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = [[0] * n for _ in range(m)]
        result[0][0] = grid[0][0]
        for i in range(1, m):
            result[i][0] = result[i - 1][0] + grid[i][0]

        for j in range(1, n):
            result[0][j] = result[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                result[i][j] = min(result[i - 1][j], result[i][j - 1]) + grid[i][j]

        return result[-1][-1]

s = Solution()
print(s.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))