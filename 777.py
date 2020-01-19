class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        flag_l, flag_r = 0, 0
        N = len(start)
        while flag_l < N and flag_r < N:
            while flag_l < N - 1 and start[flag_l] == 'X':
                flag_l += 1
            while flag_r < N - 1 and end[flag_r] == 'X':
                flag_r += 1
            if start[flag_l] != end[flag_r]:
                return False
            if start[flag_l] == 'L' and flag_l < flag_r:
                return False
            if start[flag_l] == 'R' and flag_l > flag_r:
                return False
            flag_l += 1
            flag_r += 1
        return True
