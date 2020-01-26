class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        import collections
        n, d = len(nums), collections.defaultdict(int)
        d[0] = 1
        sum, res = 0, 0
        for i in range(n):
            sum += nums[i]
            if sum - k in d:
                res += d[sum - k]
            d[sum] += 1
        return res