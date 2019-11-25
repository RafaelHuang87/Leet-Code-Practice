class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = []

        def dfs(nums, row):
            if row == n:
                ans.append(nums[:])
                return
            for col in range(n):
                nums[row] = col
                if vaild(nums, row):
                    dfs(nums, row + 1)

        def vaild(nums, row):
            for i in range(row):
                if nums[i] == nums[row] or abs(nums[row] - nums[i]) == abs(row - i):
                    return False
            return True

        dfs([None for _ in range(n)], 0)

        results = [[] for _ in range(len(ans))]
        for i in range(len(ans)):
            for col in ans[i]:
                tmp = "." * n
                results[i].append(tmp[:col] + 'Q' + tmp[col + 1:])
        return len(results)
