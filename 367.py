class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1 or num == 4:
            return True
        left = 0
        right = num // 2

        while left < right:
            mid = (left + right) // 2
            if mid ** 2 > num:
                right = mid - 1
            elif mid ** 2 == num:
                return True
            else:
                left = mid + 1

        if left ** 2 == num:
            return True
        else:
            return False