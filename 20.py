class Solution:
    def isValid(self, s: str) -> bool:
        left = {'{': '}', '[': ']', '(': ')'}
        stack = []
        for i in s:
            if i in left.keys():
                stack.append(i)
            else:
                if not stack or left[stack.pop()] != i:
                    return False

        return stack == []

s = Solution()
print(s.isValid("()[]{}"))