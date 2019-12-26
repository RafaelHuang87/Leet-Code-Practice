class Solution:
    def reverseString(self, s: [str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s or len(s) == 1:
            return s
        left, right = 0, len(s) - 1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

s = Solution()
print(s.reverseString(["h","e","l","l","o"]))