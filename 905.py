"""
Solution for Leet Code 905.
"""


class Solution:
    def sortArrayByParity(A):
        return sorted(A, key = lambda x : x % 2)


print(Solution.sortArrayByParity([2,3,5,4,1]))