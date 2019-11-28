class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        subsets = [[]]

        for x in nums:
            newsets = [preset + [x] for preset in subsets]
            subsets.extend(newsets)
        return subsets

s = Solution()
print(s.subsets([1,2,3]))
