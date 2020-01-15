class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        import math
        if num == 1:
            return True
        sums = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                sums += i + num // i
            if i == num // i:
                break
        return sums == num