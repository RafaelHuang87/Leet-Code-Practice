class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack or len(needle) > len(haystack):
            return -1
        if needle == haystack:
            return 0
        query_len = len(needle)
        p = 0
        flag = -1
        while p + query_len <= len(haystack):
            if haystack[p: p+query_len] == needle:
                flag = p
                return flag
            else:
                p = p + 1
        return flag

s = Solution()
print(s.strStr("mississippi", "pi"))