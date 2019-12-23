class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        import operator
        if len(matrix) == 0:
            return 0
        dp = [[1] * len(matrix[0]) for _ in range(len(matrix))]

        slist = sorted([(i, j, val)
                        for i, row in enumerate(matrix)
                        for j, val in enumerate(row)], key=operator.itemgetter(2))

        for x, y, val in slist:
            for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] > matrix[x][y]:
                    dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)

        return max(max(x) for x in dp)