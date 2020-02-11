class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if s1 == s2:
            return True
        if l2 < l1:
            return False
        s = "abcdefghijklmnopqrstuvwxyz"
        dict1 = {}
        dict2 = {}

        for i in range(len(s)):
            dict1[s[i]] = 0
            dict2[s[i]] = 0

        for i in range(l1):
            dict1[s1[i]] += 1
            dict2[s2[i]] += 1

        if dict1 == dict2:
            return True

        for i in range(l2 - l1):
            dict2[s2[i]] -= 1
            dict2[s2[i + l1]] += 1
            if dict1 == dict2:
                return True

        return False