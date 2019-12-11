class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c)
                    res += 1
        return res

    def dfs(self, grid, i, j):
        dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        grid[i][j] = "0"
        for dir in dirs:
            nr, nc = i + dir[0], j + dir[1]
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                if grid[nr][nc] == "1":
                    self.dfs(grid, nr, nc)