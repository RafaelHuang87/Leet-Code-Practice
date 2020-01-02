class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if len(stones) <= 1:
            return True
        elif stones[1] != 1:
            return False
        else:
            maxJumpstep = {s: set() for s in stones}
        maxJumpstep[1].add(1)
        for s in stones[1:-1]:
            for j in maxJumpstep[s]:
                for jump in (j - 1, j, j + 1):
                    if jump > 0 and s + jump in maxJumpstep:
                        maxJumpstep[s + jump].add(jump)
        return len(maxJumpstep[stones[-1]]) > 0
