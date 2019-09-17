"""
Solution for Leet Code 977.
"""


class Solution:
    def sortedSquares(A):
        return sorted(x*x for x in A)


print(Solution.sortedSquares([-4,-1,0,3,10]))