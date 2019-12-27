class Solution:
    def kthSmallest(self, matrix: [[int]], k: int) -> int:
        initial = []
        for row in matrix:
            initial += row
        return sorted(initial)[k - 1]

s = Solution()
print(s.kthSmallest([
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
], k = 8))