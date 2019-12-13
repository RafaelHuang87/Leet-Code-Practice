class Solution:
    def summaryRanges(self, nums: [int]) -> [str]:
        if not nums:
            return []
        l, end, start = [], 0, 0
        while end < len(nums) - 1:
            if nums[end] + 1 != nums[end + 1]:
                l.append((nums[start], nums[end]))
                start = end + 1
            end += 1
        l.append((nums[start], nums[-1]))
        q = []
        for c in l:
            if c[0] != c[1]:
                q.append(str(c[0]) + '->' + str(c[-1]))
            else:
                q.append(str(c[0]))

        return q
