class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return s
        temp = list(s)
        left, right = 0, len(s) - 1
        vowels = "aeiouAEIOU"
        while left <= right:
            if temp[left] not in vowels:
                left += 1
                continue
            if temp[right] not in vowels:
                right -= 1
                continue
            temp[left], temp[right] = temp[right], temp[left]
            left += 1
            right -= 1
        temp = ''.join(temp)
        return temp

s = Solution()
print(s.reverseVowels("hello"))