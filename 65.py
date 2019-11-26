class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        isdot, isnum, ise = False, False, False

        for i, value in enumerate(s):
            if value in '+-':
                if i != 0 and s[i - 1] != 'e':
                    return False
            elif value == 'e':
                if ise or not isnum:
                    return False
                ise = True
                isnum = False
            elif value == '.':
                if ise or isdot:
                    return False
                isdot = True
            elif value.isdigit():
                isnum = True
            else:
                return False
        return len(s) > 0 and isnum

s = Solution()
print(s.isNumber('-1.'))
