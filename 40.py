class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        self.res = []
        if len(candidates) <= 0:
            return self.res
        candidates.sort()
        self.dfs(candidates, [], target, 0)
        return self.res

    def dfs(self, candidates, sublist, target, index):
        if target == 0:
            self.res.append(sublist)
        if target < candidates[0]:
            return
        for i in range(index, len(candidates)):
            if i != index and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates, sublist + [candidates[i]], target - candidates[i], i + 1)

s = Solution()
print(s.combinationSum([2,3,6,7], 7))