class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if heightMap == []:
            return 0
        m = len(heightMap)
        n = len(heightMap[0])
        peakMap = [[float("inf")] * n for __ in range(m)]

        stack = []
        for i in range(m):
            for j in range(n):
                if i in (0, m - 1) or j in (0, n - 1):
                    peakMap[i][j] = heightMap[i][j]
                    stack.append((i, j))
        while stack:
            i, j = stack.pop(0)
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in dirs:
                nx, ny = i + dx, j + dy
                if nx < 0 or nx > m - 1 or ny < 0 or ny > n - 1:
                    continue
                limit = max(peakMap[i][j], heightMap[nx][ny])
                if peakMap[nx][ny] > limit:
                    peakMap[nx][ny] = limit
                    stack.append((nx, ny))
        return sum([peakMap[i][j] - heightMap[i][j] for i in range(m) for j in range(n)])
