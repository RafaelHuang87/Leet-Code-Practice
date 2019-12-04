class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        m = 0
        for i in nums:
            if i - 1 not in nums:
                t = i + 1
                while t in nums:
                    t = t + 1
                m = max(m, t - i)
        return m

s = Solution()
print(s.longestConsecutive([100, 101, 102, 103, 104, 200, 1, 3, 2]))
