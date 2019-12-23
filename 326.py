class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 0:
                n /= 3
            else:
                break
        return True if n == 1 else False