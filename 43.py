class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        nums1, nums2 = 0, 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i, v in enumerate(num1):
            offset = ord(v) - ord('0')
            nums1 += offset * (10 ** i)

        for i, v in enumerate(num2):
            offset = ord(v) - ord('0')
            nums2 += offset * (10 ** i)

        return str(nums1 * nums2)

s = Solution()
print(s.multiply('2', '3'))