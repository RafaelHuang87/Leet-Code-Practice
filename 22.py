class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        res = []
        def backtrack(temp = '', left = 0, right = 0):
            if len(temp) == 2 * n:
                res.append(temp)
                return
            if left < n:
                backtrack(temp + '(', left + 1, right)
            if right < left:
                backtrack(temp + ')', left, right + 1)

        backtrack()
        return res


s = Solution()
print(s.generateParenthesis(3))