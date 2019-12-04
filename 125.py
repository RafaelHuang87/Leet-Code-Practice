
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        temp = []
        for i in s.lower():
            if i.isdigit() or i.isalpha():
                temp.append(i)
        return temp == temp[::-1]
s = Solution()
print(s.isPalindrome("0P"))
