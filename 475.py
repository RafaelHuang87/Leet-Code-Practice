class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        heaters = [float('-inf')]+heaters+[float('inf')]
        r = i = 0
        for x in sorted(houses):
            while x > heaters[i+1]:
                i += 1
            dis = min (x - heaters[i], heaters[i+1]- x)
            r = max(r, dis)
        return r
