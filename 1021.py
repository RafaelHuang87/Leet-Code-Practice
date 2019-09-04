"""
Solution for Leet Code 1021.
"""


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = []
        state, last = 0, 0
        for i, word in enumerate(S):
            if word is '(':
                state += 1
            if word is ')':
                state -= 1
            if state is 0:
                result.append(S[last + 1: i])
                last = i + 1
        return ''.join(result)


print(Solution.removeOuterParentheses("(()())(())"))
