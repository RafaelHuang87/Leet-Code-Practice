class Solution:
    def minimumTotal(self, triangle: [[int]]) -> int:
        res = triangle[-1]

        i = len(triangle) - 2

        while i >= 0:
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
            i -= 1
        return res[0]

s = Solution()
print(s.minimumTotal([[-1], [2, 3], [1, -1, -3]]))