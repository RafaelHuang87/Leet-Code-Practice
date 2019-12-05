class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        if len(s) == 0 or not wordDict:
            return []
        strides = [len(x) for x in wordDict]
        max_stride = max(strides)
        stride_set = set(strides)
        if self.canBreak(s, wordDict):
            self.sub_wordBreak(s, wordDict, max_stride, stride_set, [], res)
        return res

    def sub_wordBreak(self, sub_s, wordDict, max_stride, stride, cur_result, result):
        if len(sub_s) == 0:
            result.append(" ".join(cur_result))
        else:
            for stride_length in stride:
                if stride_length <= len(sub_s):
                    if sub_s[:stride_length] in wordDict:
                        self.sub_wordBreak(sub_s[stride_length:], wordDict, max_stride, stride,
                                           cur_result + [sub_s[:stride_length]], result)

    def canBreak(self, s, wordDict):
        if s in wordDict:
            return True
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]
