import re
class Solution:
    def lengthCheck(self, s:str) -> List[int]:
        l = []
        curr = 1
        for i in range(1, len(s)):
            if s[i] is s[i - 1]:
                curr += 1
            else:
                if curr > 2:
                    l.append(curr)
                curr = 1
        if curr > 2:
            l.append(curr)
        return l

    def uppercaseCheck(self, s: str) -> int:
        if re.search("[A-Z]", s) is None:
            return 1
        return 0

    def lowercaseCheck(self, s: str) -> int:
        if re.search("[a-z]", s) is None: return 1
        return 0

    def numberCheck(self, s: str) -> int:
        if re.search("[0-9]", s) is None: return 1
        return 0

    def strongPasswordChecker(self, s: str) -> int:
        leng = len(s)

        if leng <= 4: return 6 - leng

        lis = self.lengthCheck(s)

        if leng is 5:
            if self.uppercaseCheck(s) + self.lowercaseCheck(s) + self.numberCheck(s) == 2: return 2
            return 1

        if not leng > 20:
            return max(sum(map(lambda x: int(x / 3), lis)),
                       self.uppercaseCheck(s) + self.lowercaseCheck(s) + self.numberCheck(s))

        if leng > 20:

            numdel = leng - 20

            runreplace = sum(map(lambda x: int(x / 3), lis))

            l = list(map(lambda x: (x % 3) + 1, lis))
            l.sort()

            rem = numdel

            for i in range(0, len(l)):
                if rem >= l[i]:
                    rem -= l[i]
                    runreplace -= 1

            runreplace -= int(rem / 3)

            if (runreplace < self.uppercaseCheck(s) + self.lowercaseCheck(s) + self.numberCheck(
                s)): runreplace = self.uppercaseCheck(s) + self.lowercaseCheck(s) + self.numberCheck(s)

            return numdel + runreplace
        return 0