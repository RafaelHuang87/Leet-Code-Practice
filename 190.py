class Solution:
    def reverseBits(self, n: int) -> int:
        res = '{0:032b}'.format(n)[::-1]
        res = int(res, 2)
        return res

s = Solution()
print(s.reverseBits(00000010100101000001111010011100))