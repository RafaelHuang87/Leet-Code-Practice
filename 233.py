class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        ln = len(str(n))
        if ln == 1:
            return 1
        tmp1 = 10 ** (ln - 1)
        firstnum = n // tmp1
        fone = n % tmp1 + 1 if firstnum == 1 else tmp1
        other = firstnum * (ln - 1) * (tmp1 // 10)
        return fone + other + self.countDigitOne(n % tmp1)
