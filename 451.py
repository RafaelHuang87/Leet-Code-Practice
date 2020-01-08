class Solution:
    def frequencySort(self, s: str) -> str:
        if len(s) == 1 or not s:
            return s
        temp = dict()
        for word in s:
            if word not in temp:
                temp[word] = 1
            else:
                temp[word] += 1
        res = ''
        for val in sorted(temp, key=temp.__getitem__, reverse=True):
            res += val * temp[val]
        return res

s = Solution()
print(s.frequencySort("tree"))

