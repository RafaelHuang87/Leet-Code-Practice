class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        if not s:
            return 0
        temp = 0
        start = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack == []:
                    temp = max(temp, i - start)
                    start = i + 1
                else:
                    _ = stack.pop()
                    if stack == []:
                        temp = max(temp, i - start + 1)
                    else:
                        temp = max(temp, i - stack[-1])
        return temp

s = Solution()
print(s.longestValidParentheses("(()()"))
