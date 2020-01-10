class Solution:
    def findComplement(self, num: int) -> int:
        temp = 1
        s = str(bin(num))
        length = len(s)-2
        while length:
            length -= 1
            num = num ^ temp
            temp *= 2
        return num