class Solution:
    def findMaxLength(self, nums: [int]) -> int:
        loc = {0: 0}
        _max = {0: 0}
        _sum = 0
        for i, num in enumerate(nums):
            _sum = _sum + 1 if num else _sum - 1
            if _sum in loc:
                _max[_sum] = i + 1 - loc[_sum]
            else:
                loc[_sum] = i + 1
        return max(_max.values())

print(Solution().findMaxLength([0,1,0]))