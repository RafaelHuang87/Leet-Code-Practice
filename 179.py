class Solution:
    def largestNumber(self, nums: [int]) -> str:
        if max(nums) == 0:
            return '0'
        nums = list(map(str, nums))
        from functools import cmp_to_key
        cmp = lambda a, b: 1 if (a + b) > (b + a) else -1 if (a + b) < (b + a) else 0
        nums.sort(key=cmp_to_key(cmp), reverse=True)
        res = ''.join(nums)
        return res

s = Solution()
print(s.largestNumber([3,30,34,5,9]))