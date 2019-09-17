"""
Solution for Leet Code 561.
"""

class Solution:
    def arrayPairSum(nums):
        return sum(sorted(nums, reverse=True)[1::2])

print(Solution.arrayPairSum([1,4,3,2]))

