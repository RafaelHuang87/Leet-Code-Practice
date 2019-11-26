class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if i == j == 0:
                        continue
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

s = Solution()
print(s.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))
