class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        n = len(x)
        x.append(0.5)
        if n < 4:
            return False
        grow = x[2] > x[0]

        for i in range(3, n):
            if not grow and x[i] >= x[i-2]:
                return True
            if grow and x[i] <= x[i-2]:
                grow = False
                if x[i] + x[i-4] >= x[i-2]:
                    x[i-1] -= x[i-3]
        return False