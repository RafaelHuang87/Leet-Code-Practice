class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ""
        while n != 0:
            result = chr((n - 1) % 26 + 65) + result
            n = (n - 1) // 26
        return result