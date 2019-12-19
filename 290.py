class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str_list = str.split()
        if len(str_list) != len(pattern) or len(set(str_list)) != len(set(pattern)):
            return False

        d = {}
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]] = str_list[i]
            else:
                if d[pattern[i]] != str_list[i]:
                    return False
        return True