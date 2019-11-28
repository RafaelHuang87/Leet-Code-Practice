class Solution:
    def grayCode(self, n: int) -> [int]:
        if n < 1:
            return [0]
        if n == 1:
            return [0, 1]

        res = self.grayCode(n - 1)

        digit = pow(2, n - 1)
        for i in range(digit - 1, -1, -1):
            res.append(res[i] + digit)
        return res

s = Solution()
print(s.grayCode(2))