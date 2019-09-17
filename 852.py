"""
Solution for Leet Code 852.
"""


class Solution:
    def peakIndexInMountainArray(A):
        for i in range(len(A)):
            if A[i] > A[i + 1]:
                return i


print(Solution.peakIndexInMountainArray([0,2,1,0]))