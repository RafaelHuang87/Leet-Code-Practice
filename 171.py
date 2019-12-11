class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for letter in s:
            result = result * 26 + ord(letter) - ord('A') + 1
        return result