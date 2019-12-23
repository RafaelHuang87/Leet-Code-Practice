class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        import collections
        if not s:
            return s
        s = s.lower()
        dic = collections.Counter(s)
        stack = [s[0]]
        dic[s[0]] -= 1
        for i in range(1, len(s)):
            dic[s[i]] -= 1
            while stack and s[i] < stack[-1] and s[i] not in stack:
                if dic[stack[-1]] > 0:
                    stack.pop()
                else:
                    break
            if s[i] not in stack:
                stack.append(s[i])

        return ''.join(stack)