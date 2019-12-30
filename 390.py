class Solution:
    def lastRemaining(self, n: int) -> int:
        return self.help(n, True)

    def help(self, n, flag):
        if n == 1:
            return 1
        if flag:
            return 2 * self.help(n // 2, False)
        else:
            return 2 * self.help(n // 2, True) - 1 + n % 2