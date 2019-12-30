class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        import collections
        r = collections.Counter(ransomNote)
        m = collections.Counter(magazine)

        for key in r:
            if m.get(key, 0):
                if m[key] < r[key]:
                    return False
            else:
                return False

        return True
