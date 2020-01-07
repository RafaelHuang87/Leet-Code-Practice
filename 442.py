class Solution:
    def findDuplicates(self, nums: [int]) -> [int]:
        import collections
        temp = collections.Counter(nums)
        res = []
        for item, val in temp.items():
            if val > 1:
                res.append(item)
        return res


s = Solution()
print(s.findDuplicates([4,3,2,7,8,2,3,1]))