import itertools

class Solution:
    def findSubstring(self, s: str, words: [str]) -> [int]:
        if len(words) == 0: return []
        wordsDict = {}
        for word in words:
            if word not in wordsDict:
                wordsDict[word] = 1
            else:
                wordsDict[word] += 1

        n, m, k = len(s), len(words[0]), len(words)
        res = []
        print(n - m * k + 1)
        for i in range(n - m * k + 1):
            j = 0
            cur_dict = {}

            while j < k:
                word = s[i + m * j:i + m * j + m]
                if word not in wordsDict:
                    break
                if word not in cur_dict:
                    cur_dict[word] = 1
                else:
                    cur_dict[word] += 1
                if cur_dict[word] > wordsDict[word]:
                    break
                j += 1
            if j == k: res.append(i)

        return res


s = Solution()
print(s.findSubstring("barfoothefoobarman", ["foo","bar"]))