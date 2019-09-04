"""
Solution for Leet Code 832.
"""


class Solution:
    def flipAndInvertImage(A):
        return [[i ^ 1 for i in temp[::-1]]for temp in A]


print(Solution.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
