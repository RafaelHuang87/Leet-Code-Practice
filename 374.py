# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                high = mid - 1
            else:
                low = mid + 1
