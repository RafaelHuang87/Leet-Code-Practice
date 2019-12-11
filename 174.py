class Solution:
    def calculateMinimumHP(self, dungeon: [[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for x in range(m - 1, -1, -1):
            for y in range(n - 1, -1, -1):
                s1 = 0
                s2 = 0
                if x < m - 1:
                    s1 = ans[x + 1][y]
                if y < n - 1:
                    s2 = ans[x][y + 1]
                if s1 == 1 or s2 == 1 or (s1 == 0 and s2 == 0):
                    if dungeon[x][y] >= 0:
                        ans[x][y] = 1
                    else:
                        ans[x][y] = 1 - dungeon[x][y]
                elif s1 == 0:
                    ans[x][y] = max(1, s2 - dungeon[x][y])
                elif s2 == 0:
                    ans[x][y] = max(1, s1 - dungeon[x][y])
                else:
                    ans[x][y] = max(1, min(s1, s2) - dungeon[x][y])

        return ans[0][0]
