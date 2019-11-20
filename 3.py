class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        temp = dict()
        i = 0
        max_dis = 0
        for k in range(len(s)):
            if s[k] in temp:
                i = max(temp[s[k]] + 1, i)
            temp[s[k]] = k
            max_dis = max(k - i + 1, max_dis)
        return max_dis