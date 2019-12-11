class Solution:
    def combinationSum3(self, k: int, n: int) -> [[int]]:
        res = []

        def dfs(k, n, index, path):
            if k == 0 or n < 0:
                if n == 0:
                    res.append(path)
                return
            for i in range(index, 10):
                dfs(k - 1, n - i, i + 1, path + [i])

        dfs(k, n, 1, [])
        return res