class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if s == '':
            return []
        res = []
        if s == s[::-1]:
            res.append([s])
        for i in range(len(s)):
            if s[:i + 1] == s[i::-1]:
                p = self.partition(s[i + 1:])
                for c in p:
                    if c != []:
                        res.append([s[:i + 1]] + c)

        return res
