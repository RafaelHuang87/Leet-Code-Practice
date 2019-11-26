class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
# DP
        if m == 1 or n == 1:
            return 1
        path_count = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                path_count[i][j] = path_count[i - 1][j] + path_count[i][j - 1]
        return path_count[-1][-1]