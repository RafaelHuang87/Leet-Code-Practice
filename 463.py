class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count, m = 0, len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 4
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        count -= 2
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        count -= 2
        return count
