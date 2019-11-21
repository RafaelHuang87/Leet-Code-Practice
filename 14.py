class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if '' in strs or not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        min_len = min([len(x) for x in strs])
        end = 0
        while end < min_len:
            for i in range(1, len(strs)):
                if strs[i][end] != strs[i-1][end]:
                    return strs[0][:end]
            end += 1
        return strs[0][:end]

s = Solution()
print(s.longestCommonPrefix(["flower","owfl","flight"]))
