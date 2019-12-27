class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        for x in b:
            res = self.pow(res, 10) * self.pow(a, x) % 1337
        return res

    def pow(self, a, b):
        if b == 0 or a == 1: return 1
        if b % 2:
            return a * self.pow(a, b - 1) % 1337
        return self.pow((a * a) % 1337, b / 2) % 1337
