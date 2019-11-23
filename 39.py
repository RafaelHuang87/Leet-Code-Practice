class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        self.res = []
        if len(candidates) <= 0:
            return self.res
        candidates.sort()
        self.dfs(candidates, [], target, 0)
        return self.res

    def dfs(self, candidates, sublist, target, last):
        if target == 0:
            self.res.append(sublist)
        if target < candidates[0]:
            return
        for num in candidates:
            if num > target:
                return
            if num < last:
                continue
            self.dfs(candidates, sublist + [num], target - num, num)

s = Solution()
print(s.combinationSum([2,3,6,7], 7))