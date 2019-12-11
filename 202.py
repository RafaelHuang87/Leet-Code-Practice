class Solution:
    def isHappy(self, n: int) -> bool:
        mem = set()
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n not in mem:
                mem.add(n)
            else:
                return False
        return True
